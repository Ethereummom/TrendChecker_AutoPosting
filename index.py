import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
import requests
import mistune


output = 'json'
grant_type = 'authorization_code'
visibility = 0
category_id_list = {}
tags = []

# 실행 시 JSON 파일에서 데이터를 가져와서 저장

def getData():
    with open('tistory.json' , 'r') as f:
        global json_data
        json_data = json.load(f)
        
        global client_id
        client_id = json_data['client_id']
        
        global client_secret
        client_secret = json_data['client_secret']
        
        global code
        code = json_data['code']
        
        global redirect_uri
        redirect_uri = json_data['redirect_uri']
        
        global blogName
        blogName = json_data['blogName']
        
        if checkJsonKey(json_data, 'access_token') == false:
            getToken()
        
        else :
            global access_token
            access_token = json_data['access_token']

#JSON 파일에 키값이 존재하는지 확인
def checkJsonKey(json, key):
    try:
        tmp = json[key]
        print(tmp)
        if "error" in tmp:
            print("Token error")
            return False
        else :
            print("Token Exist")
            return True
    
    except:
        print("토큰 없음")
        return False

#access_token 가져오기
def getToken():
    url = 'https://www.tistory.com/oauth/access_token?'
    data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'code': code,
            'grant_type': grant_type
    }