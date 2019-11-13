# CrisPy-Disco
a small Python script that lists a youtube playlist into a google spreadsheet

## How to use ?
requires python 3 with [pip](https://pypi.org/project/pip/)
To run the source code, you need:
*  [Google API Client](https://github.com/googleapis/google-api-python-client)
*  [GSpread](https://gspread.readthedocs.io/en/latest/)
*  [OAuth2 client](https://pypi.org/project/oauth2client/)

To be able to use this script, you need a google application created [here](https://console.developers.google.com/apis), that has access to the `Youtube API v3` and the `Google Sheets API` with file editing permissions. You should then get 2 thigs:
*  For the `Google Spreadsheets API`, you will get a file, that contains a JSON objet (you can follow [this tutorial](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) to be sure to do it right). You sould rename that file `client.secret.json` and place it alongside the `main.py` file.
*  For the `Youtube API`, you will simply get a OAuth2 token, that you sould be putting in a `client.secret.txt`, alongside `main.py`.
After that, simply execute the script using `python main.py`.
