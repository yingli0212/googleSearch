import os
import unittest
import logging

logging.basicConfig(filename="../test_python_org_search.log", format='%(asctime)s - %(message)s', level=logging.DEBUG)


def test_output():
    cmd = 'curl "http://localhost:5000/search?username=admin&verifycode=644434&keyword=lidl" > /Users/xuhengwang/PycharmProjects/googleSearch/result.json'
    os.system (cmd)
    filepath = "/result.json"
    if os.path.exists(filepath):
        # check if the output file exists
        msg = "Test ok."
    else:
        msg = "Test FAILED."
    print(msg)


if __name__ == "__main__":
    test_output()
