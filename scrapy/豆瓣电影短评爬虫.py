import requests
from bs4 import BeautifulSoup
def get_comments(url_comments):                                  #定义评论爬取函数

    headers ={
    "User-Agent":'Mozilla/5.0(Windows;U;Windows NT 6.1;Win64;x64) AppleWebKit\
	/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
     'Host':'book.douban.com'
    }                                             #定义爬虫请求头
    comments_list=[]                                 #定义存储评论的列表
    for i in range(0,5):
        link=url_comments+str(i)   #换页
        r=requests.get(link,headers= headers,timeout=20)
        print (str(1),"页响应状态码：",r.status_code)
        soup=BeautifulSoup(r.text,"lxml")                   #利用beautifulsoup进行页面解析
        div_list =soup.find_all('div',class_='comment')       #获取类型为comment标签为div后的文本
        for  each in div_list:
            comment=each.p.text.strip()
            comments_list.append(comment)
    return comments_list


host_l=input('please paste the urls and ended at \'start=\'')      #输入短评链接
comments=get_comments(host_l)
with open('comments.txt',"a+",encoding='utf-8')  as f:                       #输出到txt文件
    f.write(str(comments))
    f.close()
print(comments)