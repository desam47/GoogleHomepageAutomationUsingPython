# -*- coding: utf-8 -*-
'''
Created on Jan 15, 2016

@author: Dipesh
'''

import unittest
from selenium import webdriver
 
class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
        cls.driver.get("http://google.com")
 
    def test_01_EnterSearch(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Phones")
        self.search_field.submit()
        self.button = self.driver.find_element_by_name("btnG")
        self.button.click()
        self.search_field= self.assertIn("Phones - Google Search", self.driver.title)
 
    def test_02_BackToGoogleHomePage(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Pant")
        self.search_field.submit()
        self.button = self.driver.find_element_by_xpath(".//*[@id='sblsbb']/button")
        self.button.click()
        self.button = self.driver.find_element_by_xpath(".//*[@id='logo']/img")
        self.button.click()
        self.search_field= self.assertIn("Google", self.driver.title)
 
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
 
if __name__ == "__main__":
    unittest.main(verbosity=2)