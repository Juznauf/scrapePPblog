# import requests
import urllib.request
from bs4 import BeautifulSoup
import csv
import os


# scrape the article name, article date, article tags, author

# the article tage is  <h1 class="article-title">Thinking Out of the Subscription Box</h1> text

# the article date is <span class="post-date">October 8, 2019</span>

# the article tags are <h6 class="tags-title meta-title">Tags</h6>
# <div class="tagcloud single-tags meta-container"><h6 class="tags-title meta-title">Tags</h6> <a href="https://www.parcelmonitor.com/blog/tag/blue-apron/" rel="tag">Blue Apron</a><a href="https://www.parcelmonitor.com/blog/tag/customer-service/" rel="tag">Customer Service</a><a href="https://www.parcelmonitor.com/blog/tag/dollar-shave-club/" rel="tag">Dollar Shave Club</a><a href="https://www.parcelmonitor.com/blog/tag/rent-the-runway/" rel="tag">Rent The Runway</a><a href="https://www.parcelmonitor.com/blog/tag/supply-chain/" rel="tag">Supply Chain</a></div>

# the author is <a href="https://www.parcelmonitor.com/blog/author/jiaxin/" class="vcard author" rel="author" itemprop="url"><span class="fn" itemprop="name">Jia Xin</span></a>

# test for one url first 

# page =requests.get("https://www.parcelmonitor.com/blog/lessons-from-subscription-services/")

page =urllib.request.urlopen("https://www.parcelmonitor.com/blog/lessons-from-subscription-services/")
soup = BeautifulSoup(page, features="html.parser")
# print(soup.prettify())

# print(soup.title.string())
# soup.title.string()

# soup.title.string()
# find title
title = soup.find('title')
print(title.string)
# find date
date = soup.find(class_ = "post-date").string
print(date)
# find article tags
# article_tags = soup.find_all(class_="tagcloud single-tags meta-container")
# print(article_tags)
article_tags = soup.find("div", {"class":"tagcloud single-tags meta-container"})
print(article_tags)
ls = [] 
for tags in article_tags:
    full_tags = tags.string.split('/')
    if full_tags[0] == 'Tags' or full_tags[0] == ' ':
        pass
    else:
        ls.append(full_tags[0])
    # print(type(tags))
    # print(full_tags)
print(ls)
author = soup.find(class_ = "vcard author").string
print(author)

# find the article topics

topics = soup.find(class_ = "post-cat").text
print(topics)
topics_ls = topics.split(',')
print(topics_ls)


# to check if the webpages has a video embedded

try:
    video = soup.find('video').get('src')
    has_video = True
except AttributeError:
    has_video = False
print(has_video)


