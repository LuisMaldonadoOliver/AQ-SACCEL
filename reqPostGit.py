#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests


client_id = 'f8924d146e144505afb0'
client_secret = 'f5787e7963b693570817a48d04d25a4c8e8ea530'

code = 'ab950f304feb957ed4a4'

if __name__ == '__main__':
    
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id' : client_id, 'client_secret' : client_secret, 'code' : code}
    headers = {'Accept' : 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        #res = response_json.get('res', [])
        #print(res)
        access_token = response_json['access_token']
        print(access_token)