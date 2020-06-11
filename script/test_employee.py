# 导包
import unittest, logging
from api.login_api import LoginApi
from api.employee import EmployeeApi
import app


# 创建测试类
class TestIHRMEmployee(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化员工
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type":"application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))

    def test02_add_emp(self):
        logging.info("app.HEADERS的值是：{}".format(app.HEADERS))
        # 发送添加员工的接口请求
        response = self.emp_api.add_emp("祖冲之", "13986350828", app.HEADERS)
        # 打印添加员工的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        # 提取员工中的令牌并把员工令牌保存到全局变量中
        app.EMP_ID = response.json().get("data").get("id")
        # 打印保存的员工ID
        logging.info("保存到全局变量的员工的ID为：{}".format(app.EMP_ID))