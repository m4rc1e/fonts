import sys
import os
import requests
# from diffbrowsers.diffbrowsers import DiffBrowsers
# from diffbrowsers.browsers import gdi_browsers, all_browsers

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


def ci_diff():
    auth = (os.environ['BSTACK_USERNAME'], os.environ['BSTACK_ACCESS_KEY'])
    print(auth)
    print(os.environ['IMGUR_CLIENT_ID'])
    # diff = DiffBrowsers(auth, 'google-fonts', fonts_after, dst_dir=IMG_DIR)
    # diff.diff_View('waterfall', gen_gifs=True)
    # diff.update_browsers(gdi_browsers)
    # diff.diff_view('glyphs-all', gen_gifs=True)

    # gifs = []
    # for path, r, files in os.walk(IMG_DIR):
    #     for f in files:
    #         if not f.endswith('.gif'):
    #             continue
    #         gifs.append(os.path.join(path, f))
    # imgur_img_urls = post_images_to_imgur(gifs)


if __name__ == '__main__':
    ci_diff()
