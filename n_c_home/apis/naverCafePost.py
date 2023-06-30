from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse, parse_qs

import pandas as pd
import numpy as np
import time
import requests
import pyperclip

def find_css(css_selector):
    return browser.find_element(By.CSS_SELECTOR, css_selector)
def finds_css(css_selector):
    return browser.find_elements(By.CSS_SELECTOR, css_selector)

def find_xpath(xpath):
    return browser.find_element(By.XPATH, xpath)
def finds_xpath(xpath):
    return browser.find_elements(By.XPATH, xpath)

def find_id(e_id):
    return browser.find_element(By.ID, e_id)

def find_className(cn):
    return browser.find_element(By.CLASS_NAME, cn)
def finds_className(cn):
    return browser.find_element(By.CLASS_NAME, cn)

def find_linktext(lt):
    return browser.find_element(By.LINK_TEXT, lt)

# Options Setting
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('no-sandox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1080,800")
options.add_argument('incognito')
# options.add_argument('headless')
# Header Setting
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)