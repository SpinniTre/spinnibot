# Setup

Activate Python Virtual Env (VENV)

https://docs.python.org/3/library/venv.html

### Linux
>source ./bin/activate

### Windows
>source Scripts\activate.bat

# Package management

Using pip

Packages are stored in `requirements.txt`

Update `requirements.txt`

>pip freeze > requirements.txt

# .sh files

update.sh: Updates the bot. Pulls latest code from git.
run.sh: Runs the bot. Checks that there is internet connection