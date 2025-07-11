name: "Noto Sans Tangsa"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2022-09-12"
fonts {
  name: "Noto Sans Tangsa"
  style: "normal"
  weight: 400
  filename: "NotoSansTangsa[wght].ttf"
  post_script_name: "NotoSansTangsa-Regular"
  full_name: "Noto Sans Tangsa Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tangsa)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "tangsa"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/tangsa"
  commit: "8d40c34e78702e6ec2ef9a8e2cbd6a38cd7f6d4a"
  archive_url: "https://github.com/notofonts/tangsa/releases/download/NotoSansTangsa-v1.506/NotoSansTangsa-v1.506.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "NotoSansTangsa/googlefonts/variable/NotoSansTangsa[wght].ttf"
    dest_file: "NotoSansTangsa[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-tangsa.yaml"
}
is_noto: true
languages: "nst_Tnsa"
primary_script: "Tnsa"
