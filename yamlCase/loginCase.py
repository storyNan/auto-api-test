method: "post"
url: "/login"

data: {"username": '', "password": ''}
check: 
  code: 400, 
  success: False


data: {"username": 'admin', "password": ''}
check: 
  code: 400,
  success: False


data: {"username": 'admin', "password": 'admin'}
check:
  code: 200,
  success: True

data: {"username": "123456789456786532322222", "password": "6666666666666666666666"}
check:
  code: 400,
  success: False
