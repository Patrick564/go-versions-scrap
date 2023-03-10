import scrapy

from golang_versions.items import VersionsItem


class VersionsSpider(scrapy.Spider):
    name = "versions"
    allowed_domains = ["go.dev"]
    start_urls = ["http://go.dev/dl/"]

    def parse(self, response):
        versions = VersionsItem()

        versions["versions"] = response.xpath("//*[@class='toggle']/@id").getall()

        return versions
