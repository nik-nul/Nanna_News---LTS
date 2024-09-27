#!/bin/python3

# import sys
# import ast
import os

email_address = "231220103@smail.nju.edu.cn"
# email_password = sys.argv[1]
email_password = os.environ.get("EMAIL_PASSWORD")
smtp_server = "smtp.exmail.qq.com"
smtp_port = 465
# mailing_list = ast.literal_eval(sys.argv[2])
mailing_list = os.environ.get("MAILING_LIST")
today = os.popen("TZ=Asia/Urumqi date '+%F'").read()[:-1]


import email.message

msg = email.message.EmailMessage()
msg["Subject"] = "今日并没有南哪消息哦～"
msg["From"] = "南哪小报编辑部 <231220103@smail.nju.edu.cn>"
# msg["Bcc"] = "231220103@smail.nju.edu.cn, 2486227356@qq.com"
msg["Bcc"] = mailing_list

msg_end = f"""<html><body><p>今日没有消息或消息过少且均没有很强的时效性，故而今日停刊一次。</p><p>感谢您对南哪消息的支持，祝您消息通达，生活愉快。</p><br>南哪小报编辑部<br>{today}<hr/><hr/></body></html>"""


msg.set_content(msg_end, subtype="html")


import smtplib
import time

for _ in range(5):
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(email_address, email_password)
            server.send_message(msg)
    except Exception as e:
        print(e)
        time.sleep(1)
        continue
    break