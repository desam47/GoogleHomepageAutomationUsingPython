# -*- coding: utf-8 -*-
'''
Created on Jan 15, 2016

@author: Dipesh
'''

import unittest
from selenium import webdriver
 
class GoogleHomepagePrivicyLink(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
        cls.driver.get("http://google.com")
 
    def test_01_EnterSearch(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='_eEe']/a")
        self.search_field.click()
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsr']/a[1]")
        self.search_field.click()
        self.search_field= self.assertIn("Privacy Policy - Privacy & Terms - Google", self.driver.title)
 
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
 
if __name__ == "__main__":
    unittest.main(verbosity=2)