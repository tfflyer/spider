import requests
from bs4 import BeautifulSoup
import csv

proxies = {'http': 'http://127.0.0.1:9292', 'https': 'http://127.0.0.1:9292'}  # 代理
session = requests.session()
post_url = 'http://almvdkg6vrpmkvk4.onion/ucp.php?mode=login'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
           'Origin': "http://almvdkg6vrpmkvk4.onion",
           'Referer': "http://almvdkg6vrpmkvk4.onion/ucp.php?mode=login&sid=a3772e5d620f399554aa20fa40d652a5",
           'Host': "almvdkg6vrpmkvk4.onion",
           }
index_url = 'http://almvdkg6vrpmkvk4.onion/index.php'
index_text = session.get(index_url, headers=headers, proxies=proxies)
index_soup = BeautifulSoup(index_text.text, "lxml")
redirext_t = index_soup.select('input[name=redirect]')[0]
redir_value = str(redirext_t.get('value'))
redir_value = str(redir_value.split('sid=')[1])
print('sid=' + redir_value + '\n')
postdata = {
    'mode': 'login',
    'username': "wiki1221",
    'password': "Qwer0016",
    'login': "登录",
    'redirect': "./ucp.php?mode=login",
    'sid': redir_value,
}
host_1 = session.post(post_url, data=postdata, headers=headers, proxies=proxies)  # 获取页面
print('首页页面状态：')
print(host_1.status_code)


def get_page(purchase_url):

#host_soup=BeautifulSoup(host_1.text,"lxml")
    purchase_1=session.get(purchase_url,headers=headers,proxies=proxies)
    print('\n讨论区页面状态：')
    print(purchase_1.status_code)
    topicp_soup=BeautifulSoup(purchase_1.text,"lxml")
    return topicp_soup

def get_data(post_list):        #需要改解析
    data_list = []
    for post in post_list:
        #print(post)
        title_td=post.find('div',class_='list-inner')
        title=post.find('a',class_='topictitle').text.strip()
        post_link=title_td.find('a',class_='topictitle')['href']
        post_link='http://almvdkg6vrpmkvk4.onion'+post_link         #文章链接
        author=title_td.find('div',class_='topic-poster responsive-hide left-box').span.text.strip()   #作者
        c_reply=post.find('dd',class_='posts').text.strip()   #回复次数
        c_view=post.find('dd',class_='views').text.strip()    #阅读次数
        last_username= post.find('dd', class_='lastpost').span.text.strip()   #最后回复者
        data_list.append([title,post_link,author,c_reply
                          ,c_view,last_username,])

    return data_list

purchase_url='http://almvdkg6vrpmkvk4.onion/viewforum.php?f=8'    #f后面的参数代表着不同的页面。
ptopic_soup=get_page(purchase_url)    #获取第一页
ptopic_ul=ptopic_soup.find('ul', class_='topiclist topics')
topic_list_st=ptopic_ul.find_all('li',class_='row bg1 sticky')
topic_list1 = ptopic_ul.find_all('li',class_='row bg1')
topic_list2 = ptopic_ul.find_all('li',class_='row bg2')
topic_list=topic_list_st+topic_list1+topic_list2

date_list_1=get_data(topic_list)

for i in range(1,17):                 #后续17页
    purchase_url='http://almvdkg6vrpmkvk4.onion/viewforum.php?f=8&start='+str(i*30)
    ptopic_soup = get_page(purchase_url)  # 获取第2-17页
    ptopic_ul=ptopic_soup.find('ul', class_='topiclist topics')
    topic_list1 = ptopic_ul.find_all('li', class_='row bg1')
    topic_list2 = ptopic_ul.find_all('li', class_='row bg2')
    topic_list = topic_list1 + topic_list2
    date_list_2=get_data(topic_list)
    date_list_1=date_list_1+date_list_2


name=['标题','链接','作者','回复总数','阅读总数','最新','时间']

with open('chat.csv', "a+", encoding='utf-8') as csvfile:  # 输出到CSV
    writer = csv.writer(csvfile)

    writer.writerow(name)

    writer.writerows(date_list_1)
    csvfile.close()










