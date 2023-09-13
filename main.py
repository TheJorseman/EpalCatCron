import requests
from dotenv import load_dotenv
import os
import logging
load_dotenv()

EPAL_TOKEN = os.getenv('EPAL_TOKEN')

EPAL_IDS = os.getenv('EPAL_IDS')

#'XKjQ4oQJsbXxbLjRUZBJhcWT6kvHvqjd'

def get_headers():
    return {
        'authority': 'cat.epal.gg',
        '_tk_': EPAL_TOKEN,
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.epal.gg',
        'referer': 'https://www.epal.gg/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
        'versionnum': '130',  
    }

def list_vitality(userId):
    url = 'https://cat.epal.gg/vitality/list'
    headers = get_headers()
    data = {
        'userId': userId
    }
    response = requests.post(url, headers=headers, json=data)
    return response

def collect_vitality(vitalityItemId):
    url = 'https://cat.epal.gg/vitality/collectVitality'
    headers = get_headers()
    data = {
        'vitalityItemId': vitalityItemId
    }
    response = requests.post(url, headers=headers, json=data)
    return response

def main():
    user_ids = EPAL_IDS.split(',')    
    for user_id in user_ids:
        items = list_vitality(int(user_id))
        if items.status_code == 200:
            items = items.json()
            list_items = items['content']['vitalityItemList']
            if len(list_items) < 1:
                return
            for item in list_items:
                _id = item['id']
                res = collect_vitality(_id)
                json_response = res.json()
                logging.info(json_response)
        else:
            logging.error(f"Error: {items.status_code}")


if __name__ == '__main__':
    main()

#Jorseman
#userId = 1477589
#Neko
#userId = 1201536
#Hazel
# 1242875
# Dian
# 1540578


