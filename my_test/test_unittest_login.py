import requests,unittest
from parameterized import parameterized

from utils import get_json


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    @parameterized.expand(get_json())
    def test_login(self,case_name,data,login_assert):
        response = requests.post(url=self.login_url,json=data)
        for i in login_assert.values():
            self.assertIn(i,str(response.json()))