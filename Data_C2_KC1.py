import requests
import pandas as pd
import json

## Pulling data from weather api and putting data into a pandas dataframe

baseurl = "http://api.weatherapi.com/v1/current.json?key=e57b4067a4df4bd980d24725231306&q=Jeffersonville&aqi=no"

r = requests.get(baseurl)

weatherjson = r.json()


df = pd.read_json(json.dumps(weatherjson))

## Find and print TWO descriptive statistics about your data

categories = df['current'].value_counts()
print(categories)


null_sum = df.isnull().sum()
print(null_sum)

## doing a pandas query of the data
print(df.query('current.isna()'))


# Select and print the SECOND AND THIRD columns of your data frame. I printed first and second because there isn't a third column

print(df.iloc[:, [0, 1]])


# Select and print the FIRST 4 rows of you data frame.

print(df.head(4))










