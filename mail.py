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
msg["Subject"] = f"南哪消息 {today}"
msg["From"] = "南哪小报编辑部 <231220103@smail.nju.edu.cn>"
# msg["Bcc"] = "231220103@smail.nju.edu.cn, 2486227356@qq.com"
msg["Bcc"] = mailing_list

msg_end = f"""<html><body><hr><hr/><p>本次消息推送适用 html 格式文本推送。若您的文本渲染异常或渲染效果不佳请及时与我联系。</p><p>RSS 推送已经上线，可见本文顶部的图片。</p><p>html 格式原显示效果请见<a href="https://nik-nul.github.io/news/latest">https://nik-nul.github.io/news/latest</a></p><p>图片可见<a href="https://nik-nul.github.io/news/imgs/latest.png">https://nik-nul.github.io/news/imgs/latest.png</a></p><p>pdf 可见<a href="https://nik-nul.github.io/news/pdfs/latest.pdf">https://nik-nul.github.io/news/pdfs/latest.pdf</a></p><p>今日以后的小报会在<a href="https://nik-nul.github.io/news">https://nik-nul.github.io/news</a>有所记录，有需求可自行下载。</p><p>由于国内网络环境原因，上述链接访问所需时间波动可能较大，但是使用南大校园网环境进行访问一般较为迅速。正确配置代理可确保快速访问。</p><p>若您没有订阅，不再希望订阅，或 pdf 和文本中有不能正确显示的，请回复此邮件，或联系 QQ: <a href="https://qm.qq.com/cgi-bin/qm/qr?k=AieBgJsSLFD_TTuiutNxHxSJpOxRm_7X">2486227356</a>以获得更多帮助。</p><p>感谢您对南哪消息的支持，祝您消息通达，生活愉快。</p><br>南哪小报编辑部<br>{today}<hr/><hr/></body></html>"""

with open("tmp.html", 'r') as ht:
    msg.set_content(ht.read()+msg_end, subtype="html")

with open("./pdfs/latest.pdf", 'rb') as pdf:
    msg.add_attachment(pdf.read(), maintype='application', subtype='pdf', filename=f"南哪消息{today}.pdf")


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