# flask-env
Simple .env management 


## Setup
    $ git clone git@github.com:texuf/flask-env.git
    $ cd flask-env
    $ pipenv install
    $ pipenv run python app.py
    ...
    should fail with an exception asking you to create a .env file, so follow the instructions and then
    ...
    $ pipenv run python app.py

## Maintenance
    $ pipenv run python scripts/env.py # will build a .env.lock file


## IMPORTANT!!
    # Don't forget to add .env to your .gitignore!!! 
    # GitHub puts it there by default, but double check, just in case.