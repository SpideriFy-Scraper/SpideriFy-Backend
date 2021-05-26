import unittest
from crawler.tests.test_AmazonSpider import *
from crawler.tests.test_AmScrapper import *


def suite():
    suite = unittest.TestSuite()

    # suite.addTest(TestRunSpider('test_run_spider_easy_one'))
    print('Testing: test_requester_easy_one')
    suite.addTest(TestDictToListReviews('test_requester_easy_one'))
    print('Testing: test_sigmoid_easy_one')
    suite.addTest(TestSigmoid('test_sigmoid_easy_one'))
    print('Testing: test_sigmoid_easy_two')
    suite.addTest(TestSigmoid('test_sigmoid_easy_two'))
    print('Testing: test_url_validator_easy_one')
    suite.addTest(TestUrlValidator('test_url_validator_easy_one'))
    print('Testing: test_url_normalizer_easy_one')
    suite.addTest(TestUrlNormalizer('test_url_normalizer_easy_one'))
    print('Testing: test_requester_easy_one')
    suite.addTest(TestCheckLanguageContent('test_requester_easy_one'))
    print('Testing: test_requester_easy_one')
    suite.addTest(TestRequester('test_requester_easy_one'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
