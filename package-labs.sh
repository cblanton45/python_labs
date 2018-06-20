#!/bin/bash

## install nbconvert as
##      conda install nbconvert
##              or
##      pip install nbconvert

## cleanup html
find . -name "*.html" -print0 | xargs -0 rm -f

## convert ipynb notebooks into HTML
notebooks=$(find . -type f -name "*.ipynb" | grep -v ".ipynb_checkpoints" )

jupyter nbconvert ${notebooks}

rm -f *.zip
#git archive -o python-labs.zip .
zip -x '*.git*'  -x '*zip*'  -r python-labs.zip .
