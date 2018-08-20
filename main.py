import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    res = requests.get(url, headers=headers).text
    return res


def all_page():
    base_url = 'https://book.douban.com/top250?start='
    urls = [base_url + str(page) for page in range(0, 250, 25)]
    return urls


def html_parse():
    urls = all_page()
    for url in urls:
        soup = BeautifulSoup(get_html(url), 'lxml')
        alldiv = soup.find_all('div', class_='pl2')
        names = [a.find('a')['title'] for a in alldiv]
        allp = soup.find_all('p', class_='pl')
        authors = [p.get_text() for p in allp]
        allspan = soup.find_all('span', class_='rating_nums')
        grades = [span.get_text() for span in allspan]
        allinq = soup.find_all('span', class_='inq')
        comments = [inq.get_text() for inq in allinq]
        for name, author, grade, comment in zip(names, authors, grades, comments):
            name = '书名：' + name + '\n'
            author = '作者：' + author + '\n'
            grade = '评分：' + grade + '\n'
            comment = '简介：' + comment + '\n'
            data = name + author + grade + comment
            f.write(data + '=======================================================================' + '\n')


f = open('豆瓣TOP250.txt', 'w', encoding='utf-8')
html_parse()
f.close()
print('DONE!!!')
