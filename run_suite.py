from my_test.test_unittest_login import TestLogin
import time
import unittest
from BeautifulReport import BeautifulReport
from app_config import BASE_DIR
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

report_name = "report" + ".html"
# report_name = time.strftime("%Y%m%d %H%M%S") + ".html"
report_dir = BASE_DIR + "/report"
BeautifulReport(suite).report(description="必填注释", filename=report_name,report_dir=report_dir)