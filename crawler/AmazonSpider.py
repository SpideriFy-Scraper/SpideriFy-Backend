from crawler.AmScrapper import AmScrapper
from urllib.parse import urlparse
from crawler.AmSentimentAnalyzer import AmSentiment
from logger.Logger import Logger
from inspect import currentframe, getframeinfo
import os.path
import math


class AmazonSpider:
    """
    Main Spider Class for Amazon WebSite
    ====================================
    This class is responsible for calling Scraper, Sentiment Analyzer,
    Summarizer Components and URL validation Checking.
    """
    CUSTOM_SORT: list = []

    class AmSpiderConfig:
        """
        This is the Configuration Class of Amazon Spider
        +++++++++++++++++++++++++++++++++++++++++++++++

        Attributes
        ++++++++++
            * PRODUCT_URL
            * AmScrapper
            * SentimentAnalyzer
            * Summarizer
            * raw_data
            * AMAZON_DOMAINS
        """

        AM_SENT = None
        AM_SCRAPER = None
        AMAZON_DOMAINS = [
            "amazon.com.br", "amazon.ca", "amazon.com.mx", "amazon.com",
            "amazon.cn", "amazon.in", "amazon.co.jp", "amazon.sg",
            "amazon.com.tr", "amazon.ae", "amazon.sa", "amazon.fr",
            "amazon.de", "amazon.it", "amazon.nl", "amazon.pl",
            "amazon.es", "amazon.se", "amazon.co.uk", "amazon.com.au"
        ]
        PRODUCT_URL: str = None
        ALL_REVIEW_URL: str = None
        SCRAPED_DATA = None
        ANALYZED_DATA = None
        FINAL_DATA = None

        def clean_attributes(self):
            self.AM_SENT = None
            self.AM_SCRAPER = None
            self.AMAZON_DOMAINS = [
                "amazon.com.br", "amazon.ca", "amazon.com.mx", "amazon.com",
                "amazon.cn", "amazon.in", "amazon.co.jp", "amazon.sg",
                "amazon.com.tr", "amazon.ae", "amazon.sa", "amazon.fr",
                "amazon.de", "amazon.it", "amazon.nl", "amazon.pl",
                "amazon.es", "amazon.se", "amazon.co.uk", "amazon.com.au"
            ]
            self.PRODUCT_URL = None
            self.ALL_REVIEW_URL = None
            self.SCRAPED_DATA = None
            self.ANALYZED_DATA = None
            self.FINAL_DATA = None

    def __init__(self, url: str):
        self.AmSpiderConfig.PRODUCT_URL = url

    def run_spider(self, sentiment=True):
        """
        Run the Spider by calling url checkers and the other main components
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        if self.url_validator(url=self.AmSpiderConfig.PRODUCT_URL):
            self.AmSpiderConfig.SCRAPED_DATA = self.call_scraper(
                all_review_url=self.url_normalizer(
                    url=self.AmSpiderConfig.PRODUCT_URL),
                product_url=self.AmSpiderConfig.PRODUCT_URL
            )
            if self.AmSpiderConfig.SCRAPED_DATA is None:
                # log stopping Amazon spider
                script_name = os.path.basename(__file__)
                line_no = currentframe().f_lineno + 2
                logger = Logger(script_name, line_no)
                logger.log_warning("Stopping Amazon spider")
                return None
        else:
            # log URL is not valid
            script_name = os.path.basename(__file__)
            line_no = currentframe().f_lineno + 2
            logger = Logger(script_name, line_no)
            logger.log_error("URL is not valid")
            return None

        if sentiment:
            self.AmSpiderConfig.ANALYZED_DATA = self.call_sentiment_analyzer(
                self.dict_to_list_reviews(
                    data=self.AmSpiderConfig.SCRAPED_DATA)
            )

        self.merge_analyzed_scraped_data()

        return self.AmSpiderConfig.FINAL_DATA

    def dict_to_list_reviews(self, data: dict):
        """
        Create a list of reviews from scraped data
        """
        reviews_list = []

        for key in data.keys():
            if key.startswith("REVIEW #"):
                reviews_list.append(data[key]["content"])
                self.CUSTOM_SORT.append(key)

        return reviews_list

    def merge_analyzed_scraped_data(self):
        """
        Merge Two ANALYZED_DATA and SCRAPED_DATA and filling FINAL_DATA
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        script_name = os.path.basename(__file__)
        line_no = currentframe().f_lineno + 2
        logger = Logger(script_name, line_no)
        logger.log_info("Merging Scraped and Analyzed Data...")

        self.AmSpiderConfig.FINAL_DATA = self.AmSpiderConfig.SCRAPED_DATA.copy()

        if self.AmSpiderConfig.ANALYZED_DATA is None:
            script_name = os.path.basename(__file__)
            line_no = currentframe().f_lineno + 2
            logger = Logger(script_name, line_no)
            logger.log_info("Skipping Merging... ")

            return

        for i in range(len(self.CUSTOM_SORT)):
            self.AmSpiderConfig.FINAL_DATA[self.CUSTOM_SORT[i]]["sentiment"] = \
                str(self.sigmoid(self.AmSpiderConfig.ANALYZED_DATA[i][0]))

    def sigmoid(self, grade):
        return 1 / (1 + math.exp(-grade))

    def url_validator(self, url: str) -> bool:
        """
        Checks the URL to belong to Amazon
        ++++++++++++++++++++++++++++++++++
        """

        url_obj = urlparse(url)
        domain_name = str(url_obj.netloc)[4:]
        if domain_name in AmazonSpider.AmSpiderConfig.AMAZON_DOMAINS:
            return True
        else:
            return False

    def url_normalizer(self, url: str) -> str:
        """
        Generates the 'all review' URL of the entered link
        ++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        if url.find("all_reviews") > 0:
            return url
        obj = urlparse(url)
        parts = obj.path.split('/')
        review_url = obj.scheme + "://" + obj.netloc + "/" + \
            parts[1] + "/product-reviews/" + parts[3] + \
            "/ie=UTF8&reviewerType=all_reviews"
        return review_url

    def call_scraper(self, all_review_url: str, product_url: str):
        """
        Creates a AmScrapper instance and calls the scrap function
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        self.AmSpiderConfig.AM_SCRAPER = AmScrapper(
            all_review_url, product_url=product_url, headers=None)

        return self.AmSpiderConfig.AM_SCRAPER.scrap('dict')

    def call_sentiment_analyzer(self, review_list: list):
        """
        Create the AmSentiment Object and call the sent_analyz func
        """
        self.AmSpiderConfig.AM_SENT = AmSentiment(None)
        return self.AmSpiderConfig.AM_SENT.sent_analyz(review_list)

    def clean_attributes(self):
        self.AmSpiderConfig.AM_SCRAPER.clean_attributes()
        self.CUSTOM_SORT = []
        self.AmSpiderConfig.clean_attributes()

    def call_summarizer(self):
        pass
