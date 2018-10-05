"""Generate before and after gifs using diffbrowsers. Upload them to imgur then post them to PR"""
import sys
import os
import requests
import json
from diffbrowsers.diffbrowsers import DiffBrowsers
from diffbrowsers.browsers import gdi_browsers


IMG_DIR = 'imgs'


def post_images_to_imgur(paths):
    """Post images to hosting service imgur."""
    upload_urls = []
    for path in paths:
        r = requests.post('https://api.imgur.com/3/image',
            data={'image': open(path, 'rb').read(), 'type': 'file'},
            headers = {'Authorization': 'Client-ID {}'.format(os.environ['IMGUR_CLIENT_ID'])}
        )
        upload_urls.append(r.json()['data']['link'])
        time.sleep(1)
    return upload_urls


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
    print(fonts_after)

    auth = (os.environ['BSTACK_USERNAME'], os.environ['BSTACK_ACCESS_KEY'])
    diff = DiffBrowsers(auth, 'google-fonts', fonts_after, dst_dir=IMG_DIR)

    diff.diff_View('waterfall', gen_gifs=True)
    diff.update_browsers(gdi_browsers)
    diff.diff_view('glyphs-all', gen_gifs=True)

    gifs = []
    for path, r, files in os.walk(IMG_DIR):
        for f in files:
            if not f.endswith('.gif'):
                continue
            gifs.append(os.path.join(path, f))
    imgur_img_urls = post_images_to_imgur(gifs)

    img_msg = ""
    for url in imgur_img_urls:
        img_msg += '![alt text]({} "{}")\n\n'.format(url, url)
    post_gh_msg(img_msg)

if __name__ == '__main__':
    main()
