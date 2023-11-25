# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



import openpyxl

class ExcelExportPipeline:
    def __init__(self):
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.append(['Name', 'Work Place', 'First Department', 'Recruit Num'])

    def process_item(self, item, spider):
        row = [
            item['name'],
            ', '.join(item['workPlaceNameList']),
            item['firstDepName'],
            item['recruitNum']
        ]
        self.sheet.append(row)
        return item

    def close_spider(self, spider):
        # Save the workbook when the spider is closed
        self.workbook.save('output.xlsx')
