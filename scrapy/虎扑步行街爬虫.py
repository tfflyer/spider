import requests
from bs4 import BeautifulSoup
import datetime

def get_page(link):  

    headers = {
        "User-Agent": 'Mozilla/5.0(Windows;U;Windows NT 6.1;Win64;x64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        # host
    }  # 定义爬虫请求头
    r = requests.get(link, headers=headers, timeout=20)
    html = r.content
    html = html.decode('UTF-8')
    soup = BeautifulSoup(html, "lxml")
    return soup

def get_data(post_list):
    data_list = []
    for post in post_list:
        title_td=post.find('div',class_='titlelink box')
        title=title_td.find('a',class_='truetit').text.strip()
        post_link=title_td.find('a',class_='truetit')['href']
        post_link='https://bbs.hupu.com'+post_link

        author=post.find('div',class_='author box').a.text.strip()
        author_page=post.find('div',class_='author box').a['href']


        reply_view=post.find('span',class_='ansour box').text.strip()
        reply=reply_view.split('/')[0].strip()
        view=reply_view.split('/')[1].strip()


        last_reply=post.find('span',class_='endauthor').text.strip()

        data_list.append([title,post_link,author,author_page,reply
                          ,view,last_reply,])

    return data_list

link="https://bbs.hupu.com/bxj"
soup=get_page(link)
link_list=soup.find('ul',class_='for-list')
post_list=link_list.find_all('li')
data_list=get_data(post_list)


with open('bxj.txt',"a+",encoding='utf-8')  as f:                       #输出到txt文件
    f.write(str(data_list))
    f.close()
	print('已输出到文件')

for each in data_list:
    print(data_list)
	


