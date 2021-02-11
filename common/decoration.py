from flask import Flask, session, request, abort
from functools import wraps
from marshmallow import Schema, ValidationError


class Decoration:
#  公共装饰器类
  def isLogin(func):
     # 验证接口session是否正确
    @wraps(func)
    def check_login(*args, **kwargs):
      if 'username' in session:
        return func(*args, **kwargs)
      else:
        return {"msg": "请先登录，session验证失败"}
    return check_login


  def validatSchema(schema_class: Schema):
    # 接口参数验证 装饰器
    def validateDecoration(views_function):
      @wraps(views_function)
      def innerValidate(*args, **kwargs):
        if request.method == 'GET':
          form_data = request.args
        else:
          if request.json:
            form_data = request.json
          else:
            form_data = request.form
        try:
          data = schema_class().load(form_data)
          request.schema_data = data
        except ValidationError as e:
          return abort(400)
        finally:
          views_function(*args, **kwargs)

      return innerValidate

    return validateDecoration
      


