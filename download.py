#!/usr/bin/env python

import sys
import re
import urllib2
from BeautifulSoup import BeautifulSoup

def main():
    html_file = open("music.html", "r")
    soup = BeautifulSoup(html_file)
    div_list = soup.find('div', {'id': 'audios_list'})
    items = div_list.findAll('input', attrs={'type': 'hidden'})
    raw_links = [i['value'] for i in items]
    clean_links = [k[:k.find('mp3') + 3] for k in raw_links]
    
    for link in clean_links:
        download_item(link)


def download_item(url):
    print 'Download request URL: %s' % (url)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    file_name = url.split('/')[-1]
    song = open(file_name, "wb")
    song.write(data)
    song.close
    print 'Done..\n'

if __name__ == '__main__':
    main()
