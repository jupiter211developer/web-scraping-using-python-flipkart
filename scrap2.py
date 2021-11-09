import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.freelancer.com/projects/javascript/ReactJS-expert-for-API-integration/details')
soup = BeautifulSoup(r.text, 'lxml')

f = csv.writer(open('dataprocess.csv', 'w'))
f.writerow(['Title'])
f.writerow([soup.title.text])

import json
r = requests.get('https://www.freelancer.com/projects/javascript/ReactJS-expert-for-API-integration/details')
soup = BeautifulSoup(r.text, 'lxml')
y = json.dumps(soup.title.text)
with open('JSONFile.json', 'wt') as outfile:
   json.dump(y, outfile)