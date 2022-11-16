from flask import Flask, request, redirect, render_template
import pymysql

app = Flask(__name__)

datetime= []
offset = []

@app.route('/')
def index():
    return render_template('main.html')

# @app.route('/node/<int:id>/', methods=['GET', 'POST'])
# def update(id):
#     if request.method =='GET':
#         datetime=''
#         offset=''
#
#         db = pymysql.connect(host='',
#                              user='',
#                              password='',
#                              db='',
#                              charset='utf8',
#                              cursorclass=pymysql.cursors.DictCursor)
#
#         # database 사용하기 위한 cursor 세팅
#         cursor = db.cursor()
#
#         select1 = """SELECT * FROM node1"""
#         select2 = """SELECT * FROM node2"""
#         select3 = """SELECT * FROM node3"""
#         selecttemp = """SELECT * FROM temp"""
#
#         # Sql query실행
#         cursor.execute(selecttemp)
#
#         # 실행결과 가져오기
#         result = cursor.fetchall()
#
#         db.close()
#
#         for i in result:
#             datetime.append(result[i]['datetime'])
#             offset.append(result[i]['offset'])
#
#
#         content = f'''
#             <form action="/update/{id}" method="POST">
#                 <p><input type="text" name ="title" placeholder="title" value="{title}"></p>
#                 <p><textarea name="body" placeholder="body">{body}</textarea></p>
#                 <p><input type="submit" value="update"></p>
#             </form>
#             '''
#         return template(getContents(), content)
#     elif request.method =='POST':
#         global nextId
#         title = request.form['title']
#         body = request.form ['body']
#         for topic in topics:
#             if id == topic['id']:
#                 topic['title']=title
#                 topic['body']=body
#                 break
#         url = '/read/'+str(id)+'/'
#         return redirect(url)

app.run(debug=True)


