#!/usr/bin/python3
# -*- coding: UTF-8 -*-


# @Author:	ZHANG Shi
# @Date:	2017/11/26
# @Version:	1.0



import requests


if __name__ == '__main__':
	target = 'http://gitbook.cn'
	req = requests.get(url=target)
	print(req.text)
