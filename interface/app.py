#code: UTF-8
from flask import Flask, session, request, abort
import json
import sys
import os
import time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.orm import DB_Operation
from common.decoration import Decoration
from common.schema_cls import LoginSchema, ArticleSchema

app = Flask(__name__)
app.secret_key = '1234'
db_conn = DB_Operation()

@app.route('/login', methods=['POST'])
@Decoration.validatSchema(LoginSchema)
def login():
  # 登录并获取session
  username = request.args.get('username')
  password = request.args.get('password')
  if username == None or password == None:
    return {"msg": "账户哦或密码错误"}
  else:
    try:
      sql = "select * from user where user.name='%s' and user.password='%s'"
      items = db_conn.query(sql, True, username, password)
      if items == None:
        return {"msg": "账号或密码错误"}
      if 'username' in session:
        session.pop('username', None)
      session['username'] = username
      return {"msg": "登录成功"}
    except Exception as e:
      return abort(500)
    

@app.route('/logout', methods=['GET'])
def logout():
  # 退出
  session.pop('username', None)
  return {"msg": "退出登录"}


@app.route('/getData', methods=['GET'])
@Decoration.isLogin
def getData():
  # 获取列表数据
  size = int(request.args.get('size'))
  pageNum = int(request.args.get('pagenum'))
  sql = "select * from blogs limit %s offset %s" 
  items = DB_Operation.query(sql, False, size, pageNum)
  return {
    "msg": "ok",
    "data": items
  }

@app.route('/addArticle', methods=['POST'])
@Decoration.isLogin
@Decoration.validatSchema(ArticleSchema)
def addArticle():
  # 新增文章
  title = request.args.get('title')
  user_name = request.args.get('username')
  user_image = request.args.get('user_image')
  summary = request.args.get('summary')
  content = request.args.get('content')
  created_at = time.time()
  articleId = request.args.get('articleId')
  editType = int(request.args.get('editType'))
  if title == None or username == None or summary == None or content == None:
    return {"msg": "参数不完整"}
  else:
    try:
      if editType == 1:
        sql = "inset into blogs (title, user_name, user_image, summary, content, created_at) values (%s %s %s %s %s %s)"
        items = db_conn.execute(sql, title, user_name, user_image, summary, content, created_at)
        print(items)
        return {"msg": "添加成功"}
      else:
        sql = "update blogs set title='%s',user_name='%s', user_image='%s', content='%s', summary='%s', created_at='%s' where blogs.id='%s'"
        items = db_conn.execute(sql, title, user_name, user_image, summary, content, created_at, articleId)
        print(items)
        return {"msg": "修改成功"}
    except Exception as e:
      return abort(500)


if __name__ == '__main__':
  app.run(port=8082, debug=True)