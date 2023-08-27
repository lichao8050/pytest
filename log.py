# _*_ coding: utf-8 _*_
# @Time    : 2021/9/9 17:34
# @Author  : Mr_Li
# @FileName: log.py
# logging 日志封装==========
import logging


class Log(object):

    def __init__(self, name=__name__, path='../untitled/logs/mylog.log', level='DEBUG'):
        self.__name = name
        self.__path = path
        self.__level = level
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def __ini_handler(self):
        """初始化handler"""
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.__path, encoding='utf-8')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回 logger """
        stream_handler, file_handler = self.__ini_handler()
        self.__set_handler(stream_handler, file_handler)
        self.__set_formatter(stream_handler, file_handler)
        self.__close_handler(stream_handler, file_handler)
        return self.__logger


# import logging
# import os
# import time
# # log_path是日志存放路径地址
# get_path = os.path.dirname(os.path.abspath('./log'))
# log_path = os.path.join(os.path.dirname(get_path),"log")
# # 如果不存在这个logs文件夹，就自动创建一个
# if not os.path.exists(log_path):os.mkdir(log_path)
#
# class Log():
#     def __init__(self):
#         # 文件的命名
#         self.logname = os.path.join(log_path,"%s.log"%time.strftime("%Y:%m:%d"))
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#         # 日志输出格式
#         self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
#
#     def __console(self,level,message):
#
#         # 创建一个FileHandler，用于写到本地
#         fh = logging.FileHandler(self.logname,"a",encoding='utf-8') # 追加模式
#         fh.setLevel(logging.DEBUG)
#         fh.setFormatter(self.formatter)
#         self.logger.addHandler(fh)
#
#         # 创建一个StreamHandler,用于输出到控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         ch.setFormatter(self.formatter)
#         self.logger.addHandler(ch)
#
#         if level == "info":
#             self.logger.info(message)
#         elif level == "debug":
#             self.logger.debug(message)
#         elif level == "warning":
#             self.logger.warning(message)
#         elif level == "error":
#             self.logger.error(message)
#
#          # 这两行代码是为了避免日志输出重复问题
#         self.logger.removeHandler(ch)
#         self.logger.removeHandler(fh)
#
#         # 关闭打开的文件
#         fh.close()
#
#     def debug(self,message):
#         self.__console("debug",message)
#     def info(self,message):
#         self.__console("info",message)
#     def warning(self,message):
#         self.__console("warning",message)
#     def error(self,message):
#         self.__console("error",message)
#
# if __name__ == "__main__":
#     log = Log()
#     log.info("--测试开始--")
#     log.info("操作步骤1，2,3")
#     log.warning("--测试结束--")

# import logging
# from logging import handlers
#
# class Log(object):
#     level_relations = {
#         'debug': logging.DEBUG,
#         'info': logging.INFO,
#         'warning': logging.WARNING,
#         'error': logging.ERROR,
#         'crit': logging.CRITICAL
#     }  # 日志级别关系映射
#
# def __init__(self, filename='mylog.log', level='debug', when='D', backCount=3, fmt='%(asctime)s - %(pathname)s[
# line:%(lineno)d] - %(levelname)s: %(message)s'): self.logger = logging.getLogger(filename) format_str =
# logging.Formatter(fmt)  # 设置日志格式 self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别 sh =
# logging.StreamHandler()  # 往屏幕上输出 sh.setFormatter(format_str)  # 设置屏幕上显示的格式 th = handlers.TimedRotatingFileHandler(
# filename=filename,when=when,backupCount=backCount,encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器 #
# 实例化TimedRotatingFileHandler #  interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种： # S 秒
# M 分        # H 小时、        # D 天、        # W 每星期（interval==0时代表星期一）        # midnight 每天凌晨 th.setFormatter(
# format_str)  # 设置文件里写入的格式 self.logger.addHandler(sh)   # 把对象加到logger里 self.logger.addHandler(th)
#
#     @property
#     def Logger(self):
#         """构造收集器，返回 logger """
#         return self.logger
