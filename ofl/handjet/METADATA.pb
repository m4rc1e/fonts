name: "Handjet"
designer: "Rosetta, David Březina"
license: "OFL"
category: "DISPLAY"
date_added: "2020-09-11"
fonts {
  name: "Handjet"
  style: "normal"
  weight: 400
  filename: "Handjet[ELGR,ELSH,wght].ttf"
  post_script_name: "Handjet-Regular"
  full_name: "Handjet Regular"
  copyright: "Copyright 2018 The Handjet Project Authors (https://github.com/rosettatype/Handjet/)"
}
subsets: "arabic"
subsets: "armenian"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "greek-ext"
subsets: "hebrew"
subsets: "korean"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "ELGR"
  min_value: 1.0
  max_value: 2.0
}
axes {
  tag: "ELSH"
  min_value: 0.0
  max_value: 16.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
registry_default_overrides {
  key: "ELSH"
  value: 2.0
}
source {
  repository_url: "https://github.com/rosettatype/handjet"
  commit: "91e0cf7d364d49c16cc79c43beab7dd97e629086"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Handjet[ELGR,ELSH,wght].ttf"
    dest_file: "Handjet[ELGR,ELSH,wght].ttf"
  }
  branch: "master"
}
stroke: "SANS_SERIF"
classifications: "DISPLAY"
