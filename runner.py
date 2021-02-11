import time
import os
import unittest

root_dir = os.path.dirname(os.path.abspath(__file__))

def run():
  test_dir = os.path.join(root_dir, 'cases')
  discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
  now = time.strftime("%Y-%m-%d %H-%M-%S")


if __name__ ==  "__main__":
  run()





