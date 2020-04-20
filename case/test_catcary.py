from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from case.Login import Login
from case.find import Base
import unittest
import time
from case.find import Base




# Base(wd)
# FindElement(self,name,method):单纯查找元素
# ClickElement(self,name,method):元素已经找到，输入元素就执行了点击事件
# text(self,name,method):元素已经找到，输入元素就执行了text
# sendKeys(self, name,method, text):元素已经找到，输入元素就执行了sendkeys
# clear(self, name,method):元素已经找到，输入元素就执行了clear
# back(self)

# Login(wd).test_login001()测试登录页面是否正常显示,直接调用就行
# Login(wd).test_login002("13253728975","123456w")
# wd.quit()




class CatcaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        # 每个测试用例都会执行
        self.wd = webdriver.Chrome(r'D:\lw\python\chromedriver.exe')
        self.wd.get('https://m.ninmon.me/')

    def test_index_001(self):
        """测试首页是否正常显示"""
        try:
            word=Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[3]/div[3]/div')
            assert word=="完本"
        except:
            word2=Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
            assert word2 == "男生"
    def test_catcary_004(self):
        """测试不登陆时--分类--顶部分类是否显示"""
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]')
        time.sleep(2)
        ns=Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/span')
        assert ns=='女生'

    def test_catcary_005(self):
        """测试不登陆时--分类--顶部分类点击事件"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]')
        time.sleep(2)
        all = WebDriverWait(self.wd, 30, 1).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.van-tab'))
        s=len(all)
        print(all[0].text)
        print(all[1].text)
        print(all[2].text)
        print(s)
        for i in range(s):
            print(all[i].text)
            all[i].click
            time.sleep(5)
    def test_catcary_006(self):
        """测试--分类--下的每个书分类是否可以点击"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]')
        all = WebDriverWait(self.wd, 30, 1).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.name-icon'))
        s = len(all)
        for i in range(3):
            all[i].click()
            time.sleep(2)
            self.wd.back()
            all = WebDriverWait(self.wd, 30, 1).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.name-icon'))
    def tearDown(self):
        self.wd.quit()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()