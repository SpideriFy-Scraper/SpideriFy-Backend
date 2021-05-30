from unittest import TestCase, IsolatedAsyncioTestCase
from crawler.AmScrapper import AmScrapper


class TestRequester(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.testScrapereasy = AmScrapper("someurl", "someurl", headers=None)

    async def test_requester_easy_one(self):
        url = (
            "https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews"
            "/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_review"
        )
        response = await self.testScrapereasy.requester(url)
        self.assertTrue(response.status_code >= 200)

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
            headers=None,
        )
        self.testScrapermeduim = AmScrapper(
            url="https://www.amazonn.comc/HP-Buss-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
            headers=None,
        )

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
        self.testScraper = AmScrapper("someurl", "someurl", headers=None)

    def test_scrap_easy_one(self):
        # self.assertEqual(self.testScraper.scrap(), "crawler\\fixtures\\Scraped-data.json")
        pass

    def test_scrap_easy_two(self):
        pass

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
        self.testScraper = AmScrapper("someurl", "someurl", headers=None)

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
            headers=None,
        )

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
            headers=None,
        )

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
            headers=None,
        )

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


class TestCheckLanguageContent(TestCase):
    def setUp(self) -> None:
        self.testScrapereasy = AmScrapper("someurl", "fuckyou", headers=None)

    def test_requester_easy_one(self):
        input = {
            "REVIEW #1": {
                "title": "4GB RAM NOT 8GB RAM!",
                "content": "This is NOT an 8GB RAM! It is only 4GB RAM! With that being said, it is advertised as an 8GB RAM, packaging was basically triple boxes, packaged very well! Came with backpack and mouse pad as described. Initial start up was slow, but moving fast now that it\u2019s set up. Only gave 3 stars because the RAM is a significant part in purchasing the right laptop!",
                "date": "Reviewed in the United States on November 26, 2019",
                "variant": None,
                "verified": True,
                "author": "Atara83",
                "rating": 3.0,
            }
        }

        self.assertEqual(
            self.testScrapereasy.check_language_content(input["REVIEW #1"]), False
        )

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
