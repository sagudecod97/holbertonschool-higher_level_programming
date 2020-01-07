#!/bin/bash
# Displays the size of the body of the response
touch file && curl -so /dev/null "$1" -w '%{size_download}' > file && echo "" >> file && cat file
