import requests
import pandas as pd
import numpy as np

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)
pd.set_option('display.max_columns', 100)
json = r.json()

elements_df = pd.DataFrame(json['elements'])
element_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])

print(elements_df)

print(elements_df[['second_name', 'status', 'news']])