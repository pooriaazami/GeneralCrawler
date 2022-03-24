import constants

import scrapy


class Chief(scrapy.spiders.CrawlSpider):

    name = 'Chief'

    custom_settings = {
        'COOKIES_ENABLED': False,
        'AJAXCRAWL_ENABLED': True,
        'REDIRECT_MAX_TIMES': 10
    }

    # def __init__(self):
    #     print('*'*100)

    def start_requests(self):
        path = constants.INITIAL_SEED_PATH

        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                # yield line
                yield scrapy.Request(line, callback=self.parse)

    def parse(self, response):
        self.logger.info(
            'Got successful response from {}'.format(response.url))
        print('*'*100)
        print(response)
