import requests
from bs4 import BeautifulSoup
import csv

def get_page(purchase_url):
    proxies = {'http': 'http://127.0.0.1:9292', 'https': 'http://127.0.0.1:9292'}     #代理设置
    session=requests.session()                                                                                 #创建session跟踪cookie
    post_url='http://almvdkg6vrpmkvk4.onion/ucp.php?mode=login'             #提交表单的url，目标网站关键参数之一
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
           'Origin': "http://almvdkg6vrpmkvk4.onion",
           'Referer': "http://almvdkg6vrpmkvk4.onion/ucp.php?mode=login&sid=a3772e5d620f399554aa20fa40d652a5",
           'Host':"almvdkg6vrpmkvk4.onion",
    }                                   #制作headers
    index_url='http://almvdkg6vrpmkvk4.onion/index.php'        #主页地址，为获取sid
    index_text=session.get(index_url,headers=headers,proxies=proxies)     #获取页面
    index_soup=BeautifulSoup(index_text.text,"lxml")                              #
    redirext_t=index_soup.select('input[name=redirect]')[0]
    redir_value=str(redirext_t.get('value'))
    redir_value=str(redir_value.split('sid=')[1])                                  #获取sid值
    print('sid='+redir_value+'\n')
    postdata={
        'mode':'login',
        'username':"wiki1221",
        'password':"Qwer0016",
        'login':"登录",
        'redirect':"./ucp.php?mode=login",
        'sid':redir_value,           
    }                                                                            #制作登陆用的post表单数据，即用户名、密码
    host_1 = session.post(post_url, data=postdata,headers=headers,proxies = proxies)    #获取登录后的页面
    print('首页页面状态：')
    print(host_1.status_code)
#host_soup=BeautifulSoup(host_1.text,"lxml")                            #备用，主页解析
    purchase_1=session.get(purchase_url,headers=headers,proxies=proxies)             #进入购买分区（可以更换为讨论分区、闲话分区）页面
    print('\n购买区页面状态：')
    print(purchase_1.status_code)
    topicp_soup=BeautifulSoup(purchase_1.text,"lxml")                            #（获取改页面信息）
    return topicp_soup

def get_data(post_list):                                                                            #购买分区页面解析
    data_list = []
    for post in post_list:
        title_td=post.find('div',class_='list-inner')
        title=title_td.find('a',class_='topictitle').text.strip()    #标题
        post_link=title_td.find('a',class_='topictitle')['href']
        post_link='http://almvdkg6vrpmkvk4.onion'+post_link         #文章链接
        author=title_td.find('div',class_='topic-poster responsive-hide left-box').span.text.strip()   #作者
        c_reply=post.find('dd',class_='posts').text.strip()   #回复次数
        c_view=post.find('dd',class_='views').text.strip()    #阅读次数
        last_username= post.find('dd', class_='lastpost').span.text.strip()   #最后回复者
        data_list.append([title,post_link,author,c_reply
                          ,c_view,last_username,])

    return data_list

purchase_url='http://almvdkg6vrpmkvk4.onion/viewforum.php?f=37'
ptopic_soup=get_page(purchase_url)                    #获取第一页
ptopic_ul=ptopic_soup.find('ul', class_='topiclist topics')
topic_list = ptopic_ul.find_all('li')
date_list_1=get_data(topic_list)

for i in range(1,3):                                                   #后续3页
    purchase_url='http://almvdkg6vrpmkvk4.onion/viewforum.php?f=37&start=30'+str(i*30)
    ptopic_soup = get_page(purchase_url)  # 获取第2-4页
    ptopic_ul=ptopic_soup.find('ul', class_='topiclist topics')
    topic_list = ptopic_ul.find_all('li')
    date_list_2=get_data(topic_list)
    date_list_1=date_list_1+date_list_2


name=['标题','链接','作者','回复总数','阅读总数','最新','时间']

with open('purchase.csv', "a+", encoding='utf-8') as csvfile:          # 输出到CSV
    writer = csv.writer(csvfile)
    # 先写入columns_name
    writer.writerow(name)
    # 写入多行用writerows
    writer.writerows(date_list_1)
    csvfile.close()








