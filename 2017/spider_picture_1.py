#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import requests

if __name__ == "__main__":
	target = 'https://unsplash.com/napi/feeds/home'
	headers = {'Authorization': 'Client-ID d39d4a65cc1788fbed5c41d22891a2c161511014313'}
	req = requests.get(url=target, headers = headers, verify=False)
	print(req.text)

