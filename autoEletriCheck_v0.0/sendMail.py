﻿#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='872557422@qq.com'    # 发件人邮箱账号
my_pass = 'jirmgalkerbrbaic'              # 发件人邮箱密码
   
    

def sendMail(toSb):
    ret=True
    try:
        msg=MIMEText('Please check your electricity account! Thank you! :)','plain','utf-8')
        msg['From']=formataddr(["ElectriManager",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["Usr",toSb])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="Your Electricity fees is insufficient!"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[toSb,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
