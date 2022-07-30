#project 
#part 1:Extract the price of the phone
#part 2:If the proice is low at a point,send a message to me

#part1:
#web scrapping
import requests
url="https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Description=samsung%20galaxy%20z%20flip%203%20unlocked&cm_re=samsung_galaxy%20z%20flip%203%20unlocked-_-75-168-090-_-Product&quicklink=true"
page=requests.get(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,"html.parser")
price=soup.find_all('div',attrs={"class":"price-current"})[0].get_text()
