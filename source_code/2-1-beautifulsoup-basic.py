#����xml ��������beautifulSoup is a library for pulling data out of HTML and XML files.
#It works with your favorite parset to provide idiomatic(����) ways of navigating(����),searching,and
#modifying the parse tree. 
from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
print('\n', soup.p)

all_href = soup.find_all('a')

#����ѧϰ�е���䣬һ�㲻��ô��
#���featList = [example[i] for example in dataSet]����Ϊ�� 
#��dataSet�е����ݰ������η���example�У�Ȼ��ȡ��example�е�example[i]Ԫ�أ������б�featList��
all_href = [l['href'] for l in all_href]
print('\n', all_href)


