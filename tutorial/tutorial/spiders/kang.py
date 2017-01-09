import scrapy

from tutorial.items import KangItem

class Kangweb(scrapy.Spider):
	name="kang"
	allowed_domains=["ehdrn3020.dothome.co.kr"] #crwaling domain
	start_urls = ["http://ehdrn3020.dothome.co.kr/index.html/"] #start point

	def parse(self, response):
		items = []
		for sel in response.xpath('//html'):
			item = KangItem()
			item['title']=sel.xpath('//title/text()').extract()
			item['ptag']=sel.xpath('//p/text()').extract()
			item['img']=sel.xpath('//img/@src').extract()
			item['link']=sel.xpath('//a/@href').extract()
			item['clss']=sel.xpath('//@class="container-fluid"').extract()
			items.append(item)
		return items
		
