import scrapy
from scrapy.http import TextResponse

from golang_versions.items import VersionsItem


class VersionsSpider(scrapy.Spider):
    name = "versions"
    allowed_domains = ["go.dev"]
    start_urls = ["https://go.dev/dl/"]

    def parse(self, response: TextResponse):
        versions = VersionsItem()

        mainVersions = response.xpath(
            "//*[@class='toggleVisible']/@id"
        ).getall()
        archivedVersions = response.xpath("//*[@class='toggle']/@id").getall()[
            1:
        ]

        versions["versions"] = mainVersions + archivedVersions

        return versions
