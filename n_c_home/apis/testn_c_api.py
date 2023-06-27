from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse, parse_qs

import pandas as pd
import numpy as np
import time
import requests
import pyperclip

def css_finds(css_selector):
    return browser.find_elements(By.CSS_SELECTOR, css_selector)

def css_find(css_selector):
    return browser.find_element(By.CSS_SELECTOR, css_selector)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_xpath(xpath):
    return browser.find_elements(By.XPATH, xpath)

def find_xpath(xpath):
    return browser.find_element(By.XPATH, xpath)

def find_id(id_x):
    return browser.find_element(By.ID, id_x)

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('no-sandox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('incognito')

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)    

# Settings
NAVER_ID = "sjk5838"
NAVER_PW = "rlatjdwls00@K"

CAFENAME = "1motion1"
BORADTITLE = "전체글보기"
NICKNAME = "최고의일베충소정"

keyword = "테스트입니다. 이렇게 적으면 "
COMMENTS = "Test Comments"

# def 1
# Crawling Start

def naverCafeMacro(NAVER_ID, NAVER_PW, CAFENAME, BORADTITLE, NICKNAME, keyword, COMMENTS):
    browser.get("https://nid.naver.com/nidlogin.login")
    browser.implicitly_wait(2)

    input_id = find_id('id')
    input_pw = find_id('pw')

    time.sleep(2)

    pyperclip.copy(NAVER_ID)
    input_id.send_keys(Keys.CONTROL, "v")

    pyperclip.copy(NAVER_PW) 
    input_pw.send_keys(Keys.CONTROL, "v")
    input_pw.send_keys("\n")

    # Not needed when it's headless
    # no_save_btn = find_id('new.dontsave')
    # no_save_btn.click()

    time.sleep(1)

    # def 2
    browser.get(f"https://cafe.naver.com/{CAFENAME}")
    time.sleep(2)

    boardName = browser.find_element(By.LINK_TEXT, f'{BORADTITLE}')

    boardName.click()

    time.sleep(2)

    browser.switch_to.frame("cafe_main")

    browser.find_element(By.XPATH, '//*[@id="listSizeSelectDiv"]/a').click()
    browser.find_element(By.XPATH, '//*[@id="listSizeSelectDiv"]/ul/li[7]/a').click()

    time.sleep(1)

    soup = BS(browser.page_source, "html.parser")
    soup = soup.find_all(class_='article-board m-tcol-c')[1]

    datas = soup.find_all(class_='td_article')
    dates = soup.find_all(class_='td_date')

    a_hrefs = soup.find_all("a")

    # def 3
    post_hrefs = []
    for href in a_hrefs:
        if keyword in href.text:
            post_hrefs.append(href["href"])

    final_hrefs = []

    for href in post_hrefs:
        parsed_url = urlparse(href)
        query_params = parse_qs(parsed_url.query)
        article_id = query_params['articleid'][0]
        club_id = query_params['clubid'][0]
        new_url = f"https://cafe.naver.com/{CAFENAME}?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D{club_id}%2526page%3D1%2526boardtype%3DL%2526articleid%3D{article_id}%2526referrerAllArticles%3Dtrue"

        final_hrefs.append(new_url)

    while len(final_hrefs) == 0:
        # If final_hrefs is an empty list, continue to rotate repeatedly.
        time.sleep(1)
        browser.refresh()
        
        boardName = browser.find_element(By.LINK_TEXT, f'{BORADTITLE}')

        boardName.click()

        time.sleep(2)

        browser.switch_to.frame("cafe_main")

        browser.find_element(By.XPATH, '//*[@id="listSizeSelectDiv"]/a').click()
        browser.find_element(By.XPATH, '//*[@id="listSizeSelectDiv"]/ul/li[7]/a').click()

        time.sleep(1)

        soup = BS(browser.page_source, "html.parser")
        soup = soup.find_all(class_='article-board m-tcol-c')[1]

        datas = soup.find_all(class_='td_article')
        dates = soup.find_all(class_='td_date')

        a_hrefs = soup.find_all("a")

        # def 3
        post_hrefs = []
        for href in a_hrefs:
            if keyword in href.text:
                post_hrefs.append(href["href"])

        final_hrefs = []

        for href in post_hrefs:
            parsed_url = urlparse(href)
            query_params = parse_qs(parsed_url.query)
            article_id = query_params['articleid'][0]
            club_id = query_params['clubid'][0]
            new_url = f"https://cafe.naver.com/{CAFENAME}?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D{club_id}%2526page%3D1%2526boardtype%3DL%2526articleid%3D{article_id}%2526referrerAllArticles%3Dtrue"

            final_hrefs.append(new_url)
        
        soup = BS(browser.page_source, "html.parser")
        soup = soup.find_all(class_='article-board m-tcol-c')[1]

        datas = soup.find_all(class_='td_article')
        dates = soup.find_all(class_='td_date')

        a_hrefs = soup.find_all("a")

        post_hrefs = []
        for href in a_hrefs:
            if keyword in href.text:
                post_hrefs.append(href["href"])

        final_hrefs = []

        for href in post_hrefs:
            parsed_url = urlparse(href)
            query_params = parse_qs(parsed_url.query)
            article_id = query_params['articleid'][0]
            club_id = query_params['clubid'][0]
            new_url = f"https://cafe.naver.com/{CAFENAME}?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D{club_id}%2526page%3D1%2526boardtype%3DL%2526articleid%3D{article_id}%2526referrerAllArticles%3Dtrue"

            final_hrefs.append(new_url)


    cmtnicks = []

    for p_href in final_hrefs:
        browser.get(p_href)
        time.sleep(1)
        browser.switch_to.frame("cafe_main")
        time.sleep(1)
        
        try:
    #         nicksname = browser.find_element(By.CLASS_NAME, 'comment_inbox_name').text
            nickname = NICKNAME
            cmtNicks = browser.find_elements(By.CLASS_NAME, 'comment_nickname')

            if cmtNicks:
                for cmtNick in cmtNicks:
                    cmtnick = cmtNick.text
                    cmtnicks.append(cmtnick)

                if nickname in cmtnicks:
                    # If you have a comment with my nickname, skip to the next page
                    continue
                else:
                    # 내 닉네임으로 댓글이 없는 경우, 댓글 작성
                    time.sleep(1)
                    text_area = browser.find_element(By.CLASS_NAME, 'comment_inbox_text')
                    text_area.click()

                    pyperclip.copy(COMMENTS) 
                    text_area.send_keys(Keys.CONTROL, "v")
                    register_btn = browser.find_element(By.CLASS_NAME, 'btn_register')
                    register_btn.click()
            else:
                # 댓글 작성
                time.sleep(1)
                text_area = browser.find_element(By.CLASS_NAME, 'comment_inbox_text')
                text_area.click()

                pyperclip.copy(COMMENTS) 
                text_area.send_keys(Keys.CONTROL, "v")
                register_btn = browser.find_element(By.CLASS_NAME, 'btn_register')
                register_btn.click()
                
        except NoSuchElementException:
            pass

        cmtnicks.clear()
        
    browser.close()