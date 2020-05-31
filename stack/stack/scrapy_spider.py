# Read scrapy.txt
from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    name = "general" #Name to run the spider
    allowed_domains = ["domain"] 
    start_urls = ["url","more urls can be mentioned"] # more than 1 url can be mentioned for crawling
    def parse(self, response):
        # here the path can be chosen using the css selector gadget chrome which is a google chrome extension
        # the path is the information that you want extract
        title = response.css('path::text').extract() 
        # here 'yield' yields the result
        yield {'BookTitle': title}
        
