#!/usr/bin/python3
# -*- coding:UTF-8 -*-





from bs4 import BeautifulSoup
import requests,sys

if __name__ == '__main__':
	target = 'http://www.biqukan.com/1_1094/5403177.html'
	req = requests.get(url=target)
	html = req.text
	bf = BeautifulSoup(html)
	texts = bf.find_all('div', class_='showtxt')
	print(texts)



"""
'''
類說明:下載<筆趣看>網小說<一年永恆>
Parameter:
	無
Return:
	無
Modify:
	2017/11/15

'''

class downloader(object):
	
	def __init__(self):
		self.server = 'http://www.biqukan.com/'
		self.target =  'http://www.biqukan.com/1_1094'
		self.name = []	#存放章節名
		self.urls = []	#存放章節鏈接
		self.nums = []	#章節數



	'''
	函數說明:獲取下載鏈接
	Parameter:
		無
	Return:
		無
	Modify:
		2017/11/15
	'''

	def get_download_url(self):
		req = requests.get(url=self.target)
		html = req.text
		div_bf = BeautifulSoup(html)
		div = div_bf.find_all('div', class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]))
		a = a_bf.find_all('a')
		self.nums = len(a[15:])	#刪除不必要的章節,並統計章節數
		for each in a[15:]:
			self.name.append(each.string)
			self.urls.append(self.server + each.get('href'))


	'''
	函數說明:獲取章節內容
	Parameter:
		target - 下載連接(string)
	Returns:
		texts - 章節內容(string)
	Modify:
		2017/11/15
	'''

	def get_contents(self,target):
		req = requests.get(url = target)
		html = req.text
		bf = BeautifulSoap(html)
		texts = bf.find_all('div', class_='showtext')
		texts = texts[0].text.replace('\xa0'*8,'\n\n')
		return texts

	'''
	函數說明:將爬取的文章內容寫入文件
	Parameter:
		name - 章節名稱(string)
		path - 當前路徑下,小說保存名稱(string)
		text - 章節內容(string)
	Return:
		無
	Modify:
		2017/11/15
	'''

	def writer(self, name, path, text):
		writer_flag = True
		with open('/home/shi/Desktop','a', encoding='UTF-8') as f:
			f.write(name + '\n')
			f.writeline(text)
			f.write('\n\n')



if __name__ == '__main__':
	dl = downloader()
	dl.get_download_url()
	print('<一年永恆>開始下載:')
for i in range(dl.nums):
		dl.writer(dl.name[i],'一年永恆.txt', dl.get_contents(dl.urls[i]))
		sys.stdout.write(" 已下載: %.3f %%" % float(i/dl.nums) + '\r')
		sys.stdout.flush()
#	print('<一年永恆>下載完成')
	
"""





