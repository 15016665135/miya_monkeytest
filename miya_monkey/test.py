# encoding: utf-8
import argparse
import smtplib
import sys
import uiautomator2 as u2
import subprocess
import urllib.request
import os, re
import logging

# from selenium.common.exceptions import NoSuchElementException

from miya_monkey.applog import mklog
import logging.config
from time import sleep
d = u2.connect('48d1c4b995')
for i in range(1,10000):
    d.click(400, 664)
    sleep(1)
    d.press("back")
    print("\r当前点赞数 %d" % i, end="")
    sleep(1.5)

