import os
import logging
import sys
from backup import absoluteVal
from datetime import datetime
import time

logging.basicConfig(filename="test_python_org_search.log", format='%(asctime)s - %(message)s', level=logging.DEBUG)


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(absoluteVal.absolute_value(17) == 17)
    test(absoluteVal.absolute_value(-17) == 17)
    test(absoluteVal.absolute_value(0) == 0)
    test(absoluteVal.absolute_value(3.14) == 3.14)
    test(absoluteVal.absolute_value(-3.14) == 3.14)


def test_output():
#    cmd = 'curl "http://localhost:5000/search?username=admin&verifycode=644434&keyword=lidl" > /Users/xuhengwang/PycharmProjects/googleSearch/result.json'
#    os.system (cmd)
    filepath = "/Users/xuhengwang/PycharmProjects/googleSearch/result.json"
#    time = '%s\n' % os.stat(filepath).st_mtime
    filetime = time.ctime(os.stat(filepath).st_mtime)
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print(filetime)
 #   current_time =
    if os.path.exists(filepath):
        # check if the output file exists
        msg = "Test ok."
    else:
        msg = "Test FAILED."
    print(msg)


if __name__ == "__main__":
#    test_suite()
    test_output()
