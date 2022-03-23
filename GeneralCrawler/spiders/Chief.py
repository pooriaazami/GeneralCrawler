import constants

import scrapy


class Chief(scrapy.spiders.CrawlSpider):
    name = 'Chief'

    def __init__(self):
        print('*'*100)
        self.__read_inital_seed()

    def __read_inital_seed(self):
        path = constants.INITIAL_SEED_PATH
        print(path)
        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                print(line)

        print('Done')
