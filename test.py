#!/usr/bin/python3
from pathlib import Path
import shutil
import os
from time import sleep
import schedule
import time
from datetime import datetime
import pymysql

file = open("./log.txt", "r")
 		      

def readlog(): # parsing offset
    print("It's time") #alarm
    today = datetime.today().strftime("%Y%m%d")
    fname = "./offset/offset"+today+".txt"
    file2 = open(fname, "w")
    logs = file.readlines()
    for i in logs:
        i = i.split() #i[4]=="offset"
        if i[4] == "offset" : file2.write(i[1][1:11]+" "+i[2][0:8]+"	"+i[5]+"\n")
    file2.close()
    

#read offset    
    fname = "./offset/offset"+today+".txt"
    f=open(fname, "r")
    lines = f.readlines()
    f.close()
   
    select = "SELECT * FROM node2"
    insert ="INSERT INTO node2 VALUES(%s, %s)"
    createEvent = """CREATE EVENT """

#connect db
    conn = pymysql.connect(host='',
     		           user='',
 		           password='',
 		           db='',
 		           charset='utf8')

#input db
    cur = conn.cursor()
    for line in lines:
        st=line.split("	")
        cur.execute(insert,(st[0], int(st[1][0:-1])))
    conn.commit()
    result = cur.fetchall()
    conn.close()
    for data in result:
        print(data)   

           
    f.close()
    print("It's dbtime") #alarm
 

schedule.every().day.at('00:00').do(readlog) # run cycle settings
					     # run a function every midnight
#schedule.every(1).minute.do(readlog)

while True:
    schedule.run_pending()
    time.sleep(1)
    

file.close()
