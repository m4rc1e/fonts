"""
Compare each encoding in ./encodings against one another and find 
codepoints which overlap.
"""
from ntpath import basename
import os


def get_files(directory, t):
    paths = []
    for f in os.listdir(directory):
        if f.endswith('.nam'):
            path = os.path.join(directory, f)
            paths.append(path)
    return paths


def get_codepoints(paths):
    nam_files = {}
    for path in paths:
        nam_file_key = str(basename(path))
        with open(path, 'r') as nam_file:
            sheet = nam_file.readlines()[1:]

            if nam_file not in nam_files:
                nam_files[nam_file_key] = set()
            for row in sheet:
                nam_files[nam_file_key].add(row.split(' ')[0])
    return nam_files


def gf_sheet_link(urls, url_text):
    gf_links = []
    for url, text in zip(urls, url_text):
        hyperlink = '=HYPERLINK("%s", "%s")' % (url, text)
        gf_links.append(hyperlink)
    return gf_links


def url_for_codepoints(codepoints):
    urls = []
    for codepoint in codepoints:
        urls.append('https://www.compart.com/en/unicode/U+' + codepoint[2:])
    return urls


def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    encodings_dir = os.path.join(script_dir, 'encodings')
    nam_files_path = get_files(encodings_dir, '.nam')
    code_points = get_codepoints(nam_files_path)


    for code1 in code_points:
        for code2 in code_points:
            if code1 == code2:
                continue
            shared_codepoints = code_points[code1] & code_points[code2]
            if shared_codepoints:
                print '%s\t%s\t%s' % (code1, code2, '\t'.join(shared_codepoints))

if __name__ == '__main__':
    main()
