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

class BookCtyTest(unittest.TestCase):
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


    def test_BookCty_002(self):
        """测试--书成--男生"""
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
        print("002")
        text= Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[3]/div')
        assert text == "榜单"
    def test_BookCty_003(self):
        """测试--书成--男生模块--都市页面是否正常--"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[2]')
        print('003')
        text = Base(self.wd).text(By.CSS_SELECTOR, '.van-nav-bar__title van-ellipsis')
        assert text=='都市'

    def test_BookCty_004(self):
        """测试--书成--男生模块--玄幻页面是否正常--"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[1]/img')
        print('004')
        text = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]')
        assert text == '玄幻'

    def test_BookCty_005(self):
        """测试--书成--男生模块--榜单页面是否正常--"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[3]/img')
        print('005')
        text = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]')
        print(text)
        assert text == '榜单'
    def test_BookCty_006(self):
        """测试--书成--男生模块--日更页面是否正常--"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[4]/img')
        print('006')
        text = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]')
        print(text)
        assert text == '日更'
    def test_BookCty_007(self):
        """测试--书成--女生"""
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/span')
        print('007')
        text= Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[2]/div')
        assert text == "古代言情"
    def test_BookCty_008(self):
        """测试--书成--女生模块--现代言情页面是否正常--"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/span')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[1]/img')
        print('008')
        text = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]')
        print(text)
        assert text == '现代言情'
    def test_BookCty_009(self):
        """测试--书成--女生模块--古代言情页面是否正常--"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/span')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[2]/img')
        print('009')
        text = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]')
        print(text)
        assert text == '古代言情'
    def test_BookCty_010(self):
        """测试--书成--女生模块--榜单页面是否正常--"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/span')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[3]/img')
        print('010')
        # time.sleep(2)
        text = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]')
        print(text)
        assert text == '榜单'
    def test_BookCty_011(self):
        """测试--书成--出版"""
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[4]/span')
        print('011')
        text = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[4]/div[1]/div/div[1]/div[1]')
        time.sleep(1)
        assert text == "小编热推"
    def tearDown(self):
        self.wd.quit()

    @classmethod
    def tearDownClass(cls):
        pass
if __name__ == '__main__':
    unittest.main()