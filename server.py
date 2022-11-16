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
    datetime = []
    offset = []

    db = pymysql.connect(host='',
                         user='',
                         password='',
                         db='',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)

    # database 사용하기 위한 cursor 세팅
    cursor = db.cursor()

    select1 = """SELECT * FROM node1"""
    select2 = """SELECT * FROM node2"""
    select3 = """SELECT * FROM node3"""
    selecttemp = """SELECT * FROM temp"""

    # Sql query실행
    cursor.execute(selecttemp)

    # 실행결과 가져오기
    result = cursor.fetchall()

    db.close()

    for i in result:
        datetime.append(i['datetime'])
        offset.append(i['offset'])
        # a=i
         # dt.append(result[i]['datetime'])
         # offset.append(result[i]['offset'])
    # a=result[0]['datetime']
    # b=result[1]['offset']
    # c=result[0]['offset']

    return f'''<!doctype html>
        <html>
            <body>
                {datetime,offset}
            </body>
        </html>
        '''
app.run(debug=True)
