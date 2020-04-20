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


class SearchTest(unittest.TestCase):
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

    def test_search_002(self):
        """测试不登陆时的--发现——会不会出现登陆页面"""
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[4]')
        print('002')
        sub=Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/span')
        assert sub=='登录'
    def test_search_003(self):
        """测试登录过的--发现--页面是否正常"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]')
        print(3)
        text = Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span')
        assert text=='根据《零点超控》推荐'
    def test_search_004(self):
        """测试搜索框是否可以点击和输入"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]')
        print(4)
        time.sleep(2)
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div')
        print(4)
        time.sleep(2)
        Base(self.wd).sendKeys(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div/div/input','朝花夕拾')
    def test_search_005(self):
        """测试搜索取消功能"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]')
        time.sleep(1)
        Base(self.wd).ClickElement(By.CSS_SELECTOR, '#app>div:nth-child(2)>div:nth-child(1)>div.discover-search>div')
        print(5)
        time.sleep(2)
        Base(self.wd).sendKeys(By.CSS_SELECTOR,
                               '#app > div:nth-child(2) > div.search-input > div > div > div > input[type=text]',
                               '朝花夕拾')
        time.sleep(2)
        Base(self.wd).ClickElement(By.CSS_SELECTOR, '#app>div:nth-child(2)>div.search-input>div>span.cancel')
        print(5)
        text = Base(self.wd).text(By.CSS_SELECTOR,
                                  '#app > div:nth-child(2) > div:nth-child(1) > div.van-list > div:nth-child(1) > div:nth-child(1) > div.list-title > span')
        assert text == '根据《零点超控》推荐'
    def test_search_006(self):
        """测试搜索搜索功能"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div')
        time.sleep(2)
        Base(self.wd).sendKeys(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.search-input > div > div > div > input[type=text]', '朝花夕拾')
        time.sleep(2)
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/span[2]')
        all = WebDriverWait(self.wd, 30, 1).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.item-title'))
        text=all[1].text
        print(text)
        try:

            self.wd.find_element_by_xpath("//*[contains(text(),'朝花夕拾')]")
        except:
            return False

    def test_search_007(self):
        """测试阅读页面是否存在"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div')
        print('点击输入框')
        time.sleep(2)
        # Base.(self.wd).sendKeys(By.CSS_SELECTOR,'#app > div:nth-child(2) > div.search-input > div > div > div > input[type=text]')
        Base(self.wd).sendKeys(By.CSS_SELECTOR, '#app > div:nth-child(2) > div.search-input > div > div > div > input[type=text]', '朝花夕拾')
        print('输入')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/span[2]')
        time.sleep(2)
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div/ul[1]/div/li/div/div[2]')
        time.sleep(2)
        text=Base(self.wd).text(By.CSS_SELECTOR,'.author')
        assert text=='鲁迅'
    def test_search_008(self):
        """测试--免费阅读---"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]')
        time.sleep(1)
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div')
        print('点击输入框')
        time.sleep(2)
        Base(self.wd).sendKeys(By.CSS_SELECTOR, '.input-container>input', '朝花夕拾')
        print('输入')
        time.sleep(1)
        # 点击搜索
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/span[2]')
        print('sou')
        time.sleep(2)
        #点击第一个
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/div/ul[1]/div/li/div/div[2]')
        print('one')
        time.sleep(1)
        #点击免费阅读
        Base(self.wd).ClickElement(By.CSS_SELECTOR,'.van-hairline--surround')
        time.sleep(1)
        try:
            text=self.wd.find_element_by_xpath("//*[contains(text(),'螺旋')]")
        except:
            return False
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        Base(self.wd).ClickElement(By.CSS_SELECTOR,'#app > div:nth-child(2) > div > div.chang-chapter > span:nth-child(2)')
        self.wd.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(2)
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        Base(self.wd).ClickElement(By.CSS_SELECTOR,
                                   '#app > div:nth-child(2) > div > div.chang-chapter > span:nth-child(1)')
    def test_search_009(self):
         """测试--搜索历史--"""
         Login(self.wd).test_login002("13253728975", "123456w")
         Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]')
         time.sleep(1)
         Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div')
         print('点击输入框')
         time.sleep(2)
         Base(self.wd).sendKeys(By.CSS_SELECTOR, '.input-container>input', '朝花夕拾')
         print('输入')
         time.sleep(1)
         # 点击搜索
         Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/span[2]')
         print('sou')
         time.sleep(2)
         Base(self.wd).ClickElement(By.CSS_SELECTOR, '#app div:nth-child(2) > div.search-input > div > span.cancel')
         time.sleep(1)
         Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div')
         # time.sleep(4)
         all = WebDriverWait(self.wd, 30, 1).until(lambda x: x.find_elements(By.CSS_SELECTOR, 'div.search-history > ul > li:nth-child(1) > span'))
         all[0].click()
         time.sleep(1)
         text = Base(self.wd).text(By.CSS_SELECTOR, '.author')
         assert text=='鲁迅'
    def tearDown(self):
        self.wd.quit()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()