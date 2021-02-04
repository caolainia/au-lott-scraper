import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

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

def scrape_flash_select_powerball():
	f = open("flash-select-powerball.html", 'r')
	df = pd.DataFrame(columns=['num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'powerball'])

	html = f.read()
	names = re.finditer(r"<div class=\"numbers\">.+?PB.+?</div>", html, flags = re.MULTILINE)
	index = 0
	for tr in names:
		entry = tr.group()
		rows = entry.split('\n')
		row = rows[0]

		numbers = re.finditer(r"<span(.|\n)*?au-target-id.*?[0-9]+\">[0-9]{1,2}</span>", row, flags = re.MULTILINE)
		result = []
		for num in numbers:
			n = num.group()
			things = re.compile("<span(.|\n)*?au-target-id.+?>").split(n)
			target = things[2].replace("</span>", "")
			result.append(target)
		
		nums = result[0:7]
		powerball = result[7]
		nums = [int(x) for x in nums]
		nums.sort()
		nums.append(powerball)
		df.loc[index] = nums
		index += 1
	print(df)
	df.to_csv("powerball-flash-result.csv", index=False, mode='a', header=False)
	f.close()

# def combine_filter_lotto(arr1, arr2, arr3, arr4, arr5, arr6):

# def summation(a, b):
# 	result = a + b
# 	# print(result)
# 	if result == 11:
# 		return result
# 		print("123")
# 	else:
# 		print("321")
# 		return 4
# 	print("345")


def strip_comma(text):
	print(text.replace(",", ""))

def main():
    # scrape_flash_select_powerball()
    # n3 = n2 + n1
    d = {}

    d["a"] = {"b": [ {1:"n"} , {2:["c", "b"]} ] }
    d["jose"] = ["amazon", "taobao", "alibaba"]

    print(d["a"]["b"][1][2][1])



if __name__ == "__main__":
    main()