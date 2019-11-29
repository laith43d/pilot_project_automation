#!/bin/bash

function create() {
    python create.py $1
    cd /Users/lzah/Desktop/PyDev/$1
    git init
    git remote add origin git@github.com:laith43d/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}