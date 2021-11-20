# ส่งเมลล์ภาษาไทย 
import smtplib # ไลบรารี่สำหรับส่งเมล์
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี\nHello\n"):

	myemail = '4qch88@gmail.com'
	mypassword = '4qch88&2021'
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'ระบบส่งเมล์'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP('smtp.gmail.com:587')# โดเมน email
	s.ehlo()
	s.starttls()

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()

	print('ส่งแล้ว')


# ###########Start sending#############
subject = 'ทดสอบอีเมล์'

msg = '''สวัสดีครับ

ทดสอบส่งข้อความ 

เขียนเว็บไซต์ 4QWC
'''

sendthai('4qch88@gmail.com,hs4qwc@gmail.com',subject,msg)

# # หากต้องการส่งหลายคนสามารถใส่คอมม่าใน string ได้เลย เช่น 'loongTu1@gmail.com,loongTu2@gmail.com'


# '''
# -------------------------
# ตั้งค่าให้เป็นสีเขียวก่อนส่ง แล้วลองรีเฟรชดู ( on )
# https://myaccount.google.com/lesssecureapps
# '''