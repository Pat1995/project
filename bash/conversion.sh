#!/bin/bash

for f in `ls`; do
    filename=$(basename "$f")
    ext="${filename##*.}"
    filename="${filename%.*}"
    #echo $filename
    #echo $ext
    if [[ $ext == "jpg" ]]; then
        mv "$filename" "${filename%.png}"ll
    fi
done
