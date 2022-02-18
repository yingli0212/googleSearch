# ---------------------------------------------------------------
# This program shows how web service "googleSearch" works.
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------

import json
from flask import Flask, request, render_template
import authMethode
import authVerify
import tParser_Post

app = Flask(__name__)
# This webapp uses CURL as client response and Jsonfile as output
# Command in cmd: curl "http://localhost:5000/search?username=admin&password=password&keyword=facebook" > result.json
# Authentication is realized by using username and password, which could be improved by using public key and private key

#   Dynamic generation of secret key (gtoken) is deactived in the test pahse
#   gtoken = pyotp.random_base32(64)  # get secret key 获取随机密钥，存于用户表中,随机64位
#   [a, qrcodepath] = authMethode.get_qrcode(gtoken, 'chunyuwang1@gmail.com')  # generate qr code by using secret key
gtoken = "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE"
qrcodepath = "../static/7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE.png"
print(gtoken)
print(qrcodepath)
users = {"admin": "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE", "lisa": "exampellel"}


#   in curl: curl "http://localhost:5000/signin?keyword=bosch"
#   in curl: curl "http://localhost:5000/search?username=admin&password=password&verifycode=verifycode&keyword=facebook" > result.json
@app.route('/search', methods=['GET'])
def search():
    """search
    """
    username = request.args.get("username")
    print(username)
#    password = request.args.get("password")
#    print(password)
    verifycode = request.args.get("verifycode")
    print(verifycode)
    secret_key = gtoken  # eindeutig zu jedem Benutzer, QRcode generated
    keyword = request.args.get("keyword")
    print(keyword)
#    if username == 'admin' and password == 'password' and authVerify.Google_Verify_Result(secret_key, verifycode):
    if authVerify.Google_Verify_Result(users[username], verifycode):
        #Authentication without password
        #   return a Json file
        filename = tParser_Post.searchresults(keyword)
#        jsonfile = json.load(filename)
        with open(filename) as f:
            dictionary = json.load(f)
        print(dictionary)
        return dictionary
    else:
        return "Bad User!"


if __name__ == '__main__':
    app.run()
