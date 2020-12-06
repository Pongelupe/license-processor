#!/usr/bin/env python3

import scrapy
from scrapy.crawler import CrawlerProcess
from maven_repository_spider import MavenRepositorySpider 
import sys
import xml.etree.ElementTree as ET

path_pom = sys.argv[1] # path to maven xml

dependencies = []

root = ET.parse(path_pom).getroot()
for el in root:
    if 'dependencies' in el.tag:
        for d in el:
            dependency = {'groupId': '', 'artifactId': '' }
            dependencies.append(dependency)
            for i in d:
                if 'groupId' in i.tag:
                    dependency['groupId'] = i.text
                elif 'artifactId' in i.tag:
                    dependency['artifactId'] = i.text

print(dependencies)

process = CrawlerProcess(settings={
    'BOT_NAME': 'maven_repository_scrapper',
    'FEED_FORMAT': 'json',
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'DOWNLOAD_DELAY': 0.75,
    'ITEM_PIPELINES': {
        #'pipelines.FilterPipeline': 300,
        #'pipelines.SaveReviewPipeline': 400
        }}
    )
process.crawl(MavenRepositorySpider, dependencies=dependencies)
process.start()
