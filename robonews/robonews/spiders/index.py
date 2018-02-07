import scrapy
from robonews.items import RobonewsItem
from time import strftime

def readFile():
	f = open("ksp200list.txt", 'r')
	lines = f.readlines()
	f.close()
	return lines

class indexWeb(scrapy.Spider):
	name="index"
	allowed_domains=["finance.daum.net/"] #crwaling domain
	form_url = "http://finance.daum.net/item/main.daum?code="

	start_urls = [ ]
	ecode = readFile()
	for code in ecode :
		start_urls.append(form_url + code[0:6])

	def parse(self, response):
		time = str(strftime('%H:%M:%S'))
		items = []

		for sel in response.css('div.topInfo'):
			item = RobonewsItem()
			item['time'] = time
			item['ename']=sel.css('h2::text').extract()
			item['ecode']=sel.css('span.stockCode::text').extract()
			item['stock'] = sel.css('em.curPrice::text').extract()
			item['updown'] = sel.css('span.sise::text').extract()
			item['percent'] = sel.css('span.rate::text').extract()
			item['trade'] = sel.css('span.num_trade::text')[0].extract()
			item['trade_rate'] = sel.css('span.txt_rate::text').extract()
			item['rmoney'] = sel.css('span.num_trade::text')[1].extract()
			items.append(item)
		return items

