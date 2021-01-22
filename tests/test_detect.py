#!/usr/bin/env python3
from test import Chrome, ChromeOptions

options = ChromeOptions()
chrome = Chrome(options=options)

chrome.get(url="https://bot.sannysoft.com/")
import pdb;pdb.set_trace()