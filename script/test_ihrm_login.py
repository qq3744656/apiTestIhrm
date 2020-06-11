# 导包
import unittest, logging
from api.login_api import LoginApi

from utils import assert_common

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
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))

        assert_common(self, 200, True,10000,"操作成功", response)
3

        # 哪些是灵活变化的，哪些是固定的？
        # self 是灵活的吗？固定的
        # assertEqual 和 assertIn是固定的还是灵活变化的？
        # assertEqual和assertIn都是self的属性，所以我们需要把self作为一个参数
        # 传递给封装的函数
        # 预期数据是不是固定的？（200,True,10000，操作成功) 不是固定的，每个
        # 用例都不一样 预期数据也需要从外部传给封装的函数
        # response是固定吗？response的属性？它也有很多属性

