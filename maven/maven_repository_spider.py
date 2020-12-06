import scrapy
from search_item import SearchItem

class MavenRepositorySpider(scrapy.Spider):

    def __init__(self, dependencies):
        self.name = 'maven_repository_spider'
        self.start_urls = []
        for dependency in dependencies:
            url = f"https://mvnrepository.com/artifact/{dependency['groupId']}/{dependency['artifactId']}"
            self.start_urls.append(url)

        scrapy.Spider.__init__(self)

    def parse(self, response):
        table = response.xpath('(//table[@class="grid"])[1]')
        dependency = SearchItem()
        for tr in table.xpath('.//tr'):
            header = tr.xpath('.//th/text()').get()
            if 'License' in header:
                dependency['license'] = tr.xpath('.//td/span/text()').getall()
            elif 'Used By' not in header:
                values = tr.xpath('.//td/a/text()').getall()
                dependency[header.lower()] = values

        print(dependency)
        yield dependency
