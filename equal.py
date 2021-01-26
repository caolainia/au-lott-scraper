import pandas as pd
import numpy as np
import itertools

df = pd.read_csv('powerball-result.csv')

t = [1,2,3,4,5,6,7]
c3 = list(itertools.combinations(t, 3))
c4 = list(itertools.combinations(t, 4))

equals = 0
for index, row in df.iterrows():
	sdf = df.loc[index+1:,:]
	for index2, row2 in sdf.iterrows():
		if row['num1' ] == row2['num1'] and row['num2'] == row2['num2'] and row['num3'] == row2['num3']:
			print("---------------")
			print(row)
			print(row2)
			equals += 1

print(equals)


def check_exist_equal_on_three(target):
	for index, row in df.iterrows():
		if (target[2] == row['num3'] and target[3] == row['num4'] and target[4] == row['num5']) or (target[3] == row['num4'] and target[4] == row['num5'] and target[5] == row['num6']) or (target[4] == row['num5'] and target[5] == row['num6'] and target[6] == row['num7']) or (target[0] == row['num1'] and target[1] == row['num2'] and target[3] == row['num4']) or (target[0] == row['num1'] and target[1] == row['num2'] and target[5] == row['num6']) or (target[0] == row['num1'] and target[2] == row['num3'] and target[4] == row['num5']) or (target[0] == row['num1'] and target[3] == row['num4'] and target[4] == row['num5']) or (target[0] == row['num1'] and target[3] == row['num4'] and target[5] == row['num6']) or (target[0] == row['num1'] and target[3] == row['num4'] and target[6] == row['num7']) or (target[0] == row['num1'] and target[4] == row['num5'] and target[5] == row['num6']) or (target[0] == row['num1'] and target[4] == row['num5'] and target[6] == row['num7']) or (target[1] == row['num2'] and target[2] == row['num3'] and target[4] == row['num5']) or (target[1] == row['num2'] and target[2] == row['num3'] and target[5] == row['num6']) or (target[1] == row['num2'] and target[2] == row['num3'] and target[6] == row['num7']) or (target[1] == row['num2'] and target[3] == row['num4'] and target[6] == row['num7']):
			print('*************************')
			print('not suitable')
			print(row)