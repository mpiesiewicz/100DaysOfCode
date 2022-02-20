import csv

import numpy as np
import pandas as pd


# working with csv without pandas
# with open('data.csv') as file:
#     data = file.readlines()
#
# print(data)
#
# with open('data.csv') as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temp = row[1]
#         temp_int = int(temp)
#         temperatures.append(temp_int)
#


def celsius_to_fahrenheit(x):
    x = x * 9 / 5 + 32
    return float(x)


# print(temperatures)

# data = pandas.read_csv('data.csv')
# data_dict = data['temp'].to_list()
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.temp.apply(celsius_to_fahrenheit))

# create dataframe
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [75, 44, 81]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

# squirrel data excercise

sq_data = pd.read_csv('Squirrel_Data.csv')
greys = len(sq_data[sq_data['Primary Fur Color'] == 'Gray'])
blacks = len(sq_data[sq_data['Primary Fur Color'] == 'Black'])
reds = len(sq_data[sq_data['Primary Fur Color'] == 'Cinnamon'])

print(greys)
print(blacks)
print(reds)

data_dict = {
    'Fur Color': ['Gray', 'Cinammon', 'Black'],
    'Count': [greys, blacks, reds]
}

df = pd.DataFrame(data_dict)
df.to_csv('colors.csv')
