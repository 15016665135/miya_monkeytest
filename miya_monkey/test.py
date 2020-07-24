import argparse
import smtplib
import sys
import uiautomator2 as u2
import subprocess
import urllib.request
import os, re
import logging

# from selenium.common.exceptions import NoSuchElementException

from miya_monkey.miya_mokey.applog import mklog
import logging.config
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
d = u2.connect('127.0.0.1:62001')
command1 = 'adb shell am start -n com.airlive.miya/com.airlive.miya.MainActivity'
os.popen(command1)
sleep(10)
d.double_click(464, 144)
print("请稍等")
sleep(5)
d.app_stop("com.airlive.miya")