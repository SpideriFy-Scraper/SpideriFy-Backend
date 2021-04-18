import httpx
import asyncio
from selectorlib import Extractor
import json
import csv


class AmScrapper:
    """
    Scrapper Class for Amazon WebSite
    ================================
    Attributes:
    -----------
    export_type
    * extracted_data
    * normalized_data
    * review_counter
    * extractor_obj
    * headers
    """
    export_type = {"json": 'json', "dict": 'dict', "csv_file": 'csv_file'}
    extracted_data: dict = None
    normalized_data = None
    review_counter = 0
    extractor_obj = Extractor.from_yaml_file('crawler/selectors.yml')
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/\
        537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image\
        /webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    def __init__(self, url, headers):
        self.url = url
        if headers is not None:
            self.headers = headers

    async def requester(self):
        """
        Return the response of GET request or in case of failure return None
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        This func request the page using GET method with the help of httpx and asyncio
        """
        # log : Downloading page
        async with httpx.AsyncClient() as requester:
            response = await requester.get(self.url, params=self.headers)
        if response.status_code != httpx.codes.OK:
            # log failed to download the page
            if response.status_code >= 500:
                pass
                # log Page was blocked by Amazon.
                # Please try using better proxies.
            return None

        return response

    def extractor(self):
        """
        Return None if Data could not extracted Return True
        if required Data has been extracted
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        This func calls the requester and receive the data, then normalize
        the data and store it in self.normalize_data as a dict
        """
        data = asyncio.run(self.requester())
        if data is None:
            return None
        # log extracting data...
        self.extracted_data = self.extractor_obj.extract(data.text)
        self.normalized_data = {
            "product_title": self.extracted_data["product_title"]
        }
        self.normalized_data["Normalized_URL"] = self.url
        # log normalizing Data
        for reviews in self.extracted_data["reviews"]:
            self.review_counter += 1
            self.normalized_data["review_#{}".format(
                self.review_counter)] = reviews["content"]
        self.normalized_data["review_counts"] = self.review_counter
        return True

    def scrap(self, export_type='json'):
        """
        Calls The extractor func and exporter func
        -------------------------------------------
        Parameters
        ++++++++++
        * export_type='json'
        """
        # log scrapper has started
        result = self.extractor()
        if result:
            return getattr(self, export_type)()
        else:
            return None

    def json(self):
        """
        Dumps the data and return a json object
        +++++++++++++++++++++++++++++++++++++++
        """
        # log dumping json
        return json.dumps(self.normalized_data)

    def csv_file(self):
        """
        Export the data to a csv file and return the path directed to it
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        # log exporting csv file
        with open("/fixtures/Scraped-data.csv", 'w', newline='') as writefile:
            csv_writer = csv.writer(writefile, delimiter=',')
            for reviews in self.normalized_data.items():
                csv_writer.writerow([reviews[0], reviews[1]])
        return "/fixtures/Scraped-data.csv"

    def dict(self):
        """
        Return the data itself
        ++++++++++++++++++++++
        """
        # log exporting dictionary obj
        return self.normalized_data

    def json_file(self):
        """
        Export the data to a json file and return the path directed to it
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        # log exporting json file
        with open("/fixtures/Scraped-data.json", 'w') as writfile:
            json.dump(self.normalized_data, writfile)
        return "/fixtures/Scraped-data.json"


if __name__ == '__main__':
    testScraper = AmScrapper(
        url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews", headers=None)
    print(testScraper.scrap('dict'))
