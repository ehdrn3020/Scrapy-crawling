# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import json
import codes

class FillterKangweb(object):
	words_to_fillter = ['ideal', 'goal']
#	def __init__(self):
#		self.file = codecs.open('kangR.json','wb',encoding="utf-8")

	def process_item(self, item, spider):
		for word in self.words_to_filter:
			if word in item['ptag'].lower():
				raise DropItem("Contains forbidden word: %s" % word)  
	else:
		return item
