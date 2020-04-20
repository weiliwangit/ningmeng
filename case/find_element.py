from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time

class Base():
    def __init__(self, wd):
        self.wd = wd

    def findElement(self,name,method):
        element = WebDriverWait(self.wd,10).until(lambda x: x.find_element(name,method))
        return element

if __name__=="__main__":
    # wd = webdriver.Chrome(r'D:\lw\python\chromedriver.exe')
    # wd.get('https://m.ninmon.me/')
    # Base(wd).findElement("xpath", '//*[@id="app"]/div[2]/div[1]/div[3]/div[1]/div')
    unittest.main()
