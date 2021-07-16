#!/bin/bash

if [ "$1" == "" ] || ! [ -f "$1" ] || ! [[ "$1" == *.txt ]]; then
    echo "You need to provide file name as a argument to this script!"
    exit 0
fi

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

python3 main.py "$1"
