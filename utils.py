# 导包
import app_config
import logging
from logging import handlers
import json
# 编写初始化日志的代码
# 1 首先定义一个初始化日志的函数
from app_config import BASE_DIR


def init_logging():
    # 2 在函数中，设置日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 设置控制台处理器
    sh = logging.StreamHandler()
    # 5 设置文件处理器（文件处理的作用是设置保存日志的文件地址的：需要使用项目根目录定位到日志文件）
    log_path = app.BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when='M',
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding='utf-8')
    # 6 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 7 将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8 将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)

def get_json():
    with open(BASE_DIR+"/data/login.json","r",encoding="utf-8") as file:
        json_data = json.load(file)
        data_return = []
        for i in json_data:
            data = []
            for x in i.values():
                data.append(x)
            data_return.append(data)
        return data_return


# 封装通用断言函数
def assert_common(self, msg, response):
    """
    :param self:
    :param msg: 断言消息组成的列表
    :param response: requests返回的数据
    :return:
    """
    for i in msg:
        self.assertEqual(i, str(response))



if __name__ == '__main__':
    print(get_json())
    print(__name__)