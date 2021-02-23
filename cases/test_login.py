from ddt import ddt, data
import unittest
import json
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from getRootPath import root_dir
from common.readConf import getConf
from common.readYaml import ReadYaml
from common.assertCheck import AssertCheck
from common.sendRequest import SendRequest
from common.logger import Logger

@ddt
class  Test_login(unittest.TestCase):
  yaml_path = os.path.join(root_dir, 'yamlCase', 'loginCase.yaml')
  open_Yaml = ReadYaml(yaml_path)
  cases = open_Yaml.readCaseList()
  method = cases[0]["method"]
  uri = cases[1]["uri"]
  headers = {"Content-Type": "application/json;charset=UTF-8"}

  @classmethod
  def setUpClass(cls):
    print(getConf("api_host"))
    cls.url = getConf("api_host") + cls.uri
    print(cls.url)
    cls.client = SendRequest()

  @data(*cases[2:])
  def test_login(cls, case_list):
    for caseName, caseInfo in case_list.items():
      caseName = caseName
      case_data = caseInfo['data']
      case_check = caseInfo['check']
    res = cls.client.send(cls.url, method=cls.method, headers = cls.headers, params = case_data)
    res.encoding = 'UTF-8'
    text = res.text
    text_dict = json.loads(text)
    Logger().writeLog(caseName, cls.url, case_data, case_check, text_dict)
    AssertCheck().check(case_check, text_dict)
    

  def tearDown(self):
    pass

if __name__ == '__main__':
  unittest.main()