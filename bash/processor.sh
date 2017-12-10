#!/bin/bash

echo "Give a num: "
read num

if [[ num -gt 20 ]]; then
    echo `uname --processor`
fi
