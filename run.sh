#!/bin/bash


# Activate venv
source ./bin/activate

# See if token is set to ENV
if [ -z "$API_TOKEN" ]; then
    echo "API Token set"
else
    echo "Error: Bot API Token is not set. Solution: Set it."
    exit 1
fi

# Run Python with recommended flags
# -u: Unbuffered stdout/stderr (essential for real-time logging)
# -B: Prevents writing .pyc files (keeps your directory clean)
python3 -u -B main.py "$@"
