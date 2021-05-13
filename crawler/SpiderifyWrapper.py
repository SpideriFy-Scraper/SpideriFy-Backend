from crawler.AmazonSpider import AmazonSpider


class SpiderifyWrapper:

    AMAZONSPIDER = None
    DATA = None

    def __init__(self, url: str):
        self.AMAZONSPIDER = AmazonSpider(url)

    def start_amazon_spider(self):
        self.DATA = self.AMAZONSPIDER.run_spider()
        self.clean_attributes()
        return self.organize_reviews(self.DATA)

    def organize_reviews(self, data: dict):
        organized_data = {}
        organized_data["REVIEWS"] = []
        for key in data.keys():
            if key.startswith("REVIEW #"):
                organized_data["REVIEWS"].append(data[key])
            else:
                organized_data[key] = data[key]
        return organized_data

    def clean_attributes(self):
        self.AMAZONSPIDER.clean_attributes()
