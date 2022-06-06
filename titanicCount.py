# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 08:38:55 2022

@author: gen
"""
import pandas as pd
import re
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
df = pd.read_csv('C:/PycharmProjects/base/titanic.csv', index_col='PassengerId')
df.head()
# Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел
sex_counts = df['Sex'].value_counts()
print('{} {}'.format(sex_counts['male'], sex_counts['female']))
#Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров в процентах 
survived_df = df['Survived']
count_of_survived = survived_df.value_counts()[1]
survived_percentage = 100.0 * count_of_survived / survived_df.value_counts().sum()
print("{:0.2f}".format(survived_percentage))
#Какую долю пассажиры первого класса составляли среди всех пассажиров? Ответ приведите в процентах
pclass_df = df['Pclass']
count_of_first_class_passengers = pclass_df.value_counts()[1]
first_class_percentage = 100.0 * count_of_first_class_passengers / survived_df.value_counts().sum()
print("{:0.2f}".format(first_class_percentage))
#Какое самое популярное женское имя на корабле?
def clean_name(name):
    # First word before comma is a surname
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)

    # get name from braces (if in braces)
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)

    # Removing appeal
    name = re.sub('(Miss\. |Mrs\. |Ms\. )', '', name)

    # Get first left word and removing quotes
    name = name.split(' ')[0].replace('"', '')

    return name


names = df[df['Sex'] == 'female']['Name'].map(clean_name)
name_counts = names.value_counts()
name_counts.head()
print(name_counts.head(1).index.values[0])

