import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import csv
import os
# import pandas as pd

# function to scrape each url
def scrape_pp(url):
    """function takes in a full url and returns the title, date, author, ls, topic_ls
    if found. Else will return part of it with try and except statements"""
    space = ' '
    try:
        page =urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features="html.parser")
    except urllib.error.HTTPError:     #raise request error
        # pass
        return (url, space,space, space, space, space) #return empty string 
    try:
        title = soup.find('title').string 
    except TypeError:  #if type error return url 
        title = space
        # return (url, space, space, space, space, space)
    try:
        date = soup.find(class_ = "post-date").string
        date = date.replace(',', '')
    except TypeError:  #if type error retrun title only
        date = space
        # return(url, title, space, space, space, space)
    try:
        author = soup.find(class_ = "vcard author").string 
    except AttributeError: #if attribute error return title and date
        author = space
        # return(url, title, date, space, space,space)
    try:
        video = soup.find('video').get('src')
        has_video = 'True'
    except AttributeError:
        has_video = 'False'
    article_tags = soup.find("div", {"class":"tagcloud single-tags meta-container"})  #returns the html in this div and class, filled with all the tagnames
    ls = [] #create new list to store all article tags
    try:
        for tags in article_tags:
            full_tags = tags.string.split('/') #split the html tag
            if full_tags[0] == 'Tags' or full_tags[0] == ' ':  #pass if element contains 'Tags' or ' '
                pass
            else:
                ls.append(full_tags[0]) #add to the list if element contains an actual tag
    except TypeError:
        pass
    topics = soup.find(class_ = "post-cat").text
    topics_ls = topics.split(',')
    return (url, title, date, author, has_video, ls, topics_ls)

    
# open the list of url and scrape each url
with open("full_url_revised.csv", 'r') as in_file:
    all_url = [] #create empty list to store returned tuples from each url
    for line in in_file:
        line = line.strip('\n').split(',')
        for url in line:
            if url == '':
                pass
            else:
                details = scrape_pp(url)
                all_url.append(details)


with open("scraped_data5.csv", 'w') as outfile:
    # writer = csv.writer(outfile, delimiter = '=', lineterminator='\n')
    for i in range(len(all_url)):
        data = '' #create a data string to capture data scraped from EACH url
        for n in range(len(all_url[i])):
            if n <= 4: #all elements including title, date and author (single items)
                data += all_url[i][n] + ',' 
            elif n in (5,6): #for elements in position 4 or 5
                tags = '' #empty string to concat tags or topics
                for e in range(len(all_url[i][n])):
                    tags += all_url[i][n][e] + '|'   #delimit each tag or topic with a '|'
                data += tags + ','     #add the tags or topic to the comma seperated values 
        # writer.writerow(data)
        outfile.write(data + '\n')  #write to the file and jump to the next row



                

