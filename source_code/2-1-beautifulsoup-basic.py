#引入xml 解析器，beautifulSoup is a library for pulling data out of HTML and XML files.
#It works with your favorite parset to provide idiomatic(惯用) ways of navigating(导航),searching,and
#modifying the parse tree. 
from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
print('\n', soup.p)

all_href = soup.find_all('a')

#机器学习中的语句，一般不这么用
#语句featList = [example[i] for example in dataSet]作用为： 
#将dataSet中的数据按行依次放入example中，然后取得example中的example[i]元素，放入列表featList中
all_href = [l['href'] for l in all_href]
print('\n', all_href)


