#!/usr/bin/env python
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import urllib2


def make_soup(url):
	html = urllib2.urlopen(url).read().decode('shift-jis')
	soup = BeautifulSoup(html)	
	return soup


def prettify_price(price):
	price = price.replace(u'\uffe5 ', '')
	price = price.replace(',', '')
	price = int(price)
	return(price)


def scrape_bestseller(soup): 
	result = []

	for item in soup.findAll('div', {'class': 'zg_item_normal'}): 
		tmp = []

	    ## title 
		zg_title = item.find('div', {'class': 'zg_title'})
		title = zg_title.string.replace('\n', '')
		tmp.append(title)

		## link
		link = zg_title.find('a').get('href')
		link = link.replace('\n', '')
		tmp.append(link)

		## brand
		brand = item.find('div', {'class': 'zg_byline'}).string
		brand = brand.replace('\n', '')
		tmp.append(brand)

		## list price
		try:
			list_price = item.find('span', {'class': 'listprice'}).string
			list_price = prettify_price(list_price)
		except AttributeError:
			list_price = 'NA'
		tmp.append(list_price)

		## price
		price = item.find('span', {'class': 'price'}).find('b').string
		price = prettify_price(price)
		tmp.append(price)

		result.append(tmp)
		
	return result


		
		
		


