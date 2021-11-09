from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1',user='root', passwd = None, db = 'mysql',
charset = 'utf8')
cur = conn.cursor()
cur.execute("USE scrap")
random.seed(datetime.datetime.now())
def store(title, content):
   cur.execute('INSERT INTO scrap_pages (title, content) VALUES ''("%s","%s")', (title, content))
   cur.connection.commit()

# def getLinks(articleUrl):
#    html = urlopen('https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_data_processing.htm'+articleUrl)
#    bs = BeautifulSoup(html, 'html.parser')
#    title = bs.find('h1').get_text()
#    content = bs.find('div', {'id':'mw-content-text'}).find('p').get_text()
#    store(title, content)
#    return bs.find('div', {'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))
# links = getLinks('/wiki/Kevin_Bacon')
links = [{ 'title': 'jupiter', 'content': 'content-1' }, { 'title': 'jupiter', 'content': 'content-2' }]

try:
    for link in links:
        store(link['title'], link['content'])
        # links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()