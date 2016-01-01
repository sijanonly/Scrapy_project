import scrapy
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem


class MySpider(scrapy.Spider):
    name = "craig"
    allowed_domains = ["monster.com"]
    start_urls = ["http://jobview.monster.com/Warehouse-Associate-Up-to-35-per-hour-Job-Seattle-WA-US-146142960.aspx?mescoid=4300743001001&jobPosition=1"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='pl']")
        items = []
        for titles in titles:
            item = CraigslistSampleItem()
            item['title'] = titles.select("a/text()").extract()
            item['link'] = titles.select("a/@href").extract()
            items.append(item)

        return (items)