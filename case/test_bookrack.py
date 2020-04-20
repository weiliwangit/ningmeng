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


class BookrackTest(unittest.TestCase):
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
            word = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[3]/div')
            assert word == "完本"
        except:
            word2 = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
            assert word2 == "男生"

    def test_bookra_002(self):
        """测试未登录时书架会不会显示登陆页面"""
        Base(self.wd).ClickElement(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.van-hairline--top-bottom.van-tabbar.van-tabbar--fixed > div:nth-child(1)')
        tex=Base(self.wd).text(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.container > div.login > span')
        print(2)
        assert tex=='登录'
    def test_bookra_003(self):
        """检测是否显示书架页面1"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.CSS_SELECTOR,
                                   '#app > div:nth-child(2) > div.van-hairline--top-bottom.van-tabbar.van-tabbar--fixed > div:nth-child(1)')
        time.sleep(2)
        self.wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        cc=Base(self.wd).exct(By.CSS_SELECTOR,'#app > div:nth-child(2) > div:nth-child(1) > div.bookCon > div:nth-child(10) > div')
        assert  cc==True
    def test_bookra_004(self):
        """检测是否显示书架页面2"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.CSS_SELECTOR,
                                   '#app > div:nth-child(2) > div.van-hairline--top-bottom.van-tabbar.van-tabbar--fixed > div:nth-child(1)')
        time.sleep(2)
        tex=Base(self.wd).FindElement(By.CSS_SELECTOR,
                                      '#app > div:nth-child(2) > div:nth-child(1) > div.van-nav-bar.van-hairline--bottom > div.van-nav-bar__title.van-ellipsis')
        cc=tex.text
        assert cc =="我的书架"
    def test_bookra_005(self):
        """检测书架上的书是否可以点进去"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.van-hairline--top-bottom.van-tabbar.van-tabbar--fixed > div:nth-child(1)')
        time.sleep(2)
        all=Base(self.wd).FindElements(By.CSS_SELECTOR,'.imgCon')
        s=len(all)
        if not s :
            return
        else:
            all[0].click()
            time.sleep(2)
        self.wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        tex=Base(self.wd).text(By.CSS_SELECTOR,'#app > div:nth-child(2) > div > div.chang-chapter > span:nth-child(2)')
        print(tex)
        assert tex=='下一章'

    def tearDown(self):
        self.wd.quit()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()