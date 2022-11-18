from flask import Flask, request, redirect, render_template
import pymysql

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

@app.route('/')
def index():
    # nodelist=[]
    # db = pymysql.connect(host='',
    #                      user='',
    #                      password='',
    #                      db='',
    #                      charset='utf8',
    #                      cursorclass=pymysql.cursors.DictCursor)
    #
    # # database 사용하기 위한 cursor 세팅
    # cursor = db.cursor()
    #
    # selectnodelist="""select * from nodelist """
    #
    # # Sql query실행
    # cursor.execute(selectnodelist)
    #
    # # 실행결과 가져오기
    # result = cursor.fetchall()
    #
    # db.close()
    # print(result)
    return render_template('main.html', nodelist=getlist())
global date
date=''
@app.route('/show/', methods=['POST'])
def show():
    global date
    data = request.values
    date=data['date']
    return render_template('main.html', nodelist=getlist())

@app.route('/<int:id>/')
def update(id):
    global date
    datetime=[]
    offset=[]

    db = pymysql.connect(host='',
                         user='',
                         password='',
                         db='',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)

    # database 사용하기 위한 cursor 세팅
    cursor = db.cursor()

    select = f"""SELECT * FROM node{id}"""
    selecttemp="""SELECT * FROM temp"""

    # Sql query실행
    cursor.execute(selecttemp)

    # 실행결과 가져오기
    result = cursor.fetchall()

    db.close()

    for i in result:
        datetime.append(i['datetime'])
        offset.append(i['offset'])

    return render_template('main.html', nodelist=getlist(), id=id, datetime=datetime, offset=offset)

app.run(debug=True)


