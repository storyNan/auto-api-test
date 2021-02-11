import configparser
import os
from getRootPath import root_dir

config_path = os.join(root_dir, "conf", "config.ini")
cf = configparser.ConfigParser()

flag = "Test"

def getConf(name):
  cf.read(config_path, encoding="utf-8")
  section = cf.sections()
  options = cf.options(flag)
  return cf.get(flag, name)
