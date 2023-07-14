import json
import os

import scrapy

from golang_versions.items import SelectedVersionItem, SelectedVersionListItem


class SelectedVersionSpider(scrapy.Spider):
    name = "selected_version"
    allowed_domains = ["go.dev"]
    start_urls = ["https://go.dev/dl/"]

    def parse(self, response):
        f = open(os.getcwd() + "/data/versions.json")
        file = json.load(f)
        f.close()

        versions_list = SelectedVersionListItem()
        result = {}
        versions = file[0]["versions"]

        for version in versions:
            field = []
            download_list = response.xpath(
                f"//*[@id='{version}']//div[@class='expanded']//table//tr[@class='highlight ']"
            )

            for element in download_list:
                selected_version = SelectedVersionItem()

                rows = element.xpath("td")

                selected_version["filename"] = rows[0].xpath("a/@href").get()
                selected_version["size"] = rows[4].xpath("text()").get()
                selected_version["checksum"] = rows[5].xpath("tt/text()").get()

                field.append(selected_version)

            result[version] = field

        versions_list["all_versions"] = result

        return versions_list
