#!/bin/sh
pr_files=`curl "https://api.github.com/repos/$TRAVIS_REPO_SLUG/pulls/$TRAVIS_PULL_REQUEST/files" | jq '.[] | .filename' | tr '\n' ' ' | tr '"' ' '`

fontbakery check-googlefonts $pr_files -l FAIL
