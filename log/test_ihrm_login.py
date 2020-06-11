# 导包
import unittest,logging
from api.login_api import LoginApi



# 创建unittest的类
class TestIHRMLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass
    # 编写登录成功函数
    def test01_login_success(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile":"13800000002","password":"123456"},
                             {"Content-Type":"application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))