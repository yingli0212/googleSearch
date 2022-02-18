import time
import unittest
import logging
import authVerify


class PythonOrgSearch(unittest.TestCase):

    def test_verifycode_valid(self):
        """
        Test if a verifycode from Google Authenticator is valid
        """
        self.verifycode = input()
        # Enter a valid verifycode
        users = {"admin": "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE"}
        if authVerify.google_verify_result(users["admin"], self.verifycode):
            msg = "Test ok."
        else:
            msg = "Test FAILED."
        print(msg)

    def test_verifycode_non_realtime(self):
        """
        Test if an expired verifycode from Google Authenticator is valid
        """
        self.verifycode = input()
        # Enter a valid verifycode
        users = {"admin": "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE"}
        time.sleep(31)
        if authVerify.google_verify_result(users["admin"], self.verifycode):
            msg = "Test FAILED."
        else:
            msg = "Test ok."
        print(msg)

    def test_verifycode_length(self):
        """
        Test if a wrong verifycode is valid, e.g. part of an valid verifycode from Google Authenticator
        """
        verifycode = input()
        self.verifycode = verifycode[:4]
        # enter part of a valid verifycode as new verifycode
        users = {"admin": "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE"}
        if authVerify.google_verify_result(users["admin"], self.verifycode):
            msg = "Test FAILED."
        else:
            msg = "Test ok."
        print(msg)


if __name__ == "__main__":
    unittest.main()
