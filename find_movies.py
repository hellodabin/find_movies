from bs4 import BeautifulSoup
import requests

url = "http://www.dytt8.net/"


# -*- coding:utf8 -*-
class getMovies():
    def __init__(self, url):
        self.url = url

    def getHtml(self):
        res = requests.get(url)
        res.encoding = 'gb2312'  # 解决字符编码的问题
        html = BeautifulSoup(res.text)
        items = html.find_all('div', 'co_content8')
        return items

    def get_head_urls(self):
        items = self.getHtml()
        lists = []  # 原始数据
        head_urls = []  # 所有的链接
        for item in items:
            link = item.find_all('a')
            lists += link
        count = 1
        while count < len(lists):  # 不能大于列表的数目
            a = lists[count]['href']
            head_urls.append(a)  # 把获取到的a标签添加到列表
            count += 2
        return head_urls

    def get_info(self):
        movies = []
        head_urls = self.get_head_urls()
        try:
            for head_url in head_urls:
                url = 'http://www.dytt8.net' + head_url
                res = requests.get(url)
                res.encoding = 'gb2312'
                html = BeautifulSoup(res.text)
                items = html.find(id='Zoom')
                con = items.get_text().split('◎')
                print(con[1] + con[9][:13] + '\n' + ' '.join(con[-1].split())[-88:] + '\n')
        except IndexError as err:
            return None


m = getMovies(url)
m.get_info()
