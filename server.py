from flask import Flask, request, redirect
import pymysql

app = Flask(__name__)

result=''
@app.route('/')
def index():
    return f'''<!doctype html>
        <html>
            <body>
               <a href="/show/">go</a>
            </body>
        </html>
        '''

@app.route('/show/')
def show():
    global result
    # database 접근
    db = pymysql.connect(host='',
     		           user='',
 		           password='',
 		           db='',
 		           charset='utf8')

    # database 사용하기 위한 cursor 세팅
    cursor = db.cursor()

    select1 = """SELECT * FROM node1"""
    select2 = """SELECT * FROM node2"""
    select3 = """SELECT * FROM node3"""

    # Sql query실행
    cursor.execute(select2)

    # 실행결과 가져오기
    result = cursor.fetchall()

    db.close()
    return f'''<!doctype html>
        <html>
            <body>
                {result}
            </body>
        </html>
        '''
app.run()
