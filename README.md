# Trackable Flask API

A demo website to generate a selected amount of strings of desirable lengths, using a trackable API with contexts from a simple Flask server.
It is associated with this [tutorial](https://dev.to/adrianluong/trackable-flask-api-using-eventsource-365f):

Follow these steps to set it up in your IDE's terminal:

- Using [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to install a desirable Python version, i.e **3.11.11**: `pyenv install 3.11.11`

    Other versions can be found by this command `pyenv install -l` and can be installed instead.

- Set up a virual environment with the installed Python version, named **.venv**: `[pyenv path]/3.11.11/bin/python -m venv .venv`, whereas **[pyenv path]** stands for the installed location of pyenv in your machine.

    If you want to set up with a different version of Python, replace **3.11.11** with that version.

- Activate the environment with:
    (in Mac OS and Linux): `source .venv/bin/activate`
    (in Windows): `source .venv/Scripts/activate`
    , whereas **[env path]** stands for where the environment has been set up.
    The environment is successfully activated when there is a (.venv) prefix in your terminal.

- Install all necessary packages: `pip install -r requirements.txt`.
- Run the demo: `flask run`.
