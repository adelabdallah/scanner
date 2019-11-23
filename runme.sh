#!/bin/bash

# navigate to root directory of repository

python3 -m venv env

source env/bin/activate

echo "Confirm activation of venv:"
echo 
echo `which python`
echo

pip install -r requirements.txt

exit 0