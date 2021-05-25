import math
from unittest import TestCase
from crawler.AmazonSpider import AmazonSpider


class TestRunSpider(TestCase):
    def setUp(self):
        self.spider = AmazonSpider(
            url="https://www.amazon.com/Acer-Chromebook-Convertible-Bluetooth-CP311-2H-C679/dp/B086MBQKH2/ref=sr_1_1_sspa?dchild=1&keywords=hp&qid=1621192415&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaVUtYUklUVzlIN0EmZW5jcnlwdGVkSWQ9QTAxMzY5NDIyOEJKRE9JTjBLMFlJJmVuY3J5cHRlZEFkSWQ9QTAxNDg4NDUyTDRLWUlDRVQwTjVQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==", )

    def test_run_spider_easy_one(self):
        self.assertTrue('PRODUCT_NAME' in self.spider.run_spider(sentiment=False))
        print('test_run_spider_easy_one passed!')

    def test_run_spider_easy_two(self):
        pass

    def test_run_spider_medium_one(self):
        pass

    def test_run_spider_medium_two(self):
        pass

    def test_run_spider_hard_one(self):
        pass

    def test_run_spider_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.spider = None


class TestDictToListReviews(TestCase):
    def setUp(self) -> None:
        self.spider = AmazonSpider(
            url="https://www.amazon.com/Acer-Chromebook-Convertible-Bluetooth-CP311-2H-C679/dp/B086MBQKH2/ref=sr_1_1_sspa?dchild=1&keywords=hp&qid=1621192415&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaVUtYUklUVzlIN0EmZW5jcnlwdGVkSWQ9QTAxMzY5NDIyOEJKRE9JTjBLMFlJJmVuY3J5cHRlZEFkSWQ9QTAxNDg4NDUyTDRLWUlDRVQwTjVQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==", )

    def test_requester_easy_one(self):
        input = {
            "REVIEW #1": {
                "title": "4GB RAM NOT 8GB RAM!",
                "content": "This is NOT an 8GB RAM! It is only 4GB RAM! With that being said, it is advertised as an 8GB RAM, packaging was basically triple boxes, packaged very well! Came with backpack and mouse pad as described. Initial start up was slow, but moving fast now that it\u2019s set up. Only gave 3 stars because the RAM is a significant part in purchasing the right laptop!",
                "date": "Reviewed in the United States on November 26, 2019",
                "variant": None,
                "verified": True,
                "author": "Atara83",
                "rating": 3.0
            },
            "REVIEW #2": {
                "title": "Great Laptop, Good Value, well worth it",
                "content": "Amazon delivered my order promptly. This laptop bundle came in a solid double packaging, and it comes with a backpack and a mouse pad. I am so amazed by the backpack & mouse pad quality, and I don\u2019t mind the little legendary logo both accessories. I had HP laptops previously and had been pleased with their performance. This one is exceptional for someone who isn't into a lot of gaming and such. I am self employed and I bought this laptop for my work, I only need basic internet browsing and need to do some basic excel reporting, so this computer is perfect for me and at an amazing price, especially it came with bonus accessories.",
                "date": "Reviewed in the United States on September 3, 2019",
                "variant": None,
                "verified": True,
                "author": "Maggie",
                "rating": 5.0
            },
            "REVIEW #3": {
                "title": "Nice, but faulty!",
                "content": "I got a faulty laptop from day 1! Before I ordered I made sure to ask the seller if it\u2019s NEW.  Well, I got it and it shuts down every 2 minutes. They offered refund, but I live outside the US and returning this mess will cost me a lot. I thought it was tested/upgraded as stated. How can they missed mines when it shuts off right after start up?  Now I\u2019ve trust issues with purchasing electronics online now.",
                "date": "Reviewed in the United States on November 2, 2019",
                "variant": None,
                "verified": True,
                "author": "Candice",
                "rating": 1.0
            },
            "REVIEW #4": {
                "title": "Pretty much everything that i was looking for in a large laptop",
                "content": "the box delivered on time and safe.  it was double boxed and packed well. the included laptop bag is good quality and will work well when i need to use it.  i would not buy this laptop for the bag but it is a nice value add. speed and response on this laptop is everything that i was looking for.  set up was easy and came 1/2 charged so i didn't have to immediately plug in. My only concern is battery life.  this is the largest laptop that i have ever had.  i use mainly for school and work.  i don't game or stream a lot of video.  but in the 4 hours that i have had the laptop open today, the battery has already dropped to 25%.  i don't know if that is to be expected with the multiple windows open and the large screen but i don't expect to get 8 hours out of the charge if i am on it.  I will keep the power cable near by.  if you are using less, you might make a full day on a charge.",
                "date": "Reviewed in the United States on October 31, 2019",
                "variant": None,
                "verified": True,
                "author": "Gregg Stepp",
                "rating": 4.0
            },
            "REVIEW #5": {
                "title": "Nice laptop",
                "content": "Nice looking laptop. Very light. Quality is very good and very happy with this purchase. Got this laptop earlier than expected. Highly recommended seller and a product!",
                "date": "Reviewed in the United States on August 30, 2019",
                "variant": None,
                "verified": True,
                "author": "T. Khadu",
                "rating": 5.0
            },
            "REVIEW #6": {
                "title": "Excellent",
                "content": "Excellent computer, pretty easy setup, excellent quality backpack. I\u2019d recommend this to anyone looking for a good computer at an affordable price.",
                "date": "Reviewed in the United States on October 2, 2019",
                "variant": "What's this?",
                "verified": True,
                "author": "Megs77",
                "rating": 5.0
            }
        }

        output = [
            'This is NOT an 8GB RAM! It is only 4GB RAM! With that being said, it is advertised as an 8GB RAM, packaging was basically triple boxes, packaged very well! Came with backpack and mouse pad as described. Initial start up was slow, but moving fast now that it’s set up. Only gave 3 stars because the RAM is a significant part in purchasing the right laptop!',
            "Amazon delivered my order promptly. This laptop bundle came in a solid double packaging, and it comes with a backpack and a mouse pad. I am so amazed by the backpack & mouse pad quality, and I don’t mind the little legendary logo both accessories. I had HP laptops previously and had been pleased with their performance. This one is exceptional for someone who isn't into a lot of gaming and such. I am self employed and I bought this laptop for my work, I only need basic internet browsing and need to do some basic excel reporting, so this computer is perfect for me and at an amazing price, especially it came with bonus accessories.",
            'I got a faulty laptop from day 1! Before I ordered I made sure to ask the seller if it’s NEW.  Well, I got it and it shuts down every 2 minutes. They offered refund, but I live outside the US and returning this mess will cost me a lot. I thought it was tested/upgraded as stated. How can they missed mines when it shuts off right after start up?  Now I’ve trust issues with purchasing electronics online now.',
            "the box delivered on time and safe.  it was double boxed and packed well. the included laptop bag is good quality and will work well when i need to use it.  i would not buy this laptop for the bag but it is a nice value add. speed and response on this laptop is everything that i was looking for.  set up was easy and came 1/2 charged so i didn't have to immediately plug in. My only concern is battery life.  this is the largest laptop that i have ever had.  i use mainly for school and work.  i don't game or stream a lot of video.  but in the 4 hours that i have had the laptop open today, the battery has already dropped to 25%.  i don't know if that is to be expected with the multiple windows open and the large screen but i don't expect to get 8 hours out of the charge if i am on it.  I will keep the power cable near by.  if you are using less, you might make a full day on a charge.",
            'Nice looking laptop. Very light. Quality is very good and very happy with this purchase. Got this laptop earlier than expected. Highly recommended seller and a product!',
            'Excellent computer, pretty easy setup, excellent quality backpack. I’d recommend this to anyone looking for a good computer at an affordable price.']
        self.assertEqual(self.spider.dict_to_list_reviews(input), output)

    def test_requester_easy_two(self):
        pass

    def test_requester_medium_one(self):
        pass

    def test_requester_medium_two(self):
        pass

    def test_requester_hard_one(self):
        pass

    def test_requester_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestMergeAnalyzedScrapedData(TestCase):
    def setUp(self) -> None:
        pass

    def test_requester_easy_one(self):
        pass

    def test_requester_easy_two(self):
        pass

    def test_requester_medium_one(self):
        pass

    def test_requester_medium_two(self):
        pass

    def test_requester_hard_one(self):
        pass

    def test_requester_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestSigmoid(TestCase):
    def setUp(self) -> None:
        self.spider = AmazonSpider(
            url="https://www.amazon.com/Acer-Chromebook-Convertible-Bluetooth-CP311-2H-C679/dp/B086MBQKH2/ref=sr_1_1_sspa?dchild=1&keywords=hp&qid=1621192415&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaVUtYUklUVzlIN0EmZW5jcnlwdGVkSWQ9QTAxMzY5NDIyOEJKRE9JTjBLMFlJJmVuY3J5cHRlZEFkSWQ9QTAxNDg4NDUyTDRLWUlDRVQwTjVQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==", )

    def test_sigmoid_easy_one(self):
        input = 0.25
        output = 1 / (1 + math.exp(-0.25))
        self.assertEqual(self.spider.sigmoid(input), output)

    def test_sigmoid_easy_two(self):
        input = -0.25
        output = 1 / (1 + math.exp(0.25))
        self.assertEqual(self.spider.sigmoid(input), output)

    def test_sigmoid_medium_one(self):
        pass

    def test_sigmoid_medium_two(self):
        pass

    def test_sigmoid_hard_one(self):
        pass

    def test_sigmoid_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestUrlValidator(TestCase):
    def setUp(self) -> None:
        self.url = "https://www.amazon.com/Acer-Chromebook-Convertible-Bluetooth-CP311-2H-C679/dp/B086MBQKH2/ref=sr_1_1_sspa?dchild=1&keywords=hp&qid=1621192415&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaVUtYUklUVzlIN0EmZW5jcnlwdGVkSWQ9QTAxMzY5NDIyOEJKRE9JTjBLMFlJJmVuY3J5cHRlZEFkSWQ9QTAxNDg4NDUyTDRLWUlDRVQwTjVQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
        self.spider = AmazonSpider(
            url=self.url)

    def test_url_validator_easy_one(self):
        self.assertEqual(self.spider.url_validator(self.url), True)

    def test_url_validator_easy_two(self):
        pass

    def test_url_validator_medium_one(self):
        pass

    def test_url_validator_medium_two(self):
        pass

    def test_url_validator_hard_one(self):
        pass

    def test_url_validator_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestUrlNormalizer(TestCase):
    def setUp(self) -> None:
        self.url = "https://www.amazon.com/Acer-Chromebook-Convertible-Bluetooth-CP311-2H-C679/dp/B086MBQKH2/ref=" \
                   "sr_1_1_sspa?dchild=1&keywords=hp&qid=1621192415&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWV" \
                   "yPUFaVUtYUklUVzlIN0EmZW5jcnlwdGVkSWQ9QTAxMzY5NDIyOEJKRE9JTjBLMFlJJmVuY3J5cHRlZEFkSWQ9QTAxNDg4ND" \
                   "UyTDRLWUlDRVQwTjVQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1Z" \
                   "Q=="
        self.spider = AmazonSpider(
            url=self.url)

    def test_url_normalizer_easy_one(self):
        input = "https://www.amazon.com/Acer-Chromebook-Convertible-Bluetooth-CP311-2H-C679/dp/B086MBQKH2" \
                "/ref=sr_1_1_sspa?dchild=1&keywords=hp&qid=1621192415&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaW" \
                "VyPUFaVUtYUklUVzlIN0EmZW5jcnlwdGVkSWQ9QTAxMzY5NDIyOEJKRE9JTjBLMFlJJmVuY3J5cHRlZEFkSWQ9QTAxNDg4NDUyT" \
                "DRLWUlDRVQwTjVQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
        output = "https://www.amazon.com/Acer-Chromebook-Convertible-Bluetooth-CP311-2H-C679/product-reviews/B086MBQKH2/ie=UTF8&reviewerType=all_reviews"
        self.assertEqual(self.spider.url_normalizer(input), output)

    def test_url_normalizer_easy_two(self):
        pass

    def test_url_normalizer_medium_one(self):
        pass

    def test_url_normalizer_medium_two(self):
        pass

    def test_url_normalizer_hard_one(self):
        pass

    def test_url_normalizer_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestCallScraper(TestCase):
    def setUp(self) -> None:
        pass

    def test_requester_easy_one(self):
        pass

    def test_requester_easy_two(self):
        pass

    def test_requester_medium_one(self):
        pass

    def test_requester_medium_two(self):
        pass

    def test_requester_hard_one(self):
        pass

    def test_requester_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestCallSentimentAnalyzer(TestCase):
    def setUp(self) -> None:
        pass

    def test_requester_easy_one(self):
        pass

    def test_requester_easy_two(self):
        pass

    def test_requester_medium_one(self):
        pass

    def test_requester_medium_two(self):
        pass

    def test_requester_hard_one(self):
        pass

    def test_requester_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestCleanAttributes(TestCase):
    def setUp(self) -> None:
        pass

    def test_requester_easy_one(self):
        pass

    def test_requester_easy_two(self):
        pass

    def test_requester_medium_one(self):
        pass

    def test_requester_medium_two(self):
        pass

    def test_requester_hard_one(self):
        pass

    def test_requester_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestCallSummarizer(TestCase):
    def setUp(self) -> None:
        pass

    def test_requester_easy_one(self):
        pass

    def test_requester_easy_two(self):
        pass

    def test_requester_medium_one(self):
        pass

    def test_requester_medium_two(self):
        pass

    def test_requester_hard_one(self):
        pass

    def test_requester_hard_two(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None
