# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    name = scrapy.Field()
    workPlaceNameList = scrapy.Field()
    firstDepName = scrapy.Field()
    recruitNum = scrapy.Field()

    pass
