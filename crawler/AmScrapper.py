import httpx
import asyncio
from selectorlib import Extractor
import json
import csv


class AmScrapper:
    extracted_data = None
    normalized_data = None
    review_counter = 0
    extractor_obj = Extractor.from_yaml_file('selectors.yml')
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    def __init__(self, url, headers):
        self.url = url
        if headers != None:
            self.headers = headers

    async def requester(self):
        # log : Downloading page
        async with httpx.AsyncClient() as requester:
            response = await requester.get(self.url, params=self.headers)
        if response.status_code >= 500:
            # log Page was blocked by Amazon. Please try using better proxies
            return None
        return response

    def extractor(self):

        data = self.requester()
        if data == None:
            return None
        # log extracing data...
        self.extracted_data = self.extractor_obj.extract(self.requester().text)
        self.normalized_data = {
            "product_title": self.extracted_data["product_title"]}
        self.normalized_data["URL"] = self.url
        # log normalizing Data
        for reviews in self.extracted_data["reviews"]:
            self.review_counter += 1
            self.normalized_data["review #{}".format(
                self.review_counter)] = reviews["content"]
        self.normalized_data["review_counts"] = self.review_counter
        return True

    def scaper(self, export_type=json):
        # log scrapper has started
        result = self.extractor()
        if result:
            return self.export_type()
        else:
            return None

    def json(self):
        # log dumping json
        return json.dumps(self.normalized_data)

    def csv_file(self):
        # log exporting csv file
        with open("\\fixtures\\Scraped-data.csv", 'w', newline='') as writfile:
            csvwriter = csv.writer(writfile, delimiter=',')
            for reviews in self.normalized_data.items():
                csvwriter.writerow([reviews[0], reviews[1]])
        return "\\fixtures\\Scraped-data.csv"

    def dict(self):
        # log exporting dictionary obj
        return self.normalized_data

    def json_file(self):
        # log exporting json file
        with open("\\fixtures\\Scraped-data.json", 'w') as writfile:
            json.dump(self.normalized_data, writfile)
        return "\\fixtures\\Scraped-data.json"
