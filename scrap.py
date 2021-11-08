#importing the BeautifulSoup Library  
  
from bs4 import BeautifulSoup   

soup = BeautifulSoup("<b class = \"boldest\">Extremely bold</b>", features="html5lib")  
tag = soup.b  
print(type(tag))
print(tag.name)
print(tag['class'])

class_is_multi= { '*' : 'class'}  
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)  
print(xml_soup.p['class'])
print(tag.string)
# [u'body', u'strikeout']  