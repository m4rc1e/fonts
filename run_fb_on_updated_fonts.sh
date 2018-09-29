#!/bin/sh
echo `curl "https://api.github.com/repos/$TRAVIS_REPO_SLUG/pulls/$TRAVIS_PULL_REQUEST/files"`
file_names=`curl "https://api.github.com/repos/$TRAVIS_REPO_SLUG/pulls/$TRAVIS_PULL_REQUEST/files" | jq '.[] | .filename' | tr '\n' ' ' | tr '"' ' '`
echo $file_names
fontbakery check-googlefonts $file_names -l FAIL
