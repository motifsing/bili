from selenium import webdriver
import requests
import JSONParser
import time
def login(r):
    '登录至B站'
    driver=webdriver.Chrome()
    driver.get('https://passport.bilibili.com/ajax/miniLogin/minilogin')
    aa=True
    while aa :
        time.sleep(1)
        if driver.current_url=='https://passport.bilibili.com/ajax/miniLogin/redirect' :
            aa=False
    sa=[]
    for i in driver.get_cookies() :
        r.cookies.set(i['name'],i['value'],domain=i['domain'],path=i['path'])
        t={'name':i['name'],'value':i['value'],'domain':i['domain'],'path':i['path']}
        sa.append(t)
    driver.close()
    rr=tryok(r)
    if rr==True :
        print('登录成功')
        JSONParser.savecookie(sa)
        return 0
    elif rr==False :
        print('网络错误')
        return 1
    else :
        print("登录失败："+str(rr['code'])+","+str(rr['message']))
        return 2
def tryok(r) :
    '验证是否登录成功'
    try :
        re=r.get('https://api.bilibili.com/x/web-interface/nav')
    except :
        return False
    re.encoding='utf8'
    try :
        obj=re.json()
        if obj['code']==0:
            return True
        return False
    except :
        return re.text