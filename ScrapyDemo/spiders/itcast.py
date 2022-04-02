import scrapy
from ScrapyDemo.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        items = []
        teacherlist = response.xpath("//div[@class='li_txt']")
        for t in teacherlist:
            item = ItcastItem
            name = t.xpath("./h3/text()").extract()
            title = t.xpath("./h4/text()").extract()
            info = t.xpath("./p/text()").extract()
            item['name'] = name
            item['title'] = title
            item['info'] = info
            items.append(item)
        print("----------------------------------------------------------------------------")
        return items
