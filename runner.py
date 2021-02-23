import time
import os
import unittest
from BeautifulReport import BeautifulReport
from getRootPath import root_dir
from common.sendEmail import sendEmail

def run():
  test_dir = os.path.join(root_dir, 'cases')
  discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
  reportPath = os.path.join(root_dir, "logs")
  now = time.strftime("%Y-%m-%d %H_%M_%S")
  reportName = now + '测试报告.html'
  description = "接口自动化测试报告"
  BeautifulReport(discover).report(filename=reportName, description=description, report_dir=reportPath)
  # print(discover)
  report = os.path.join(reportPath, reportName)

  # 发送邮件
  sendEmail(report)


if __name__ ==  "__main__":
  run()





