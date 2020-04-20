from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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


class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        # 每个测试用例都会执行
        self.wd = webdriver.Chrome(r'D:\lw\python\chromedriver.exe')
        self.wd.get('https://m.ninmon.me/#/login')
    def test_register001(self):
        """注册页面就简单测下"""
        """测试注册页面是否正常"""
        Base(self.wd).FindElement(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div:nth-child(4)').click()
        dom=Base(self.wd).exct(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div:nth-child(2) > div.item-body > div > div > button')
        assert dom==True
    def test_register002(self):
        """是否有注册按钮"""
        Base(self.wd).FindElement(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.container > div:nth-child(4)').click()
        time.sleep(2)
        dom = Base(self.wd).exct(By.CSS_SELECTOR,
                                 '#app > div:nth-child(2) > div.container > div.login > span')
        assert dom == True
    def test_register003(self):
        """测试注册页面登录按钮是否存在"""
        Base(self.wd).FindElement(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.container > div:nth-child(4)').click()
        time.sleep(2)
        self.wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        dom = Base(self.wd).exct(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div:nth-child(7)')
        assert dom == True
    def test_register004(self):
        """测试注册页面登录按钮是否可以按"""
        Base(self.wd).FindElement(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.container > div:nth-child(4)').click()
        time.sleep(2)
        self.wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        Base(self.wd).ClickElement(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div:nth-child(7)')
        time.sleep(2)
        tex=Base(self.wd).text(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.van-nav-bar.van-hairline--bottom > div.van-nav-bar__title.van-ellipsis')
        assert tex=='登录'
    def tearDown(self):
        self.wd.quit()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()