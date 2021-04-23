from crawler.AmazonSpider import AmazonSpider


class SpiderifyWrapper:

    AMAZONSPIDER = None
    DATA = None

    def __init__(self, url: str):
        self.AMAZONSPIDER = AmazonSpider(url)

    def start_amazon_spider(self):
        self.DATA = self.AMAZONSPIDER.run_spider()
        return self.DATA
