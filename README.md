# Spinnibot ~~ Setup and documentation

1. Install python VENV
2. Activate Python Virtual Env (VENV)

https://docs.python.org/3/library/venv.html

### Linux
>source ./bin/activate

### Windows
>source Scripts\activate.bat

DO NOT include venv files to git

---

# How to run

## Setup
- Install packages etc.
- Add Telegram secret API token to <todo>
  - See if it's already set up `echo $<todo_token_name_here>`
- Run from bash script  `bash run.sh` (recommended) or run python main file.

---

# Package management

Using pip

Package list stored in `requirements.txt`

## Install dependencies

> pip install -r requirements.txt

## Update `requirements.txt`

>pip freeze > requirements.txt

# .sh files

update.sh: Updates the bot. Pulls latest code from git.
run.sh: Runs the bot. Checks that there is internet connection
