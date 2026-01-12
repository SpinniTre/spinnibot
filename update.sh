#!/usr/bin/env bash

set -e  # exit on error

SRC_BRANCH="sandbox"   # or "master"
VENV_DIR="myvenv"

echo "Running update script"



echo "Fetching code from remote branch '$SRC_BRANCH'"

git fetch
git checkout "$SRC_BRANCH"
git pull origin "$SRC_BRANCH"

BEFORE=$(git rev-parse HEAD)
git pull
AFTER=$(git rev-parse HEAD)

# Check if code has changed
if [[ "$BEFORE" != "$AFTER" ]]; then
    
    # Deactivate current virtualenv if active
    if [[ -n "$VIRTUAL_ENV" ]]; then
        echo "Deactivating current virtualenv"
        deactivate
    fi

    echo "Changes detected ($BEFORE <> $AFTER)"
    echo "Restarting"

    # Activate virtualenv
    if [[ ! -d "$VENV_DIR" ]]; then
        echo "Virtualenv not found: $VENV_DIR"
        exit 1
    fi

    echo "venv activated"
    source "./$VENV_DIR/bin/activate"

    # Install/update deps
    if [[ -f requirements.txt ]]; then
        pip install -r requirements.txt
    fi

else
    echo "No changes in branch. Done."
fi

# Run

echo "Run bot"
bash ./run.sh