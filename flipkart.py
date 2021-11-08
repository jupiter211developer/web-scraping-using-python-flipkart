from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"  

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, features="html.parser")

containers = page_soup.find_all("div", { "class": "_13oc-S" })

# container = containers[0]

# print(soup.prettify(container))

# price = container.find_all("div", { "class": "nlI3QM" })
# print(price[0].text)
# ratings = page_soup.find_all("div", { "class": "_3LWZlK" })
# print(ratings[0].text)

filename = "product1.csv"
f = open(filename, "w")
headers = "Product_Name,Pricing,Ratings\n"  
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.find_all("div", {"class": "nlI3QM" })
    price = price_container[0].text.strip()
    rating_container = container.find_all("div", {"class": "_3LWZlK"})
    ratings = rating_container[0].text

    # print("product_name:"+product_name)  
    # print("price:"+price)  
    # print("ratings:"+ str(ratings))  
    edit_price = ''.join(price.split(','))
    # split_price = add_rs_price.split("E")  
    final_price = edit_price.split('₹')[1]

    split_rating = str(ratings).split(" ")  
    final_rating = split_rating[0]  

    print(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
    f.write(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
  
f.close()