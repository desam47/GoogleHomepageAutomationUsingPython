
'''
Created on Jan 15, 2016

@author: Dipesh
'''

import unittest
from Test_Case01 import GoogleHomePageElementVerify
from Test_Case02 import GoogleSearch
from Test_Case03 import ConvertHomepageLanguage
from Test_Case04 import GoogleHomepageGmailLink
from Test_Case05 import GoogleHomepageImagesLink
from Test_Case06 import GoogleHomepageGoogleAppsLink
from Test_Case07 import GoogleHomepageAdvertisingLink
from Test_Case08 import GoogleHomepageBusinessLink
from Test_Case09 import GoogleHomepageAboutLink
#from Test_Case10 import GoogleHomepagePrivicyLink
#from Test_Case11 import GoogleHomepageTermsLink
#from Test_Case12 import GoogleHomepageSettingsLink
import os
import HTMLTestRunner
 
def main():
    search_tests = unittest.TestLoader().loadTestsFromTestCase(GoogleHomePageElementVerify)
    search_tests2 = unittest.TestLoader().loadTestsFromTestCase(GoogleSearch)
    search_tests3 = unittest.TestLoader().loadTestsFromTestCase(ConvertHomepageLanguage)
    search_tests4 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageGmailLink)
    search_tests5 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageImagesLink)
    search_tests6 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageGoogleAppsLink)
    search_tests7 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageAdvertisingLink)
    search_tests8 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageBusinessLink)
    search_tests9 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageAboutLink)   
    #search_tests10 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepagePrivicyLink)
    #search_tests11 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageTermsLink)
    #search_tests12 = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepageSettingsLink)
    
    ## Put them in the Array
    #smoke_tests = unittest.TestSuite([search_tests])
    smoke_tests = unittest.TestSuite([search_tests, search_tests2, search_tests3, search_tests4, search_tests5, search_tests6,search_tests7, search_tests8, search_tests9])
    #smoke_tests = unittest.TestSuite([search_tests, search_tests2, search_tests3, search_tests4, search_tests5, search_tests6,search_tests7, search_tests8, search_tests9, search_tests10, search_tests11, search_tests12 ])
    ## File
    dir = os.getcwd()
    outfile = open(dir + "SmokeTestReport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Smoke Tests')
    runner.run(smoke_tests)
 
if __name__ == "__main__":
    HTMLTestRunner.main()