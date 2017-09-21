# !/usr/lib/anaconda2
# coding:utf-8
# Created by Cooper on 1/7/17.
import requests,shutil

i = 0
while i< 100:
    i+=1
    # break
    url = "http://www.bjgjj.gov.cn/wsyw/servlet/PicCheckCode1"
    r = requests.get(url,stream=True)
    if r.status_code == 200 :
        with open("./imgs/"+str(i)+".gif",'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw,f)
    if i % 100 ==0:
        print(i, "..")
print("done..")
