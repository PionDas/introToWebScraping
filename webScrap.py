#Purpose: to collect data from a website
#idea: use image recognition for parsing instead of html
# tuturial: https://www.youtube.com/watch?v=XQgXKtPSzUI&t=24s
# stoped @: 22:10

#object name is 'eReq' which calls a method 'urlopen' from module called 'request' from a package called 'urllib'
from urllib.request import urlopen as eReq
# object name soup calls the function 'BeautifulSoup' from the package bs4
from bs4 import BeautifulSoup as soup


#name of url
my_url = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card'

# making a connection (grabing a webpage and downloading it literarly)
uClient = eReq(my_url)

#reading the file(webpage) into a varible
page_html = uClient.read()

#closing the webpage
uClient.close()

# (what to parse, how to parse it)      (how to parse) can be an xnl file, html file or etc
page_soup = soup(page_html, "html.parser") # html parsing

#grabing to header of the file
#print(page_soup.h1)

# find all 'div' from the html file that has a "class" called "item-container" and store in variable "containers"
#grabing all the graphic cards and putting them in a variable
containers = page_soup.findAll("div", {"class":"item-container"})

# finding length of containers (how many items does it have)
#print(len(containers))

# use the following to get the information of the html code of that spesific item
# use the information to details like name, price, rating etc
#print(containers[0])


container = containers[0]
#looking into the html file and traversing to find text of img which is the brand name
# the img in the html file consists of keys. thus the key is "title" which provides the text
print(container.div.div.img["title"])


#creating csv file
filename = "product.csv"
#"w" is for writing to the file
f = open(filename, "w")

#commas are used to create columns in the csv file
headers = "brand, product_name, shipping\n"
f.write(headers)

#looping through each item to get the title
for container in containers:
    brand = container.div.div.img["title"]
    shipping = container.findAll("li", {"class": "price-ship"})

    print("Brand: "+ brand)
    print("Shipping: "+shipping[0].text.strip())

    #comments are used to create columns in the csv file
    f.write(str(brand) + "," + str(shipping) + "\n")

    #if the text in brand or shipping has commas then use the following to avoid making extra columns
    # ex.   brand.replace("," , "|")
    # commas are raplcedd by a line
f.close()

#use string to ommit any unucessary text from the defult html text output
#shipping_container[0].text.strip()

#modelNum_container = container.findAll("ul", {"class":"item-features"})
#modelNum_container = modelNum_container.findAll("li", {"class":""})
