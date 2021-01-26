import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime


def iterate_re(tr, endtype, starttype):
	result = ""
	entry = tr.group()
	rows = entry.split('\n')
	print('---------------------------')
	print(rows)
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
	file_object = open('powerball-result.csv', 'a')
	file_object.write('date,num1,num2,num3,num4,num5,num6,num7,powerball\n')
	for year in range(2021, 2017, -1):
		url = "https://australia.national-lottery.com/powerball/results-archive-"
		page = url + str(year)
		r = requests.get(page)
		html = r.content
		soup = BeautifulSoup(html, features="html.parser")
		table= soup.find('table', attrs = {'class': 'powerball'})
		content = table.text

		names = re.finditer(r"Thursday(.|\n)*?\t", content, flags = re.MULTILINE)
		for tr in names:
			file_object.write(iterate_re(tr, '\t', 'Thursday'))

		# count = 0
		# for test in names:
		# 	count += 1

		# if count == 0:
		# 	names = re.finditer(r"Thursday(.|\n)*?AU", content, flags = re.MULTILINE)
		# 	iterate_re(names, "AU")

	file_object.close()

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

		# count = 0
		# for test in names:
		# 	count += 1

		# if count == 0:
		# 	names = re.finditer(r"Thursday(.|\n)*?AU", content, flags = re.MULTILINE)
		# 	iterate_re(names, "AU")

	file_object.close()

def main():
    scrape_xlotto_6()

if __name__ == "__main__":
    main()