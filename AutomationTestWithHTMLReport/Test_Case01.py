# -*- coding: utf-8 -*-
'''
Created on Jan 15, 2016

@author: Dipesh
'''

import unittest
from selenium import webdriver
 
class GoogleHomePageElementVerify(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
        cls.driver.get("http://google.com")
        
    def test_01_title(self):
        self.search_field= self.assertIn("Google", self.driver.title)
        #self.assertIn("Google", self.driver.title)
        
    def test_02_logo(self):
        self.search_field = self.driver.find_element_by_id("hplogo")
 
    def test_03_searchpanel(self):
        self.search_field = self.driver.find_element_by_id("lst-ib")
        
    def test_04_googlesearchbutton(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='tsf']/div[2]/div[3]/center/input[1]")
 
    def test_05_iamfeelingluckybutton(self):
        self.search_field = self.driver.find_element_by_name("btnI")
        
    def test_06_Gmail(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='gbw']/div/div/div[1]/div[1]/a")
        
    def test_07_Images(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='gbw']/div/div/div[1]/div[2]/a")
    
    def test_08_GoogleApps(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='gbwa']/div[1]/a")
        
    def test_09_SignInButton(self):
        self.search_field = self.driver.find_element_by_id("gb_70")
        
    def test_10_Advertising(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsl']/a[1]")
      
    def test_11_Business(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsl']/a[2]") 
        
    def test_12_About(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsl']/a[3]")
        
    def test_13_Privacy(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsr']/a[1]")
        
    def test_14_Terms(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsr']/a[2]")
       
    def test_15_Settings(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsettl']")
      
    def test_16_UseGoogledotcomdotnp(self):
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='fsr']/a[3]")
    
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
 
if __name__ == "__main__":
    unittest.main(verbosity=2)