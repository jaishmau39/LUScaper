import scrapy
#import sys
#sys.path.append('/Users/jaish/Downloads/Scraper')
from LUScaper.spiders.items import FAQ 



class LakeheadSpider(scrapy.Spider):
    name = 'lakeheadu'
    allowed_domain = ['www.lakeheadu.ca']
    start_urls = ['https://www.lakeheadu.ca/programs/departments/computer-science/future-students/faq']
    custom_settings =  {
        'FEED_URI' :    'tmp/lakeheadFAQ.csv'
    }



    def parse(self, response):
        for item in response.xpath("//div[@class='field-item even']//p"):
            yield {
                'question' : item.xpath(".//strong/text()").extract(),
                'answer' : item.xpath(".//text()").extract(),
                'UniversityID' : 'ulakehead'
            }



            