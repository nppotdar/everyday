#! /usr/local/bin/python


SMTPserver = 'smtp.mail.drexel.edu'
sender =     'npp34@drexel.edu'

USERNAME = "npp34"
PASSWORD = ""

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEText import MIMEText



def mail(directory):
    subject="[ CS 260 ][ Grade ][ REVIEW ] - Homework 2"
    i = 0
    for root, dirs, filenames in os.walk(directory):
        for f in filenames:
                content= open(os.path.join(root,f) ).read()
                destination = []
                rex = re.compile("(.*).t2")
                destination.append(rex.search(f).groups()[0] + "@drexel.edu")
                print "Mailing to Destination " , rex.search(f).groups()[0]
                try:
                    msg = MIMEText(content, text_subtype)
                    msg['Subject']= subject
                    msg['From'] = "TA Nagesh<npp34@drexel.edu>" # some SMTP servers will do this automatically, not all

                    conn = SMTP(SMTPserver)
                    conn.set_debuglevel(False)
                    conn.login(USERNAME, PASSWORD)
                    try:
                        conn.sendmail(sender, destination, msg.as_string())
                    finally:
                        conn.close()

                except Exception, exc:
                    sys.exit( "mail failed; %s" % str(exc) ) # give a error message

mail("./stack/t2/reviews/")
