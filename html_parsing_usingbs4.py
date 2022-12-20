import codecs
from bs4 import BeautifulSoup
f=codecs.open("TweetDeck.html",'rb')
soup = BeautifulSoup(f.read(),features="lxml")
# print(len(soup.find_all("article",{"data-key":"1602303333766676483"})))
# #print(soup.prettify())

# articles_list = soup.find_all("article")
# twitter_header_list=soup.find_all(class_="tweet-header")
# #print(twitter_header_list[0].parent.parent.parent["data-key"]) #article mapping
# #print(len(twitter_header_list[0].contents))

# #print(dir(twitter_header_list[0]),type(twitter_header_list[0]))

# print(twitter_header_list[0].findChild("a")['href']) #twitter user link
# print(twitter_header_list[0].findChild("a").find(class_="fullname").text) #user name of the tweet
# print(twitter_header_list[0].find(class_="account-link").find(class_="username").text) #twitter user handle 
# #instead of findchild['a'] we can do .find(class_="account-link")

# print(twitter_header_list[0].findChild("time").findChild("a")['href']) #twitter link
# print(type(twitter_header_list[0]))

# soup.findAll()

#print(soup.prettify())
dict1={"data-column":"c1670853912807s50"}
print(soup.find("section",dict1).find("article"))
#print(soup.find("article"))