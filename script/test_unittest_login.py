import requests,unittest


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_url = "http://ihrm-test.itheima.net/api/sys/login"
        cls.data = {"mobile": "13800000002", "password": "123456"}
        cls.headers = {"Content-Type": "application/json"}

    def test_login(self):
        response = requests.post(url=self.login_url,json=self.data,headers=self.headers)
        print(str(response.json()))
        response_str = str(response.json())
        for i in ["操作成功","True","10000"]:
            self.assertIn(i,response_str)
        # self.assertIn("True",response_str)
        # self.assertIn("10000",response_str)