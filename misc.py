from datetime import *
import math
import random,string
import mysql.connector as my
a=my.connect(host='localhost',user='root',database='bloodpoint',password='Aprajit@29')
cur=a.cursor()
import tabulate

def member(field,table):
    cur.execute(f'select {field} from {table}')
    x=tuple()
    for i in cur:
        x+=i
    return x
def curextract(cur):
    y=''
    for i in cur :
        y=i
    for i in y:
        y=i
    return y
def r_string(l):
    x=''
    for i in range(0,l):
        x+=random.choice(string.ascii_lowercase)
    x+='@'
    for i in range(0,l):
        x+=random.choice(string.digits)
    return x
def cdate():
    return datetime.now().strftime("%Y-%m-%d")
def datediff(start,end,value):
    d1=date(int(start[0:4]),int(start[5:7]),int(start[8:]))
    d2=date(int(end[0:4]),int(end[5:7]),int(end[8:]))
    x=0
    if value=='days':
        x=(d2-d1).days
    elif value=='months':
        x=math.ceil((d2-d1).days//30)
    elif value=='years':
        x=math.ceil((d2-d1).days//365)
    return x
