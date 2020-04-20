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


class MainTest(unittest.TestCase):
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
            print('走到了try')
            assert word=="完本"
        except:
            word2=Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/span')
            print('走到了except')
            assert word2 == "男生"
    def test_login_002(self):
        """测试登录页面是否正常显示"""
        Login(self.wd).test_login001()

    def test_login_003(self):
        """测试登录页面输入框是否正常"""
        Login(self.wd).test_login002("13253728975","123456w")

    def test_main_004(self):
        """测试--‘我的’--页面是否能正常显示"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[5]')
        try:
            print(4.11)
            phoneNum=Base(self.wd).text(By.XPATH,
                                       '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/span[1]')
            js="$('.user-title-top>input').text('')"
            cc=self.wd.execute_script(js)
            print(cc)
            assert phoneNum=="13253728975"
            print(4.12)
        except:
            print(4.2)
            fx = Base(self.wd).text(By.XPATH,
                                          '//*[@id="app"]/div[2]/div[1]/div[3]/div[1]/div/span')
            assert fx=="我要分享"
    def test_main_005(self):
        "测试--‘我的’--页面底部显示"
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]')
        # 移动到页面底部
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        try:
            print(5.11)
            yijian=Base(self.wd).text(By.XPATH,
                                       '//*[@id="app"]/div[2]/div[1]/div[3]/div[6]/div/span')
            assert yijian=="意见反馈"
            print(5.12)
        except:
            print(5.2)
            lishi=Base(self.wd).text(By.XPATH,
                                       '//*[@id="app"]/div[2]/div[1]/div[3]/div[3]/div/span')
            assert lishi=="阅读历史"
    def test_main_006(self):
        """测试底部——意见反馈,阅读历史等--点击功能"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]')
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        all = WebDriverWait(self.wd, 30, 1).until(lambda x: x.find_elements(By.CSS_SELECTOR,'.van-cell__title'))
        time.sleep(2)
        s=len(all)
        for i in range(s-1):
                self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(2)
                all[i].click()
                time.sleep(2)
                self.wd.back()  # 点完之后返回
                # 重新获取一次元素
                all=self.wd.find_elements_by_css_selector('.van-cell__title')
        print('for过了')
    def test_main_007(self):
        """测试底部——意见反馈--功能"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]')
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        js = 'document.getElementsByClassName("van-cell__title")[5].click();'
        self.wd.execute_script(js)
        print(7)

        sub=Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[3]/span')
        assert sub=='确认提交'
    def test_main_008(self):
        """测试底部——意见反馈--输入少于10个字"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]')
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print(8.1)
        time.sleep(2)
        js = 'document.getElementsByClassName("van-cell__title")[5].click();'
        self.wd.execute_script(js)
        time.sleep(2)
        Base(self.wd).sendKeys(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div/div/textarea',"你好")
        print(8)
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[3]/span')
        time.sleep(2)
        sub = Base(self.wd).text(By.XPATH, '/html/body/div[2]/div')
        assert sub == '反馈内容不能少于10个字'
    def test_main_009(self):
        """测试底部——意见反馈--输入10个字以上"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]')
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        print(9.1)
        js = 'document.getElementsByClassName("van-cell__title")[5].click();'
        self.wd.execute_script(js)
        time.sleep(2)
        print(9)
        Base(self.wd).sendKeys(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div/div/textarea',"你好你好你好你好你好你好")
        time.sleep(2)
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[3]/span')
        time.sleep(2)
        try:
            self.wd.find_element_by_xpath("//a[contains(text(),'提交成功')]")
        except:
            return False
    def test_main_010(self):
        """测试——我要分享--页面是否正常"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]')
        time.sleep(2)
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[1]/div')
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        print(10)
        copy = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/span[1]')
        print(10.1)
        assert copy=="复制链接"
    def test_main_011(self):
        """测试——我要分享--页面是否可以复制链接和复制推广码"""
        Login(self.wd).test_login002("13253728975", "123456w")
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]')
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[1]/div')
        self.wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        print(11)
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/span[1]')
        time.sleep(2)
        try:
            self.wd.find_element_by_xpath("//*[contains(text(),'复制成功')]")
        except:
            return False
    def tearDown(self):
        self.wd.quit()
    @classmethod
    def tearDownClass(cls):
        pass
if __name__ == '__main__':
    unittest.main()
