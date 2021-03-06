# ---------------------------------------------------------------
# This program shows how web service "googleSearch" works.
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------

import json
from flask import Flask, request, send_file
import auth_verify
import parser_post
import os

app = Flask(__name__)

users = {"admin": "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE",
         "lisa": "7MC7522FNP7MK6ZTR7XNMZIZUR3RNVHMC2JRQL5VORXWKIUBCASX3Z6M5NVPNQTK"}
# two test users are hard coded here into a dictionary with key/value {"username":"64 bits token"}. This could be
# extended later to a database.


@app.route('/')
def home():
    """ Show the welcome page of Webservice """
    return "Welcome to Webservice googleSearch!\n"


@app.route('/search', methods=['POST'])
def search():
    """ Verify the login user and active the search on google website """
#    username = request.args.get("username")
#    verifycode = request.args.get("verifycode")
#    keyword = request.args.get("keyword")

    if request.method == 'POST':
        username = request.form.get('username')
        verifycode = request.form.get('verifycode')
        keyword = request.form.get('keyword')

    if auth_verify.google_verify_result(users[username], verifycode):
        # Authentication with username and verifycode
        filename = parser_post.searchresults(keyword)
        # call the search in google
        # os.path.abspath(filename)
        io = open(filename, 'r')
        result = json.load(io)
        return result
#        return "You can get your output file here: " + os.path.abspath(filename) + "\n"
    else:
        return "Please check your username and verify code again!"


if __name__ == '__main__':
    app.run()
