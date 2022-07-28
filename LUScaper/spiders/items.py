import scrapy
from tables import Description

#Description = scrapy.Field()
#Rating = scrapy.Field()
#Url = scrapy.Field()
#RetailPrice = scrapy.Field()
#Price

class FAQ(scrapy.Item):
    question = scrapy.Field()
    answer = scrapy.Field()
    UniversityId = scrapy.Field()


