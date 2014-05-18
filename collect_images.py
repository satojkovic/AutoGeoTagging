#-*- coding: utf-8 -*-
from __future__ import with_statement
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import argparse


def get_soup(url):
    return BeautifulSoup(requests.get(url).text)


def get_images_from_bing(query):
    url = "http://www.bing.com/images/search?q=" + query + \
          "&gft=+filterui:color2-bw+filterui:imagesize-large&FORM=R5IR3"

    soup = get_soup(url)
    images = [a['src2']
              for a in soup.find_all('img',
                                     {'src2': re.compile('mm.bing.net')})]
    for img in images:
        raw_img = urllib2.urlopen(img).read()
        cntr = len([i for i in os.listdir('images') if query in i]) + 1
        with open('images/' + query + '_' + str(cntr) + '.jpg',
                  'w') as f:
            f.write(raw_img)

    return cntr


def main():
    parser = argparse.ArgumentParser(
        description='collect training images from Bing'
    )

    parser.add_argument(
        dest='query',
        help='search query',
        nargs='+',
    )

    args = parser.parse_args()

    for q in args.query:
        num_images = get_images_from_bing(q)
        print '[%s] got %d images' % (q, num_images)

if __name__ == '__main__':
    main()
