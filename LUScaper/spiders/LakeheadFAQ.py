import scrapy
#import sys
#sys.path.append('/Users/jaish/Downloads/Scraper')
from LUScaper.spiders.items import FAQ 



class LakeheadSpider(scrapy.Spider):
    name = 'lakehead'
    allowed_domain = ['www.lakeheadu.ca']
    start_urls = ['https://www.lakeheadu.ca/faculty-and-staff/departments/services/helpdesk/articles/faq']
    custom_settings =  {
        'FEED_URI' :    'tmp/LUfuturestudents_faq.csv'
    }

    def parse(self, response):
        for item in response.xpath("//div[@class='field-items even']//h4"):
            yield {
                'question' : item.xpath(".//h4/text()").extract(),
                'answer' : item.xpath(".//p/text()").extract(),
                'UniversityID' : 'ulakehead'
            }




            