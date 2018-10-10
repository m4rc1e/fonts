"""Generate before and after gifs using diffbrowsers. Upload them to imgur then post them to PR"""
import os
import requests
import json
from diffbrowsers.diffbrowsers import DiffBrowsers
from diffbrowsers.browsers import test_browsers
from diffbrowsers.gfregression import VIEWS
import time

IMG_DIR = 'imgs'
GFR_URL = ''


def post_image_to_gfr(path, uuid):
    """Post images to GF Regression"""
    url_endpoint = GFR_URL + '/api/upload-media'
    payload = [('files', open(f, 'rb')) for f in path]
    r = requests.post(
        url_endpoint,
        data={'uuid': uuid},
        files=payload
    )
    return r.json()['items']


def post_gh_msg(msg):
    r = requests.post("https://api.github.com/repos/{}/issues/{}/comments".format(os.environ['TRAVIS_REPO_SLUG'], os.environ['TRAVIS_PULL_REQUEST']),
        data=json.dumps({'body': msg}),
        headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
    print(r.text)


def get_fonts_in_pr():
    font_paths = []
    r = requests.get("https://api.github.com/repos/{}/pulls/{}/files".format(os.environ['TRAVIS_REPO_SLUG'], os.environ['TRAVIS_PULL_REQUEST']),
        headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
    for item in r.json():
        if item['filename'].endswith('.ttf'):
            font_paths.append(item['filename'])
    return font_paths


def main():
    post_gh_msg("Generating diff images.")

    fonts_after = get_fonts_in_pr()

    auth = (os.environ['BSTACK_USERNAME'], os.environ['BSTACK_ACCESS_KEY'])
    browsers_to_test = test_browsers['vf_browsers']
    diffbrowsers = DiffBrowsers(auth=auth,
                                gfr_instance_url='http://159.65.243.73',
                                dst_dir=IMG_DIR,
                                browsers=browsers_to_test)

    diffbrowsers.new_session('from-googlefonts', fonts_after)

    diffbrowsers.diff_view('waterfall', gen_gifs=True)
    diffbrowsers.update_browsers(test_browsers['gdi_browsers'])

    views_to_diff = diffbrowsers.gf_regression.info['diffs']
    for view in views_to_diff:
        if view in VIEWS:
            diffbrowsers.diff_view(view, pt=32, gen_gifs=True)

    gifs = []
    for path, r, files in os.walk(IMG_DIR):
        for f in files:
            if not f.endswith('.gif'):
                continue
            gifs.append(os.path.join(path, f))
    uuid = diffbrowsers.gf_regression.info['uuid']
    gfr_img_urls = [post_image_to_gfr(path, uuid) for path in gifs]

    img_msg = ""
    for url in gfr_img_urls:
        img_msg += '![alt text]({} "{}")\n\n'.format(url, url)
        img_msg += '*{}\n*'.format(url)
    post_gh_msg(img_msg)

if __name__ == '__main__':
    main()
