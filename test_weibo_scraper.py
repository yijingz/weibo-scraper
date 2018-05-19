# -*- coding:utf-8 -*-

"""
 Author: Helixcs
 Site: https://iliangqunru.bitcron.com/
 File: test_weibo_scraper.py
 Time: 5/11/18
"""
import unittest

import weibo_scraper
from weibo_base import *



class TestWeiboScraper(unittest.TestCase):
    def test_get_weibo_tweets(self):
        result = weibo_scraper.get_weibo_tweets(container_id='1076031843242321')
        self.assertIsNotNone(result)

    def test_weibo_base_search_name(self):
        result = weibo_api.search_by_name("Helixcs")
        self.assertIsNotNone(result)

    def test_weibo_getIndex(self):
        result = weibo_api.weibo_getIndex('1843242321')
        self.assertIsNotNone(result)

    def test_is_name_exist(self):
        love_result1 = exist_get_uid(name="嘻红豆")
        print(love_result1)
        self.assertIsNotNone(love_result1)

        love_result2 = exist_get_uid(search_by_name_response='',name='嘻红豆')
        print(love_result2)
        self.assertIsNotNone(love_result2)

        test_result = exist_get_uid(search_by_name_response='',name='暴走大事件')
        print(test_result)
        self.assertIsNotNone(test_result)


if __name__ == '__main__':
    unittest.main()
