#!/bin/bash

echo "With Hidden files: "
cd /dev/ && ls -1a | wc -l # hidden files
echo "Files: "
ls /dev/ | wc -l
