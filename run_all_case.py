# coding:utf-8
import HTMLTestRunner
import unittest
import os


# 我也不知道为啥，总之这是可以复制粘贴的
test_dir =os.path.dirname(os.path.realpath(__file__))
start_dir=os.path.join(test_dir,"case")
discover = unittest.defaultTestLoader.discover(start_dir=start_dir,
                                               pattern="test*.py",
                                               top_level_dir=None)

report_path=os.path.join(test_dir,"report\\result.html")
runner=HTMLTestRunner.HTMLTestRunner(stream=open(report_path,'wb'),
                                     title=u'柠檬测试报告',
                                     description=u'柠檬测试描述')


runner.run(discover)