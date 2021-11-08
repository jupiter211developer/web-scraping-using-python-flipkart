from bs4 import BeautifulSoup   

doc=BeautifulSoup("<document><content/>INSERT FOOTER HERE</document>","xml")  
footer=BeautifulSoup("<footer>Here's the footer</footer>","xml")  
doc.find(text="INSERT FOOTER HERE").replace_with(footer)  
print(doc)  