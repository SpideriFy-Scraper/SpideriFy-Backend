from crawler.AmScrapper import AmScrapper


class AmazonSpider:
    """
    Main Spider Class for Amazon WebSite
    ====================================
    This class is resposible for calling Scraper, Sentiment Analyzer and Summarizer Components and URL validation Checking

    Attributes
    ++++++++++
    * url
    * AmScrapper
    * SentimentAnalyzer
    * Summerizer
    """

    AM_SCRAPER = None

    def __init__(self, url):
        self.url = url

    def run_spider(self):
        """
        Run the Spider by calling url checkers and the other main components
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        """
        if self.url_validatior():
            self.raw_data = self.call_scraper(self.url_normalizer)
            if self.raw_data == None:
                # log stopping Amazon spider
                return None

    def url_validator(self):
        """
        Checks the URL to belong to Amazon
        ++++++++++++++++++++++++++++++++++
        """
        pass

    def url_normalizer(self):
        """
        Generates the 'all review' URL of the entered link
        ++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        pass

    def call_scraper(self, normalized_url: str):
        """
        Creates a AmScrapper instance and calls the scrap function
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        self.AM_SCRAPER = AmScrapper(normalized_url)
        return self.AM_SCRAPER.scrap('dict')

    def call_sentiment_analyzer(self):
        pass

    def call_summarizer(self):
        pass
