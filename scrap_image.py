import requests

url = 'https://www.tutorialspoint.com/python_web_scraping/images/logo.png'
r = requests.get(url)

with open('logo.png', 'wb') as f:
    f.write(r.content)

print('write successfully')