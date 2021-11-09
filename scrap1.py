import builtwith
# import whois

print(builtwith.parse("https://www.microsoft.com/"))
# print (whois.whois("https://www.microsoft.com/"))
# print (whois.whois("upwork.com"))

import re
import urllib.request
response = urllib.request.urlopen('https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_data_extraction.htm')
html = response.read()
text = html.decode()
re.findall('<td class="w2p_fw">(.*?)</td>',text)
# print(text)