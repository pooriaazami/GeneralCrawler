import constants

import scrapy


class Chief(scrapy.spiders.CrawlSpider):
    name = 'Chief'

    # def __init__(self):
    #     print('*'*100)

    def start_requests(self):
        path = constants.INITIAL_SEED_PATH

        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                # yield line
            yield scrapy.Request(line)

    def parse(self, responce):
        print(responce)

