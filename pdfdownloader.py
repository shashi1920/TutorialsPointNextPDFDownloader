__author__ = 'Shashi'
import requests
import bs4
import urllib
import time
import os
import wget


def pdfdownloader(url,start,seen):
    if url in seen:
            return 1
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

    response = requests.get(url,headers=header)

    #print response.text
    download=False
    next=False
    soup = bs4.BeautifulSoup(response.text)
    if soup.findAll("div", { "class" : "pdf-btn" }):
        for div in soup.findAll("div", { "class" : "pdf-btn" }):
            div.a["href"].split('/')[-1]=wget.download("http://www.tutorialspoint.com" +div.a["href"])
            print("Saved: "+div.a["href"].split('/')[-1])
    else:
        url.split('/')[-1]=wget.download(url)
    for div in soup.findAll("div", { "class" : "nxt-btn" })[:1]:
        print "Working on : " + "http://www.tutorialspoint.com"+div.a["href"]
        seen.append(url)
        pdfdownloader("http://www.tutorialspoint.com" +div.a["href"],start,seen)
    return 1





start=raw_input("Enter the starting URL for the tutorial: ") #Enter the url of starting tutorial
DIR=' '.join(start.split('/')[3:])
if not os.path.exists(DIR):
    os.makedirs(DIR)
seen=[]

os.chdir(DIR)
pdfdownloader(start,start,seen)
print "Successfully Downloaded "+str(len(seen))+" files"