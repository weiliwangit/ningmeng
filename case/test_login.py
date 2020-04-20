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


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        # 每个测试用例都会执行
        self.wd = webdriver.Chrome(r'D:\lw\python\chromedriver.exe')
        self.wd.get('https://m.ninmon.me/#/login')
    def test_login001(self):
        """测试登陆页面是否正常显示1"""
        dom=Base(self.wd).exct(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div:nth-child(1) > div.item-body > div > div')
        assert dom==True
    def test_login002(self):
        """测试登陆页面是否正常2"""
        tex=Base(self.wd).text(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div.login')
        assert tex=="登录"
    def test_login003(self):
        """测试无密码手机号状态登录"""
        Base(self.wd).ClickElement(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div.login > span')
        time.sleep(2)
        dom=Base(self.wd).exct(By.CSS_SELECTOR,'body > div.van-toast.van-toast--middle > div')
        assert dom==True
    def test_login004(self):
        """测试密码框为空登录"""
        Base(self.wd).sendKeys(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div:nth-child(1) > div.item-body > div > div > input[type=number]','13253728975')
        time.sleep(2)
        Base(self.wd).ClickElement(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.container > div.login > span')
        time.sleep(2)
        dom = Base(self.wd).exct(By.CSS_SELECTOR, 'body > div.van-toast.van-toast--middle > div')
        assert dom == True
    def test_login005(self):
        """测试手机输入框为空时"""
        Base(self.wd).sendKeys(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div:nth-child(2) > div.item-body > div > div > input[type=password]','123456w')
        time.sleep(1)
        Base(self.wd).ClickElement(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.container > div.login > span')
        time.sleep(2)
        dom = Base(self.wd).exct(By.CSS_SELECTOR, 'body > div.van-toast.van-toast--middle > div')
        assert dom == True
    def test_login006(self):
        """测试手机号输入错误"""
        """目前登录体验不好"""
        Base(self.wd).sendKeys(By.CSS_SELECTOR,
                               '#app > div:nth-child(2) > div.container > div:nth-child(1) > div.item-body > div > div > input[type=number]',
                               '133253728975')
        time.sleep(1)
        Base(self.wd).sendKeys(By.CSS_SELECTOR,
                               '#app > div:nth-child(2) > div.container > div:nth-child(2) > div.item-body > div > div > input[type=password]',
                               '123456w')
        Base(self.wd).ClickElement(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.container > div.login > span')
        time.sleep(2)
        dom = Base(self.wd).exct(By.CSS_SELECTOR, 'body > div.van-toast.van-toast--middle > div')
        assert dom == True
    def test_login007(self):
        """测试手机号输入错误"""
        """目前登录体验不好"""
        Base(self.wd).sendKeys(By.CSS_SELECTOR,
                               '#app > div:nth-child(2) > div.container > div:nth-child(1) > div.item-body > div > div > input[type=number]',
                               '13253728975')
        time.sleep(1)
        Base(self.wd).sendKeys(By.CSS_SELECTOR,
                               '#app > div:nth-child(2) > div.container > div:nth-child(2) > div.item-body > div > div > input[type=password]',
                               '123456')
        Base(self.wd).ClickElement(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.container > div.login > span')
        time.sleep(2)
        dom = Base(self.wd).exct(By.CSS_SELECTOR, 'body > div.van-toast.van-toast--middle > div')
        assert dom == True
    def tearDown(self):
        self.wd.quit()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()