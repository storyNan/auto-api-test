import pymysql
import asyncio

class DB_Operation:
  # 数据库操作类
  host = "localhost"
  username = "root"
  password = "root"
  dbname = "awesome"
  charset = "utf8"
  cursorclass = pymysql.cursors.DictCursor

  @classmethod
  def query(cls, sql, fetchone=False, *args, ):
    # 查询数据
    rs = None
    connection = pymysql.connect(
      host = cls.host,
      user = cls.username,
      password = cls.password,
      db=cls.dbname, 
      charset = cls.charset, 
      cursorclass = cls.cursorclass
    )
    try:
      with connection.cursor(cls.cursorclass) as cur:
        queryResult = cur.execute(cls.solve_sql(sql, args))
        if fetchone:
          rs = cur.fetchone()
        else:
          rs = cur.fetchall()
        return rs
    except Exception as e:
      print(e, 908)
    finally:
      connection.close()


  @classmethod
  def execute(cls, sql, response=False, *args):
    # 插入、更新数据库操作
    rs = None
    connection = pymysql.connect(
      host = cls.host,
      user = cls.username,
      password = cls.password,
      db = cls.dbname, 
      charset =cls.charset, 
      cursorclass = cls.cursorclass
    )
    try:
      with connection.cursor(cls.cursorclass) as cur:
        queryResult = cur.execute(sql)
        if response:
          rs = cur.fetchall()
        connection.commit()
    except Exception as e:
      print(e,90)
      connection.rollback()
    finally:
      connection.close()
    return rs

  @staticmethod
  def solve_sql(sql, args):
    # 格式化sql
    if len(args) == 0:
      return sql
    if sql.find('%') > -1:
      return sql % args
    elif sql.find('{') > -1:
      if type(args) is dict:
        return sql.format(args)
      else:
        return sql.format(args)
    else:
      return sql