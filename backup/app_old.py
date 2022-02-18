import json
from flask import Flask, request, render_template
import authMethode
import authVerify
import tParser_Post

app = Flask(__name__)
# This webapp uses webpage as webinterface on localhost to have a interaction with webserver

#   Dynamic generation of secret key (gtoken) is deactived in the test pahse
#   gtoken = pyotp.random_base32(64)  # get secret key 获取随机密钥，存于用户表中,随机64位
#   [a, qrcodepath] = authMethode.get_qrcode(gtoken, 'chunyuwang1@gmail.com')  # generate qr code by using secret key
gtoken = "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE"
qrcodepath = "../static/7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE.png"
print(gtoken)
print(qrcodepath)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html', qrcodepath=qrcodepath)


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    verifycode = request.form['verifycode']
    if username == 'admin' and password == 'password':
        if authVerify.Google_Verify_Result(gtoken, verifycode):
            return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/search', methods=['POST'])
#@app.route('/search?keyword='keyword', methods=['GET'])
def search():
    keyword = request.form['keyword']
    filename = tParser_Post.searchresults(keyword)
    io = open(filename, "r")
    dictionary = json.load(io)
    return render_template('search.html', movies=json.dumps(dictionary))


if __name__ == '__main__':
    app.run()
