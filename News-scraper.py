import requests
from fpdf import FPDF
from win32com.client import Dispatch
main_url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=3bcbfbed7065411ba7b0af38aff73e8c' # Enter your API key
open_bbc_page  = requests.get(main_url).json()
articles =  open_bbc_page['articles']
results =[]
f1=open("Desktop\\NEWS.txt",'w')
for i in articles:
	# x=f'''auther:{i['author']}
	# 		  title: {i['title']}\n
	# 		  description: {i['description']}\n
	# 		  url: {i['url']}\n '''
	author=f'''Author: {i['author']}\n'''
	title=f'''Title: {i['title']}\n'''
	description=f'''Description: {i['description']}\n'''
	url = f'''Url: {i['url']}\n'''
	f1.writelines("============================ ########################### ===============================\n")
	f1.writelines("\n")
	f1.writelines(author)
	f1.writelines(title)
	f1.writelines(description)
	f1.writelines(url)
	f1.writelines("\n")
f1.close()

	

