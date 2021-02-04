import scrapy

from scrapy.loader import ItemLoader
from ..items import CapitaliomItem
from itemloaders.processors import TakeFirst


class CapitaliomSpider(scrapy.Spider):
	name = 'capitaliom'
	start_urls = ['https://www.capital-iom.com/blog']

	def parse(self, response):
		post_links = response.xpath('//div[@class="blog-title"]/a[@class="h2 blog-header"]/@href')
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//div[@class="w-pagination-wrapper pagination"]/a/@href')
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="article w-richtext"]//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('(//div[@class="blog-date text-muted"]/text())[2]').get()

		item = ItemLoader(item=CapitaliomItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
