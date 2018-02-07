# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RobonewsItem(scrapy.Item):
	time = scrapy.Field()
    	ename = scrapy.Field()
	ecode = scrapy.Field()
	stock = scrapy.Field()
	updown = scrapy.Field()
	percent = scrapy.Field()
	trade = scrapy.Field()
	trade_rate = scrapy.Field()
	rmoney = scrapy.Field()

