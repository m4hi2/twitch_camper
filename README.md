
# What is this?

Some times your sleep time doesn't go with some twitch event drops. So you let this sit as you and get drops for you. Bonus, it spams emotes too.

## How to install?

    *Use powershell if you're on Windows*

- Get [python3](https://realpython.com/installing-python/) and [pip](https://pip.pypa.io/en/stable/installing/)
- Run `pip install virtualenv` to install virtualenv
- Run `virtualenv venv --python=python3` to create a virtualenv
- Activate the virtualenv by `source ./venv/bin/activate` if you're on Linux/macOS and `& ./venv/Scrips/activate.ps1` from Windows powershell.
- Install the required libraries for this program by running `pip install -r requirements.txt`
- Download [Firefox Webdriver](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0) and put it in your `venv/Scripts` directory if you're on Windows and in `venv/bin` directory if you're on Linux/macOS

## How to use?

- Activate your virtualenv
- Run with `python main.py`
- A webbrowser with Twitch will open and you need to login there
- After the login, go to the channel you want to camp
- Notice the terminal you ran the script from, there should be a `Ready?` prompt there, type `1` then hit enter.
- You're good to go.
