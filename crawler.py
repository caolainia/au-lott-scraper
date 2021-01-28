import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime


def iterate_re(tr, endtype, starttype):
	result = ""
	entry = tr.group()
	rows = entry.split('\n')
	# print('---------------------------')
	# print(rows)
	pattern_num = re.compile("^[0-9]+$")

	for i in range(len(rows)):
		row = rows[i]
		if row.startswith(starttype):
			date = row.replace(starttype + ' ', "")
			date_object = datetime.strptime(date, "%d %B %Y")
			formatted_date = date_object.strftime("%d/%m/%Y")
			result += formatted_date
			result += ','
		elif pattern_num.match(row):
			result += row
			result += ','
	result = result[:-1] + "\n"
	return result


def scrape_powerball():
	# file_object = open('powerball-result.csv', 'a')
	# file_object.write('date,num1,num2,num3,num4,num5,num6,num7,powerball\n')
	startyear = 2021
	endyear = 2017
	for year in range(startyear, endyear, -1):
		url = "https://australia.national-lottery.com/powerball/results-archive-"
		page = url + str(year)
		r = requests.get(page)
		html = r.content
		soup = BeautifulSoup(html, features="html.parser")
		table = soup.find('table', attrs = {'class': 'powerball'})
		content = table.text
		print(content)
		names = re.finditer(r"Thursday(.|\n)*?\t", content, flags = re.MULTILINE)
		for tr in names:
			file_object.write(iterate_re(tr, '\t', 'Thursday'))
	# file_object.close()

def scrape_xlotto_6():
	file_object = open('xlotto-result-saturday.csv', 'a')
	file_object.write('date,num1,num2,num3,num4,num5,num6,sup1,sup2\n')
	for year in range(2021, 1985, -1):
		url = "https://australia.national-lottery.com/saturday-lotto/results-archive-"
		page = url + str(year)
		r = requests.get(page)
		html = r.content
		soup = BeautifulSoup(html, features="html.parser")
		table= soup.find('table', attrs = {'class': 'lotto'})
		content = table.text
		names = re.finditer(r"Saturday(.|\n)*?\t", content, flags = re.MULTILINE)
		for tr in names:
			file_object.write(iterate_re(tr, '\t', 'Saturday'))
	file_object.close()

def scrape_xlotto_1():
	file_object = open('xlotto-result-monday.csv', 'a')
	file_object.write('date,num1,num2,num3,num4,num5,num6,sup1,sup2\n')
	for year in range(2021, 2005, -1):
		url = "https://australia.national-lottery.com/monday-lotto/results-archive-"
		page = url + str(year)
		r = requests.get(page)
		html = r.content
		soup = BeautifulSoup(html, features="html.parser")
		table= soup.find('table', attrs = {'class': 'lotto'})
		content = table.text
		names = re.finditer(r"Monday(.|\n)*?\t", content, flags = re.MULTILINE)
		for tr in names:
			file_object.write(iterate_re(tr, '\t', 'Monday'))
	file_object.close()

def scrape_xlotto_3():
	file_object = open('xlotto-result-wednesday.csv', 'a')
	file_object.write('date,num1,num2,num3,num4,num5,num6,sup1,sup2\n')
	for year in range(2021, 2005, -1):
		url = "https://australia.national-lottery.com/wednesday-lotto/results-archive-"
		page = url + str(year)
		r = requests.get(page)
		html = r.content
		soup = BeautifulSoup(html, features="html.parser")
		table= soup.find('table', attrs = {'class': 'lotto'})
		content = table.text
		names = re.finditer(r"Wednesday(.|\n)*?\t", content, flags = re.MULTILINE)
		for tr in names:
			file_object.write(iterate_re(tr, '\t', 'Wednesday'))
	file_object.close()

# def combine_filter_lotto(arr1, arr2, arr3, arr4, arr5, arr6):



def main():
    scrape_powerball()

if __name__ == "__main__":
    main()