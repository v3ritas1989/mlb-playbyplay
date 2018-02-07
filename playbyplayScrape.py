from urllib import *
from bs4 import Comment
import urllib.request
import ssl
import bs4 as bs
import os
import re
import csv

ssl._create_default_https_context = ssl._create_unverified_context
######################
##   Variables  #
######################
filename = 'playbyplay.csv'
site='https://www.baseball-reference.com/boxes/LAN/LAN201711010.shtml'

params = ''
## Find your proxy here https://free-proxy-list.net/
proxy = {'http' : 'http://94.130.14.146:31288' }
hdr = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
       ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
       ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
       ('Accept-Encoding', 'none'),
       ('Accept-Language', 'en-US,en;q=0.8'),
       ('Connection', 'keep-alive')]
##################################################################################################
## Test basic variables IP, header (disabled cause to many request will ban you from this test)  #
##################################################################################################
  ##print('Actual IP', urllib.request.urlopen('http://httpbin.org/ip').read())
  ##print('Actual header',urllib.request.urlopen(site).read())


def openPage(site,hdr,proxy,params):
##    This function is for accessing and reading the the data from the required webpage
##    while masking its approach with fake IP and fake user-agent
##    After reading the webpage it will get passed to beutifulsoup for further processing
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    opener.addheaders = hdr

    post_args  = urllib.parse.urlencode(params)
    ##print(post_args)
    binary_data = post_args.encode('UTF-8')
    ##print(binary_data)
    req = urllib.request.Request(site)##, binary_data
    ##print(str(req))

    response = opener.open(req).read()
    
##########################################################################################
## Test basic variables IP (disabled cause to many request will ban you from this test)  #
##########################################################################################
    ##print('Fake IP', opener.open('http://httpbin.org/ip').read())
    
    ##print(response)

    soup = bs.BeautifulSoup(response,'lxml')
    ##print(soup)
    print('page',site,' has been red')
    return(soup)

def getPlayByPlayData(soup):
# This function identifies the wanted table within the given and passed webpage from function openPage()
# After identification with beautiful soup, it will loads the table into the multidim. list data[]
    soup = soup.find('div',  id='all_play_by_play')
    soup = bs.BeautifulSoup(soup.find(text=lambda text:isinstance(text, Comment)),'lxml')
    table = soup.find('table', id='play_by_play')
    table_body = table.find('tbody')

    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

#####################################
##    Printing the multdim list     #
#####################################
##    for row in data:
##        for elem in row:
##            print(elem, end=' ')
##        print()
    print('PlaybyPlay data has been saved to variable')
    return(data)

def ExportToCSV(Data):
## This function is for writing the data taken from function getPlayByPlayData() to a file in a local folder.
    with open(filename, 'w') as f:
       writer = csv.writer(f, delimiter=';')
       writer.writerows(data)
    print('PlaybyPlay data variable has been saved to file', filename)

soup = openPage(site,hdr,proxy,params)
data = getPlayByPlayData(soup)
ExportToCSV(data)
