import configparser
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from getRootPath import root_dir

config_path = os.path.join(root_dir, "conf", "config.ini")
cf = configparser.ConfigParser()

flag = "Test"

def getConf(name):
  cf.read(config_path, encoding="utf-8")
  section = cf.sections()
  options = cf.options(flag)
  return cf.get(flag, name)
