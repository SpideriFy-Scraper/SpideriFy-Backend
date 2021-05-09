from unittest import TestCase
from crawler.AmScrapper import AmScrapper


class TestRequester(TestCase):

    def setUp(self) -> None:
        self.testScraper = AmScrapper(
            url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)

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


class TestExtractor(TestCase):

    def setUp(self) -> None:
        self.testScrapereasy = AmScrapper(
            url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)
        self.testScrapermeduim = AmScrapper(
            url="https://www.amazon.comc/HP-Buss-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)

    def test_extractor_easy_one(self):
        self.assertEqual(self.testScrapereasy.extractor(), True)

    def test_extractor_easy_two(self):
        pass

    def test_extractor_medium_one(self):
        self.assertEqual(self.testScrapermeduim.extractor(), True)

    def test_extractor_medium_two(self):
        pass

    def test_extractor_hard_one(self):
        pass

    def test_extractor_hard_2(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestScrap(TestCase):

    def setUp(self) -> None:
        self.testScraper = AmScrapper(
            url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)

    def test_scrap_easy_one(self):
        self.assertEqual(self.testScraper.scrap('dict'), {
            'product_title': '2019 HP 15.6 Inch HD Premium Business Laptop PC, Intel Dual-core i3-7100U, 8GB DDR4 RAM, 1TB HDD, USB 3.1, HDMI, WiFi, Bluetooth, Windows 10, W/ Legendary Computer Backpack & Mouse Pad Bundle',
            'Normalized_URL': 'https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
            'review_#1': 'This is NOT an 8GB RAM! It is only 4GB RAM! With that being said, it is advertised as an 8GB RAM, packaging was basically triple boxes, packaged very well! Came with backpack and mouse pad as described. Initial start up was slow, but moving fast now that it’s set up. Only gave 3 stars because the RAM is a significant part in purchasing the right laptop!',
            'review_#2': "Amazon delivered my order promptly. This laptop bundle came in a solid double packaging, and it comes with a backpack and a mouse pad. I am so amazed by the backpack & mouse pad quality, and I don’t mind the little legendary logo both accessories. I had HP laptops previously and had been pleased with their performance. This one is exceptional for someone who isn't into a lot of gaming and such. I am self employed and I bought this laptop for my work, I only need basic internet browsing and need to do some basic excel reporting, so this computer is perfect for me and at an amazing price, especially it came with bonus accessories.",
            'review_#3': 'I got a faulty laptop from day 1! Before I ordered I made sure to ask the seller if it’s NEW.  Well, I got it and it shuts down every 2 minutes. They offered refund, but I live outside the US and returning this mess will cost me a lot. I thought it was tested/upgraded as stated. How can they missed mines when it shuts off right after start up?  Now I’ve trust issues with purchasing electronics online now.',
            'review_#4': "the box delivered on time and safe.  it was double boxed and packed well. the included laptop bag is good quality and will work well when i need to use it.  i would not buy this laptop for the bag but it is a nice value add. speed and response on this laptop is everything that i was looking for.  set up was easy and came 1/2 charged so i didn't have to immediately plug in. My only concern is battery life.  this is the largest laptop that i have ever had.  i use mainly for school and work.  i don't game or stream a lot of video.  but in the 4 hours that i have had the laptop open today, the battery has already dropped to 25%.  i don't know if that is to be expected with the multiple windows open and the large screen but i don't expect to get 8 hours out of the charge if i am on it.  I will keep the power cable near by.  if you are using less, you might make a full day on a charge.",
            'review_#5': 'Nice looking laptop. Very light. Quality is very good and very happy with this purchase. Got this laptop earlier than expected. Highly recommended seller and a product!',
            'review_#6': 'Excellent computer, pretty easy setup, excellent quality backpack. I’d recommend this to anyone looking for a good computer at an affordable price.',
            'review_#7': 'It is an amazing back to school laptop bundle, HP laptop is fast and portable for my school study, and the backpack looks awesome. Overall, it is worth every penny. Thanks',
            'review_#8': 'I have nothing to say because since I opened the Laptop, already was defected.  I was very disappointed that the next day I have to return it.  However, AMAZON, customer services took care this issue.  Amazon has so many customer services over sea like Filipinas that I was very happy how those tech support help you. Since, the price is so good, I decided to re buy it.',
            'review_#9': 'I really needed a good reliable cost effective laptop....and this is perfect.  I read the reviews and check other laptop that were Comparable.  This was exactly what I needed.  I can watch movies, read, you tube play some games... oh and yes work too!!!  Love the quality of it and the ease of using it. I would recommend it!!!',
            'review_#10': 'Nothing to dislike about it. Nice laptop for the price.', 'review_counts': 10})

    def test_scrap_easy_two(self):
        self.assertEqual(self.testScraper.scrap('json'), {
            "product_title": "2019 HP 15.6 Inch HD Premium Business Laptop PC, Intel Dual-core i3-7100U, 8GB DDR4 RAM, 1TB HDD, USB 3.1, HDMI, WiFi, Bluetooth, Windows 10, W/ Legendary Computer Backpack & Mouse Pad Bundle",
            "Normalized_URL": "https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            "review_#1": "This is NOT an 8GB RAM! It is only 4GB RAM! With that being said, it is advertised as an 8GB RAM, packaging was basically triple boxes, packaged very well! Came with backpack and mouse pad as described. Initial start up was slow, but moving fast now that it\u2019s set up. Only gave 3 stars because the RAM is a significant part in purchasing the right laptop!",
            "review_#2": "Amazon delivered my order promptly. This laptop bundle came in a solid double packaging, and it comes with a backpack and a mouse pad. I am so amazed by the backpack & mouse pad quality, and I don\u2019t mind the little legendary logo both accessories. I had HP laptops previously and had been pleased with their performance. This one is exceptional for someone who isn't into a lot of gaming and such. I am self employed and I bought this laptop for my work, I only need basic internet browsing and need to do some basic excel reporting, so this computer is perfect for me and at an amazing price, especially it came with bonus accessories.",
            "review_#3": "I got a faulty laptop from day 1! Before I ordered I made sure to ask the seller if it\u2019s NEW.  Well, I got it and it shuts down every 2 minutes. They offered refund, but I live outside the US and returning this mess will cost me a lot. I thought it was tested/upgraded as stated. How can they missed mines when it shuts off right after start up?  Now I\u2019ve trust issues with purchasing electronics online now.",
            "review_#4": "the box delivered on time and safe.  it was double boxed and packed well. the included laptop bag is good quality and will work well when i need to use it.  i would not buy this laptop for the bag but it is a nice value add. speed and response on this laptop is everything that i was looking for.  set up was easy and came 1/2 charged so i didn't have to immediately plug in. My only concern is battery life.  this is the largest laptop that i have ever had.  i use mainly for school and work.  i don't game or stream a lot of video.  but in the 4 hours that i have had the laptop open today, the battery has already dropped to 25%.  i don't know if that is to be expected with the multiple windows open and the large screen but i don't expect to get 8 hours out of the charge if i am on it.  I will keep the power cable near by.  if you are using less, you might make a full day on a charge.",
            "review_#5": "Nice looking laptop. Very light. Quality is very good and very happy with this purchase. Got this laptop earlier than expected. Highly recommended seller and a product!",
            "review_#6": "Excellent computer, pretty easy setup, excellent quality backpack. I\u2019d recommend this to anyone looking for a good computer at an affordable price.",
            "review_#7": "It is an amazing back to school laptop bundle, HP laptop is fast and portable for my school study, and the backpack looks awesome. Overall, it is worth every penny. Thanks",
            "review_#8": "I have nothing to say because since I opened the Laptop, already was defected.  I was very disappointed that the next day I have to return it.  However, AMAZON, customer services took care this issue.  Amazon has so many customer services over sea like Filipinas that I was very happy how those tech support help you. Since, the price is so good, I decided to re buy it.",
            "review_#9": "I really needed a good reliable cost effective laptop....and this is perfect.  I read the reviews and check other laptop that were Comparable.  This was exactly what I needed.  I can watch movies, read, you tube play some games... oh and yes work too!!!  Love the quality of it and the ease of using it. I would recommend it!!!",
            "review_#10": "Nothing to dislike about it. Nice laptop for the price.", "review_counts": 10}
                         )

    def test_scrap_medium_one(self):
        pass

    def test_scrap_medium_two(self):
        pass

    def test_scrap_hard_one(self):
        pass

    def test_scrap_hard_2(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestJSON(TestCase):

    def setUp(self) -> None:
        self.testScraper = AmScrapper(
            url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)

    def test_json_easy_one(self):
        pass

    def test_json_easy_two(self):
        pass

    def test_json_medium_one(self):
        pass

    def test_json_medium_two(self):
        pass

    def test_json_hard_one(self):
        pass

    def test_json_hard_2(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestCSVFile(TestCase):

    def setUp(self) -> None:
        self.testScraper = AmScrapper(
            url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)

    def test_csv_file_easy_one(self):
        pass

    def test_csv_file_easy_two(self):
        pass

    def test_csv_file_medium_one(self):
        pass

    def test_csv_file_medium_two(self):
        pass

    def test_csv_file_hard_one(self):
        pass

    def test_csv_file_hard_2(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestDict(TestCase):

    def setUp(self) -> None:
        self.testScraper = AmScrapper(
            url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)

    def test_dict_easy_one(self):
        pass

    def test_dict_easy_two(self):
        pass

    def test_dict_medium_one(self):
        pass

    def test_dict_medium_two(self):
        pass

    def test_dict_hard_one(self):
        pass

    def test_dict_hard_2(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None


class TestJSONFile(TestCase):

    def setUp(self) -> None:
        self.testScraper = AmScrapper(
            url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None)

    def test_json_file_easy_one(self):
        pass

    def test_json_file_easy_two(self):
        pass

    def test_json_file_medium_one(self):
        pass

    def test_json_file_medium_two(self):
        pass

    def test_json_file_hard_one(self):
        pass

    def test_json_file_hard_2(self):
        pass

    def tearDown(self) -> None:
        self.testScraper = None
