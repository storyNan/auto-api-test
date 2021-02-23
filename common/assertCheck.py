import unittest

class AssertCheck(unittest.TestCase):
  def check(self, hopeDict, text):
    if isinstance(hopeDict, dict):
      for key in hopeDict.keys():
        if isinstance(key, list):
          for item in key:
            self.assertIn(item, text[key])
        else:
          self.assertEqual(hopeDict[key], text[key])
    else:
      print("不符合规则")
      return {"text": "用例不符合规则"}


if __name__ == '__main__':
  case_list = {'code': '400,', 'success': '用户名/密码过长'}
  AssertCheck().check(case_list, {'code': '400,', 'success': '用户名/密码过长'})




