import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime


def iterate_re(names):
	for tr in names:
		print(tr)
		result = ""
		entry = tr.group()
		rows = entry.split('\n')
		for i in range(len(rows)):
			row = rows[i]
			if 'Thursday' in row:
				date = row.replace('Thursday ', "")
				date_object = datetime.strptime(date, "%d %B %Y")
				formatted_date = date_object.strftime("%d/%m/%Y")
				result += formatted_date
				result += ','
			else:
				if row and "AU" not in row:
					result += row
					result += ','
		result = result[:-1]
		result += "\n"
		file_object.write(result)


file_object = open('powerball-result.csv', 'a')
file_object.write('date,num1,num2,num3,num4,num5,num6,powerball\n')
for year in range(2019, 2022):
	url = "https://australia.national-lottery.com/powerball/results-archive-"
	page = url + str(year)
	r = requests.get(page)
	html = r.content
	soup = BeautifulSoup(html, features="html.parser")
	table= soup.find('table', attrs = {'class': 'powerball'})
	content = table.text
	names = re.finditer(r"Thursday(.|\n)*?AU", content, flags = re.MULTILINE)

	count = 0
	for test in names:
		count += 1

	if count == 0:
		names = re.finditer(r"Thursday(.|\n)*?-", content, flags = re.MULTILINE)
	iterate_re(names)



file_object.close()