# TCP server - Data Networks 2

This repository is based on the implementation of a simple TCP server implementation.

## Installation

- Create a [virtual environment](https://docs.python.org/es/3/tutorial/venv.html) with the command

    #### windows
    `py -3 -m venv .venv`
    #### MacOS/Linux
    `python -m venv .venv` or `python3 -m venv .venv`

- Activate the virtual environment:

    #### Windows:
    `.venv\scripts\activate` or `.venv\scripts\activate.bat`
    #### In Linux or Mac:
    `source .venv/bin/activate`

    It should appear (venv) in the console. Whenever a new console is executed, the virtual machine has a libraries and dependencies other than those found in the normal Windows environment, this to maintain the integrity of the applications in the operating system.

    Linux/Mac `pip install --upgrade pip` or `python3 -m pip install --upgrade pip`
    Windows `python -m pip install --upgrade pip` 

- Install dependencies

    #### Windows 
    may require elevation
    `python3 -m pip install -r requirements.txt` or `py -3 -m pip install -r requirements.txt`
    #### MacOS/Linux
    `python -m pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt`
    #### Linux (Debian)
    `apt-get install python3-tk`
    `python3 -m pip install m-r requirements.txt`

## Execution

- With the virtual environment activated, run the following console command:

    `uvicorn app:app --reload --port 5010`

    for root open `http://127.0.0.1:5010/`

    for swagger open `http://127.0.0.1:5010/docs`

    to run main.py use uvicorn `main:app --reload --host 0.0.0.0 --port 80`

    in case you need to delete cache use this in Linux or Mac:
    `find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf`