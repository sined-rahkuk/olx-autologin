# olx-autologin
Little Script for logging in OLX with clear agent (fetching proxies adderesses included, selenium webdriver with no cookies)

# Prerequisites
Install `selenium` package using `requirements.txt` file for `pip` package manager.
Please, ensure you have changed the `creds.json` file in the way it now contains all valid credentials that the program will use to log in with.

# Usage

Launch the script using `python main.py`, user will be prompted to type in the index of email/tel.number that were read from the `creds.json` file.
After valid index is entered, program will initiate the ***incognito-like*** browser session, navigate to olx page and log it automatically using choosen user credentials.
