from flask import Flask, request, redirect, render_template
import pymysql
from datetime import datetime
from datetime import date, timedelta
import time

app = Flask(__name__)

datetime= []
offset = []

def getlist(): # nodelist 가져오기
    db = pymysql.connect(host='',
                         user='',
                         password='',
                         db='',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)

    # database 사용하기 위한 cursor 세팅
    cursor = db.cursor()

    selectnodelist = """select * from nodelist """

    # Sql query실행
    cursor.execute(selectnodelist)

    # 실행결과 가져오기
    result = cursor.fetchall()

    db.close()
    return result

def getdata(id, date): #날짜와 offset값 가져오기
    db = pymysql.connect(host='',
                         user='',
                         password='',
                         db='',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)

    # database 사용하기 위한 cursor 세팅
    cursor = db.cursor()

    select = f"""SELECT * FROM node WHERE id={id} and DATE(datetime)='{date}'"""

    # Sql query실행
    cursor.execute(select)

    # 실행결과 가져오기
    result = cursor.fetchall()

    db.close()
    return result

@app.route('/') # 첫화면, set (yesterday날짜, node1)
def index():
    t = time.time() - 60*60*24
    yesterday = time.strftime("%Y-%m-%d", time.gmtime(t))

    datetime = []
    offset = []

    result = getdata(1,yesterday)

    for i in result:
        datetime.append(i['datetime'])
        offset.append(i['offset'])

    return render_template('main.html', nodelist=getlist(), id=1, datetime=datetime, offset=offset, gdate=yesterday)

global date
date=''
@app.route('/show/', methods=['POST']) # showchart버튼 눌렸을 때
def show():
    global date
    data = request.values
    date=data['date']
    url = '/' + data['nodeid'] + '/'
    return redirect(url) # date는 전역변수에 저장, node번호로 이동

@app.route('/<int:id>/') # show에서 호출, graph 정보 주기
def update(id):
    global date
    datetime=[]
    offset=[]

    result = getdata(id, date)

    for i in result: # datetime(x축)과 offset(y축)값 return 하기 위함
        datetime.append(i['datetime'])
        offset.append(i['offset'])

    return render_template('main.html', nodelist=getlist(), id=id, datetime=datetime, offset=offset, gdate=date)

app.run()


