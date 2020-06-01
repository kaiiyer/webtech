from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    name = "example"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.in/b?ie=UTF8&node=976389031&pf_rd_r=FKG5NM456SXP3K1WE5ZF&pf_rd_p=d4329482-f2d5-4dfb-9ce1-f1d8dab81037",]
    def parse(self, response):
        # (.acs-product-block__product-title span) path to extract the names of the books on the amazon site
        # since it produces a list we can list out one name from the list by using
        # title = response.css('.acs-product-block__product-title span::text')[index_number].extract()
        title = response.css('.acs-product-block__product-title span::text')[0].extract()
        # yields the result
        yield {'BookTitle': title}
