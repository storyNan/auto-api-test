import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = '1014086123@qq.com'
password = "11009980mghjiayou"
sender = username
receivers = ["18270837983@163.com"]

def sendEmail(report):
	# 设置请求头信息
	msg = MIMEMultipart()
	msg['Subject'] = '接口测试报告'  # 邮件名
	msg['From'] = sender
	msg['To'] = receivers
	#发送邮件
	client = smtplib.SMTP()
	client.connect('smtp.qq.com')
	client.login(username, password)
	client.sendmail(sender, receivers, msg.as_string())
	client.quit()
	print("邮件发送成功，请查看")




