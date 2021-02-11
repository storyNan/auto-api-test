from marshmallow import Schema, fields, validate, validates

class LoginSchema(Schema):
  # 登录参数验证
  username = fields.String(required=True, validate=validate.Length(min=5, max=11))
  password = fields.String(required=True, validate=validate.Length(min=5, max=11))

class ArticleSchema(Schema):
  # 添加文章参数验证
  title = fields.String(required=True, validate=validate.Length(min=1, max=20))
  user_name = fields.String(required=True, validate=validate.Length(min=5, max=11))
  user_image = fields.String()
  summary = fields.String(required=True, validate=validate.Length(min=20, max=200))
  content = fields.String(required=True,validate=validate.Length(min=20))
  editType = fields.String(required=True)




