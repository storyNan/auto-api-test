import os
import sys
import logging
import time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from getRootPath import root_dir

logger_path = os.path.join(root_dir, 'logs')

class Logger:
  def __init__(self):
    self.log_name = os.path.join(logger_path, '%s.log' % time.strftime('%Y_%m_%d'))
    self.logger = logging.getLogger()
    self.logger.setLevel(logging.DEBUG)

    self.formatter = logging.Formatter("%(asctime)s - %(filename)s- %(levelname)s : %(message)s")

  def _console(self, level, message):
    file_local = logging.FileHandler(self.log_name, 'a', encoding="UTF-8")
    file_local.setLevel(logging.DEBUG)
    file_local.setFormatter(self.formatter)
    self.logger.addHandler(file_local)

    # file_stream = logging.StreamHandler()
    # file_stream.setLevel(logging.DEBUG)
    # file_stream.setFormatter(self.formatter)
    # self.logger.addHandler(file_stream)
    if level == 'info':
      self.logger.info(message)
    elif level == 'debug':
      self.logger.debug(message)
    elif level == 'warning':
      self.logger.warning(message)
    elif level == 'error':
      self.logger.error(message)

    # 这两行代码是为了避免日志输出重复问题
    # self.logger.removeHandler(file_stream)
    self.logger.removeHandler(file_local)

    # 关闭打开的文件
    file_local.close()

  def debug(self, message):
    self._console('debug', message)
  
  def info(self, message):
    self._console('info', message)

  def warning(self, message):
    self._console('warning', message)

  def error(self, message):
    self._console('error', message)

  def writeLog(self, case, url, data, check, text):
    self.info("#" * 100 + "开始测试" + "#" * 100)
    self.info("用例名字：{}".format(case))
    self.info("请求接口地址：{}".format(url))
    self.info("请求参数：{}".format(data))
    self.info("-" * 200)
    self.info("期望结果：{}".format(check))
    self.info("实际结果：{}".format(text))
    self.info("#" * 100 + "测试结束" + "#" * 100)

if __name__ == "__main__":
    log = Logger()
    log.info("---测试开始----")
    log.info("操作步骤1,2,3")
    log.warning("----测试结束----")


