from flask import Flask, request, redirect, render_template
import pymysql
from datetime import datetime
from datetime import date, timedelta
import time

app = Flask(__name__)

datetime= []
offset = []

def getlist():
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

def getdata(id, date):
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

@app.route('/')
def index():
    t = time.time() - 60*60*24
    yesterday = time.strftime("%Y-%m-%d", time.gmtime(t))
    print(yesterday)
    datetime = []
    offset = []

    result = getdata(1,yesterday)

    for i in result:
        datetime.append(i['datetime'])
        offset.append(i['offset'])

    return render_template('main.html', nodelist=getlist(), id=1, datetime=datetime, offset=offset, gdate=yesterday)

global date
date=''
@app.route('/show/', methods=['POST'])
def show():
    global date
    data = request.values
    date=data['date']
    url = '/' + data['nodeid'] + '/'
    return redirect(url)

@app.route('/<int:id>/')
def update(id):
    global date
    datetime=[]
    offset=[]

    result = getdata(id, date)

    for i in result:
        datetime.append(i['datetime'])
        offset.append(i['offset'])

    return render_template('main.html', nodelist=getlist(), id=id, datetime=datetime, offset=offset, gdate=date)

app.run()


