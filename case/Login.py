from case.find import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time


# Base(wd)
# FindElement(self,name,method):单纯查找元素
# ClickElement(self,name,method):元素已经找到，输入元素就执行了点击事件
# text(self,name,method):元素已经找到，输入元素就执行了text
# sendKeys(self, name,method, text):元素已经找到，输入元素就执行了sendkeys
# clear(self, name,method):元素已经找到，输入元素就执行了clear
# back(self)

class Login():
    def __init__(self, wd):
        self.wd = wd
    def test_login001(self):
        """测试登陆页面是否正常"""
        # 获取登录按钮
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[1]/div[1]/div[3]')
        print(1)
        btn=Base(self.wd).text(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/span')
        assert btn=="登录"
    def test_login002(self,num,pasword):
        """"测试登陆输入框是否正常"""
        # 获取登录按钮
        Base(self.wd).ClickElement(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[1]/div[3]')
        # # 输入手机号
        Base(self.wd).sendKeys(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/input', num)
        # 输入密码
        Base(self.wd).sendKeys(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/input', pasword)
        # 点击登录
        Base(self.wd).ClickElement(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/span')
        # 是否登录成功
        print(2)
        suc = Base(self.wd).text(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[1]/div[3]')
        assert suc == "退出"
if __name__=="__main__":
    unittest.main()
    # wd = webdriver.Chrome(r'D:\lw\python\chromedriver.exe')
    # wd.get('https://m.gztv.me/#/login')
    # Login(wd).test_login001()
    # # Login(wd).test_login002("13253728975","123456w")
    # wd.quit()