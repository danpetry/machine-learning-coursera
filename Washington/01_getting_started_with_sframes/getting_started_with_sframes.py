# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas

# N.B. the below need print() functions to actually print
# TODO - find out why...
df = pandas.read_csv("people-example.csv")
df.describe()       # draw table
df.head()  # draw head of table
df['age'].value_counts('true')  # value counts as a decimal
df['Country']  # gets the 'Country' column
df['age'].mean()  # the mean of a column
df['age'].max()  # the max of a column
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']  # create a new column for the data - a new data attribute. This is called 'feature engineering'

# a couple more transformations. Both of these create new Pandas series with the same size as the original.
df['age'] + 2
df['age'] * df['age']

# applying a function to each entry in one column of a dataset, and replacing that column with the new values
def transform_country(country):
    if country == 'USA':
        return 'United States'
    else:
        return country
        
df['Country'] = df['Country'].apply(transform_country)

print("hello world")
