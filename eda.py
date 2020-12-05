import pandas as pd
import numpy as np

weather = pd.read_csv('/Users/melissakozak/Desktop/projects/covid_weather/data/en_climate_daily_ON_6158359_2019_P1D.csv')
covid = pd.read_csv('/Users/melissakozak/Desktop/projects/covid_weather/data/COVID19_cases_nov_28_2020.csv')

weather.head()
weather.columns
w = weather.drop(['Longitude (x)', 'Latitude (y)','Climate ID','Data Quality', 'Max Temp (°C)',
       'Max Temp Flag', 'Min Temp (°C)', 'Min Temp Flag', 'Mean Temp Flag', 'Heat Deg Days (°C)', 'Heat Deg Days Flag',
       'Cool Deg Days (°C)', 'Cool Deg Days Flag', 'Total Rain (mm)',
       'Total Rain Flag', 'Total Snow (cm)', 'Total Snow Flag',
       'Total Precip (mm)', 'Total Precip Flag', 'Snow on Grnd (cm)',
       'Snow on Grnd Flag', 'Dir of Max Gust (10s deg)',
       'Dir of Max Gust Flag', 'Spd of Max Gust (km/h)',
       'Spd of Max Gust Flag'], axis=1)
w.columns
w.head()
w.info()


covid.head()
