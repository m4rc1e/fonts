"""Generate before and after gifs using diffbrowsers. Upload them to imgur then post them to PR"""
import os
import shutil
import requests
import json
from diffbrowsers.diffbrowsers import DiffBrowsers
from diffbrowsers.browsers import test_browsers
from diffbrowsers.gfregression import VIEWS


IMG_DIR = 'imgs'
GFR_URL = 'http://159.65.243.73'


def post_images_to_gfr(paths, uuid):
    """Post images to GF Regression"""
    url_endpoint = GFR_URL + '/api/upload-media'
    payload = [('files', open(path, 'rb')) for path in paths]
    r = requests.post(
        url_endpoint,
        data={'uuid': uuid},
        files=payload
    )
    return [os.path.join(GFR_URL, i) for i in r.json()['items']]


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


def find_files(directory, ext='.gif'):
    """Recurs through directory and return files which have the given extension"""
    found_files = []
    for path, r, files in os.walk(directory):
        for f in files:
            if not f.endswith(ext):
                continue
            found_files.append(os.path.join(path, f))
    return found_files


def get_view_type_from_path(path):
    return path.split(os.path.sep)[-3]


def rename_img_to_include_view(path, dst):
    if not os.path.isdir(dst):
        os.mkdir(dst)
    view = get_view_type_from_path(path)
    filename = os.path.basename(path)
    new_filename = "%s_%s" % (view, filename)
    new_path = os.path.join(dst, new_filename)
    shutil.copy(path, new_path)
    return new_path


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

    gifs = find_files(IMG_DIR, ext='gif')
    gifs_to_post = [rename_img_to_include_view(p, dst='./tmp') for p in gifs]
    uuid = diffbrowsers.gf_regression.info['uuid']
    gfr_img_urls = post_images_to_gfr(gifs_to_post, uuid)

    img_msg = ""
    for url in gfr_img_urls:
        img_msg += '![alt text]({} "{}")\n\n'.format(url, url)
        img_msg += '*{}*\n'.format(os.path.basename(url))
    post_gh_msg(img_msg)

if __name__ == '__main__':
    main()
