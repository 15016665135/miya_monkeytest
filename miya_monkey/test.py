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
d = u2.connect('H5AXHM01S963ECM')
for i in range(1,10000):
    d.click(400, 664)
    sleep(1.5)
    d.press("back")
    sleep(1.5)

