import yaml
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from getRootPath import root_dir

class ReadYaml:
  def __init__(self, yaml_path):
    self.yamlPath = yaml_path

  def readCaseList(self):
    with open(self.yamlPath, 'r', encoding='utf-8') as fp:
      contents = fp.read()
      case_list = []
      testCase_dict = yaml.safe_load(contents)
      for  key, info in testCase_dict.items():
        new_dict = {}
        new_dict[key] = info
        case_list.append(new_dict)
      return case_list


if __name__ == '__main__':
  ry = ReadYaml(os.path.join(root_dir, 'yamlCase', 'loginCase.yaml'))
  ry.readCaseList()
