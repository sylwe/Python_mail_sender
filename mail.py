#!/usr/bin/env python

##### mail sender by Sylwester W.odyga sylwester.w@gmail.com #####

import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

f_time = datetime.now().strftime('%a %d %b @ %H:%M')

toaddr = 'jan.kowalski@domena.pl'    # email adresser
me = 'jacek.placek@domena.pl' # redacted
me2 = 'YouWillBurnInTheHell@domena.pl' # redacted
password = 'pass' # redacted
subject = 'Wezwanie ' + f_time

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = me
msg['To'] = toaddr
msg.preamble = "Test message @ " + f_time
message = "Main body text here"
html = "<html><head></head><body><h1>Title</h1><p>Main body text here</body></html>"
plainText = MIMEText(message, 'plain')
htmlText = MIMEText(html,'html')
msg.attach(plainText)
msg.attach(htmlText)
wiad = """From: devil@domena.pl
To: jan.kowalski@domena.pl
MIME-Version: 1.0
Content-type: text/html
Subject: Wezwanie

zapraszam z komentarzem :)
"""

#try:
s = smtplib.SMTP('localhost',587) #serwer pocztowy i port
s.starttls()
s.login(me,password)
s.sendmail(me2, toaddr, wiad)
s.quit()
#except:
#   print ("Error: unable to send email")