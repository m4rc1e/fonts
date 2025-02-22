#!/usr/bin/env python3
#
# Copyright 2022 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys

if sys.version_info < (3, 10):
    import importlib_resources as importlib_resources
else:
    import importlib.resources as importlib_resources

from gflanguages import (LoadLanguages,
                         LoadRegions,
                         LoadScripts)

DATA_DIR = importlib_resources.files("gflanguages") / "data"


def test_LoadLanguages():
    with importlib_resources.as_file(DATA_DIR) as data_path:
        for langs in [LoadLanguages(),
                    LoadLanguages(None),
                    LoadLanguages(data_path)]:
            numerals = langs["yi_Hebr"].exemplar_chars.numerals
            assert numerals == '- , . % + 0 1 2 3 4 5 6 7 8 9'


def test_LoadScripts():
    with importlib_resources.as_file(DATA_DIR) as data_path:
        for scripts in [LoadScripts(),
                        LoadScripts(None),
                        LoadScripts(data_path)]:
            scripts = LoadScripts()
            assert scripts["Tagb"].name == 'Tagbanwa'


def test_LoadRegions():
    with importlib_resources.as_file(DATA_DIR) as data_path:
        for regions in [LoadRegions(),
                        LoadRegions(None),
                        LoadRegions(data_path)]:
            regions = LoadRegions()
            br = regions["BR"]
            assert br.name == 'Brazil'
            assert br.region_group == ['Americas']
