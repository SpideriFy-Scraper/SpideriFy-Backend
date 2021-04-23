from crawler.AmScrapper import AmScrapper
from urllib.parse import urlparse
from crawler.AmSentimentAnalyzer import AmSentiment

class AmazonSpider:
    """
    Main Spider Class for Amazon WebSite
    ====================================
    This class is responsible for calling Scraper, Sentiment Analyzer,
    Summarizer Components and URL validation Checking.
    """
    CUSTOM_SORT : list = list
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
        AM_SENT =
        AM_SCRAPER = None
        AMAZON_DOMAINS = [
            "amazon.com.br", "amazon.ca", "amazon.com.mx", "amazon.com",
            "amazon.cn", "amazon.in", "amazon.co.jp", "amazon.sg",
            "amazon.com.tr", "amazon.ae", "amazon.sa", "amazon.fr",
            "amazon.de", "amazon.it", "amazon.nl", "amazon.pl",
            "amazon.es", "amazon.se", "amazon.co.uk", "amazon.com.au"
        ]
        PRODUCT_URL = str
        ALL_REVIEW_URL = str
        SCRAPED_DATA = None
        ANALYZED_DATA = None
        FINAL_DATA = None

    def __init__(self, url: str):
        self.AmSpiderConfig.PRODUCT_URL = url

    def run_spider(self):
        """
        Run the Spider by calling url checkers and the other main components
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        if self.url_validator():
            self.AmSpiderConfig.SCRAPED_DATA = self.call_scraper(
                self.url_normalizer(), self.AmSpiderConfig.PRODUCT_URL
            )
            if self.AmSpiderConfig.SCRAPED_DATA is None:
                # log stopping Amazon spider
                pass
        else:
            # log URL is not valid
            return None

        self.AmSpiderConfig.ANALYZED_DATA = self.call_sentiment_analyzer(\
            self.dict_to_list_reviews(self.AmSpiderConfig.SCRAPED_DATA)
            )

        self.merge_analyzed_scraped_data()

        return self.AmSpiderConfig.FINAL_DATA

    def dict_to_list_reviews(self,data : dict):

        reviews_list = []

        for key in data.keys():
            if str(key).startswith("REVIEW"):
                reviews_list.append(data[key]["content"])
                self.CUSTOM_SORT.append(key)

        return reviews_list

    def merge_analyzed_scraped_data(self):

        self.AmSpiderConfig.FINAL_DATA = self.AmSpiderConfig.SCRAPED_DATA.copy()

        for i in range(len(self.CUSTOM_SORT)):
            self.AmSpiderConfig.FINAL_DATA[self.CUSTOM_SORT[i]]["sentiment"] = \
                self.AmSpiderConfig.ANALYZED_DATA[i][0]

    def url_validator(self, url: str = AmSpiderConfig.PRODUCT_URL) -> bool:
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

    def url_normalizer(self, url: str = AmSpiderConfig.PRODUCT_URL) -> str:
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
            "/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
        return review_url

    def call_scraper(self, all_review_url: str = AmSpiderConfig.ALL_REVIEW_URL,
                     product_url: str = AmSpiderConfig.PRODUCT_URL):
        """
        Creates a AmScrapper instance and calls the scrap function
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        self.AmSpiderConfig.AM_SCRAPER = AmScrapper(
            all_review_url, headers=None)
        return self.AmSpiderConfig.AM_SCRAPER.scrap('dict')

    def call_sentiment_analyzer(self,review_list : list):

        self.AmSpiderConfig.AM_SENT = AmSentiment(None)

        return self.AmSpiderConfig.AM_SENT.sent_analyz(review_list)


    def call_summarizer(self):
        pass
