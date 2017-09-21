# !/usr/lib/anaconda2
# coding:utf-8
# Created by Cooper on 1/7/17.
import requests,shutil,random
from time import sleep
headers = {
    "Host":"uac.10010.com",
    "Connection":"keep-alive",
    "Cache-Control":"max-age=0",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Cookie":"gipgeo=11|110; mallcity=11|110; WT_FPC=id=28e2332935374e276721488805979950:lv=1488805979954:ss=1488805979950; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1488805980; _n3fa_cid=8d29960504454bee9c27e915aa36ed39; _n3fa_ext=ft=1488805977; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1488805977; uacverifykey=kih458d4aab44f72d602783245189bfddd0wxy",
}


i = 830
while i< 1000:
    i+=1
    # break
    sleep(random.random()*5)
    url = "https://uac.10010.com/portal/Service/CreateImage?t=1488805999138"
    r = requests.get(url,stream=True,headers = headers)
    if r.status_code == 200 :
        with open("./imgs/"+str(i)+".png",'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw,f)
    if i % 10 ==0:
        print(i, "..")
print("done..")
