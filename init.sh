#!/bin/bash

if [ ! -d "venv" ]
then
    echo Creating virtualenv
    python3 -m venv venv

    source venv/bin/activate
    pip install -r requirements.txt

    if [ ! $? -eq 0 ]
    then
        echo "Can't create virtualenv"
        exit 1
    fi
fi