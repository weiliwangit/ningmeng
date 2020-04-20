# -- coding: utf-8 --

# 这里面不需要懂，只需要复制粘贴就行，传递参数就可以了，唯一传递的参数是report_dir='../report'，这是report一个文件夹，他的下面最好只有result.html
# 不要问为啥，我也不知道，如果有其他文件在，会不会出意外俺也不知道，反正复制我的按我的要求最省事

import os
import smtplib#发送邮件模板
import datetime #标题时间，用不用无所谓
from email.mime.text import MIMEText#定义邮件内容
from email.header import Header#定义邮件标题
from email.mime.multipart import MIMEMultipart#用于传送附件
import HTMLTestRunner
import unittest
import time

#存放报告的位置
report_dir= 'report'



def Latest_Report(report_dir):
    #os.listdir()方法用于返回指定文件夹包含文件或文件名字列表
    lists=os.listdir(report_dir)
    #按照时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
    file=os.path.join(report_dir,lists[-1])
    return  file


class sendSmptEmail():
    def send_email(Latest_Report):
        #读取最新测试报告的内容
        with open(Latest_Report,'rb') as e:
            mail_content=e.read()
            e.close()

            smtpserver = 'smtp.qq.com'  # 发送邮件所用的服务器
            password = 'egvnyusvhhwgdjhh'
            user = '2456323286@qq.com'
            # 发送邮件地址和接收地址
            sender = '2456323286@qq.com'
            receives = ['2456323286@qq.com', '2456323286@qq.com']

            # 定义邮件标题和内容
            # subject = '柠檬测试报告'

            msgRoot = MIMEMultipart()
            msgRoot['subject'] = Header('柠檬测试报告(' + str(datetime.date.today()) + ')', 'utf8')
            # msgRoot['Subject'] = Header(subject, 'utf-8')  # 标题类型
            msgRoot['From'] = sender
            msgRoot['To'] = ','.join(receives)
            # 发送附件
            att = MIMEText(mail_content, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="test_report.html"'  # 定义附件名称
            msgRoot.attach(att)  # 挂起

            smtp = smtplib.SMTP_SSL(smtpserver, 465)  # SSL协议端口号要使用465或994
            smtp.helo(smtpserver)  # HELO向服务器标志用户身份
            smtp.ehlo(smtpserver)  # 服务器返回结果确认
            smtp.login(user, password)

            print('start send Email...')
            smtp.sendmail(sender, receives, msgRoot.as_string())  # 发送地址；邮件接收地址；发送信息
            smtp.quit()
            print('send end...')


if __name__ == '__main__':
    # 我也不知道为啥，总之这是可以复制粘贴的
    test_dir = os.path.dirname(os.path.realpath(__file__))
    start_dir = os.path.join(test_dir, "case")
    discover = unittest.defaultTestLoader.discover(start_dir=start_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)

    report_path = os.path.join(test_dir, "report\\result.html")
    fp=open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'柠檬测试报告',
                                           description=u'柠檬测试描述')

    runner.run(discover)
    fp.close()

    report_dir = './report/'
    sendSmptEmail.send_email(Latest_Report(report_dir))

