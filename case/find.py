from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
import time
class Base():
    def __init__(self,wd):
        self.wd=wd
        # 封装查找元素
    def FindElement(self,name,method):
        try:
            element=WebDriverWait(self.wd,10,1).until(lambda x: x.find_element(name,method))
        except:
            return False
        return element

    def FindElements(self, name, method):
        # try:
        element = WebDriverWait(self.wd, 10, 1).until(lambda x: x.find_elements(name, method))
        # except:
        #     return False
        return element
    # 封装点击事件
    def exct(self,name,method):
        try:
            element=WebDriverWait(self.wd,10,1).until(lambda x: x.find_element(name,method))
            return True
        except:
            return False
    def ClickElement(self,name,method):

        ele=self.FindElement(name,method)
        ele.click()

    #获取文本
    def text(self,name,method):

        ele = self.FindElement(name, method).text
        return ele

    #封装send_keys
    def sendKeys(self, name,method, text):
        ele = self.FindElement(name,method)
        ele.send_keys(text)
    #封装清除事件
    def clear(self, name,method):
        ele = self.FindElement(name,method)
        ele.clear()
    #封装后退
    def back(self):
        self.wd.back()
if __name__ == '__main__':
    unittest.main()
    # wd = webdriver.Chrome(r'D:\lw\python\chromedriver.exe')
    # wd.get('https://m.ninmon.me/')
    # time.sleep(4)
    # wd.quit()