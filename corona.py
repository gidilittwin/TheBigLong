

import requests
import pandas as pd
import io
import datetime
import pylab as plt
import numpy as np
##
res = requests.get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv")
df = pd.read_csv(io.BytesIO(res.content))
df.sort_values(by=df.columns[-1],ascending=False,inplace=True)



days_back = 100

for country, country_df in df.groupby('Country/Region',sort=False):
    timeseries = country_df.sum().transpose().iloc[4:]
    infected = timeseries.values
    dates = list(map(lambda x: datetime.datetime.strptime(x,'%m/%d/%y'),timeseries.index))
    if country=='Korea, South':

        infected = np.asarray(1.0*infected[-days_back:],dtype=np.float32)

        plt.figure()
        plt.subplot(2,1,1)
        color = 'tab:red'
        plt.xlabel('date')
        plt.ylabel('infected log-scale', color=color)
        plt.plot(dates[-days_back:],np.log(infected), color=color)
        plt.title(country)
  
        plt.figure()
        plt.subplot(2,1,1)
        color = 'tab:blue'
        plt.xlabel('date')
        plt.ylabel('infected linear-scale', color=color)
        plt.plot(dates[-days_back:],infected, color=color)
        plt.title(country)

