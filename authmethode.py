# ---------------------------------------------------------------
# This program shows how to generate a 64-bit secret key for a certain
# user, as well as to generate a QRcode for this user.
# This program will be used during the registration of user for one time.
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------
import pyotp
from qrcode import QRCode, constants
import os
import traceback


def get_qrcode(secret_key, username):
    """
    Generate a QRcode for a certain secret key and certain user
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dirpath = os.path.join(BASE_DIR, 'googleSearch', 'static')
    # define the path to save QRcode
    data = pyotp.totp.TOTP(secret_key).provisioning_uri(username, issuer_name="IAM MFA Code")
    # generate the data content for QRcode
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=6,
        border=4)
    try:
        qr.add_data(data)
        qr.make(fit=True)
        # make QRcode with the best fit
        img = qr.make_image()
        # generate the image of QRcode
        filepath = dirpath + os.sep + secret_key + '.png'
        filepath_part = '../static' + os.sep + secret_key + '.png'
        img.save(filepath)
        # save the image of qrcode
        return True, filepath
    except Exception as e:
        traceback.print_exc()
        return False, None


def generate_gtoken():
    """
    Generate a secret key
    """
    gtoken = pyotp.random_base32(64)  # generate secret key, can be saved in user table in database, 64 bits
    return gtoken


#def transfer_gtoken(gtoken):
#    return gtoken


if __name__ == "__main__":
#    user = "lisa@gmail.com"
    user = input()
    gtoken = generate_gtoken()
    result = get_qrcode(gtoken, user)
