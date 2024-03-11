name: "Figtree"
designer: "Erik Kennedy"
license: "OFL"
category: "SANS_SERIF"
date_added: "2022-07-21"
fonts {
  name: "Figtree"
  style: "normal"
  weight: 400
  filename: "Figtree[wght].ttf"
  post_script_name: "Figtree-Light"
  full_name: "Figtree Light"
  copyright: "Copyright 2022 The Figtree Project Authors (https://github.com/erikdkennedy/figtree)"
}
fonts {
  name: "Figtree"
  style: "italic"
  weight: 400
  filename: "Figtree-Italic[wght].ttf"
  post_script_name: "Figtree-LightItalic"
  full_name: "Figtree Light Italic"
  copyright: "Copyright 2022 The Figtree Project Authors (https://github.com/erikdkennedy/figtree)"
}
subsets: "greek-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/erikdkennedy/figtree"
  commit: "937cfe82ffa598f4965350aa9edfdf133f483d90"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Figtree[wght].ttf"
    dest_file: "Figtree[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Figtree-Italic[wght].ttf"
    dest_file: "Figtree-Italic[wght].ttf"
  }
  branch: "master"
}
minisite_url: "https://www.erikdkennedy.com/projects/figtree.html"
