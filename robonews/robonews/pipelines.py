# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import codecs

class RobonewsPipeline(object):
#	def __init__(self):
#		self.file = codecs.open('index.json','wb',encoding="utf-8")

	def process_item(self, item, spider):
        	return item
