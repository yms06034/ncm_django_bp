from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django. contrib import auth
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from selenium.common.exceptions import *
import urllib.error


from n_c_home.apis.naverCafeApi import naverCafeCrawling
from n_c_home.apis.naverCafeSerachApi import naverCafeSearchCrawling

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text, intersect

import pandas as pd
import numpy as np
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def searchInfo(request):
    return render(request, 'searchInfo.html')

def postWrite(request):
    return render(request, 'postwrite.html')

def naverCafeInfo(request):
    try:
        if request.method == 'POST':
            naver_id = request.POST['naverid']
            naver_pw = request.POST['naverpw']
            nick_name = request.POST['nickname']
            cafe_name = request.POST['cafename']
            cafe_B_name = request.POST['cafeBname']
            keyword = request.POST['keyword']
            comments = request.POST['comments']
            
            comments_list = []
            comments_list.append(comments)
            # NAVER_ID, NAVER_PW, CAFENAME, BORADTITLE, NICKNAME, keyword, COMMENTS
            final_hrefs = naverCafeCrawling(naver_id, naver_pw, cafe_name, cafe_B_name, nick_name, keyword, comments)
            context = {
                'naver_id' : naver_id,
                'naver_pw' : naver_pw,
                'nick_name' : nick_name,
                'cafe_name' : cafe_name,
                'cafe_B_name' : cafe_B_name,
                'keyword' : keyword,
                'comments' : comments_list,
                'final_hrefs' : final_hrefs,
            }
    except NoSuchWindowException as n:
        context = {
            'error_msg' : "크롤링에 실패하였습니다. 다시 시도해주세요",
        }
    except urllib.error.HTTPError as p:
        context = {
            'error_msg' : "크롤링에 실패하였습니다. 다시 시도해주세요",
        }
    except WebDriverException as w:
        context = {
            'error_msg' : "크롤링에 실패하였습니다. 다시 시도해주세요",
        }

    return render(request, 'crawling.html', context=context)


def naverCafeSearch(request):
    try:
        if request.method == 'POST':
            naver_id = request.POST['s_naverid']
            naver_pw = request.POST['s_naverpw']
            cafe_name = request.POST['s_cafename']
            nick_name = request.POST['s_nickname']
            keyword = request.POST['s_keyword']
            comments = request.POST['s_comments']
            
            comments_list = []
            comments_list.append(comments)
            # NAVER_ID, NAVER_PW, CAFENAME, NICKNAME, keyword, COMMENTS
            final_hrefs = naverCafeSearchCrawling(naver_id, naver_pw, cafe_name, nick_name, keyword, comments)
            context = {
                'final_hrefs' : final_hrefs
            }
    except NoSuchWindowException as n:
        context = {
            'error_msg' : "크롤링에 실패하였습니다. 다시 시도해주세요",
        }
    except urllib.error.HTTPError as p:
        context = {
            'error_msg' : "크롤링에 실패하였습니다. 다시 시도해주세요",
        }
    except WebDriverException as w:
        context = {
            'error_msg' : "크롤링에 실패하였습니다. 다시 시도해주세요",
        }

    return render(request, 'crawling.html', context=context)

def naverCafePostIdinfo(request):
    if request.method == 'POST':
        naver_id = request.POST['p_naverid']
        naver_pw = request.POST['p_naverpw']