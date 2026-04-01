#!/bin/bash

## Work in progress

SRC_BRANCH = "master"

echo "Running update script"

echo "Killing process first"

# Deactivate current virtualenv
deactivate

echo "Fetch code from remote branch $SRC_BRANCH"
echo git remote -v

git checkout master
git pull

echo "Restarting"

bash ./run.sh

