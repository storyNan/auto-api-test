import requests
import json

class SendRequest(object):
  def __init__(self):
    pass

  
  def send(self, url, method, headers="",params=''):
    res = None
    if method.lower() == 'get':
      res = requests.get(url,headers = headers, params=params)
      return res
    elif method.lower() == 'post':
      if len(params) > 0:
        res = requests.post(url, headers = headers, data=json.dumps(params))
      else:
        res = requests.post(url, headers = headers)
      return res
    elif method.lower() == 'put':
      if params is not None:
        res = requests.put(url, headers = headers, data=json.dumps(params))
      else:
        res = requests.put(url)
      return res
    elif method.lower == 'delete':
      if params is not None:
        res = requests.delete(url, hearders=headers, data=params)
      else: 
        res = requests.put(url, hearders=headers)
      return res
    else:
      return {"msg": '错误的请求'}

    

if __name__ == '__main__':
  getRequest = SendRequest()
  headers = {"Content-Type":"application/json"}
  
  res = getRequest.send('http://127.0.0.1:8082/login', 'POST', headers=headers, params={'username': 'admin', 'password':'admin'})


