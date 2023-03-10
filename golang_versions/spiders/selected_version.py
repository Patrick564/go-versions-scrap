import scrapy

from golang_versions.items import SelectedVersionItem


class SelectedVersionSpider(scrapy.Spider):
    name = "selected_version"
    allowed_domains = ["go.dev"]
    start_urls = ["http://go.dev/dl/"]

    def parse(self, response):
        selected_version = SelectedVersionItem()

        response.xpath("//*[@id='go1.20.2']//div[@class='expanded']//table//tr[@class='highlight']")
