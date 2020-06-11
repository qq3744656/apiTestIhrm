import os
import logging
from logging import handlers

# BASE_DIR = os.path.abspath(__file__) // 显示当前文件目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# abspath格式化当前文件路径字符串 增加兼容性
# BASE_DIR = os.path.dirname(__file__)  # __file__为当前文件路径
# os.path.dirname(os.path.dirname(__file__)) 相当当前文件的文件夹的上层文件夹

print(BASE_DIR)

def init_logging():
    # 2 在函数中，设置日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 设置控制台处理器
    sh = logging.StreamHandler()
    # 5 设置文件处理器（文件处理的作用是设置保存日志的文件地址的：需要使用项目根目录定位到日志文件）
    log_path = BASE_DIR + "/log/ihrm.log"
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
# 定义一个初始化日至器函数
# def init_logging():
#     # 在函数中设置日志器
#     logger = logging.getLogger()
#     # 设置日志等级
#     logger.setLevel(logging.INFO)
#     # 设置控制台处理器
#     sh = logging.StreamHandler()
#     # 设置文件处理器
#     log_path = BASE_DIR + "/log/ihrm.log"
#     TRFH = logging.handlers.TimedRotatingFileHandler(filename=log_path, when="M", interval=1, backupCount=3,
#                                                      encoding="utf-8")
#
#     # 设置格式化器
#     # fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
#     fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] -%(message)s'
#     formatter = logging.Formatter(fmt)
#     # 7 将格式化器添加到文件处理器和控制台处理当中
#     sh.addFilter(formatter)
#     TRFH.addFilter(formatter)
#     # 8 将文件处理器和控制台处理器添加到日志器当中
#     logger.addHandler(sh)
#     logger.addHandler(TRFH)
