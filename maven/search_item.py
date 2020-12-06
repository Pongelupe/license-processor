import scrapy

class SearchItem(scrapy.Item):
    license = scrapy.Field()
    categories = scrapy.Field()
    tags = scrapy.Field()
