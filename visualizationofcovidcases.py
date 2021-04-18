# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 02:28:29 2021

@author: Mertcan
"""

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt

#run on cell for less computing

cvd = pd.read_csv('covid_data.csv')

cvd['date'] = [dt.datetime.strptime(x, '%Y-%m-%d') for x in cvd['date']]
turkey_cases = cvd.loc[cvd["location"] == "Turkey"]

#set index as a date for easier plots
turkey_cases.set_index('date', inplace = True)

#adding a new column named 'mortality_rate'
turkey_cases['mortality_rate'] = turkey_cases['total_deaths'] / turkey_cases['total_cases']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14,14))

turkey_cases.groupby('location')['new_cases'].plot(ax=axes[0,0], legend=True)
turkey_cases.groupby('location')['new_deaths'].plot(ax=axes[0,1], legend=True)
turkey_cases.groupby('location')['total_cases'].plot(ax=axes[1,0], legend=True)
turkey_cases.groupby('location')['total_deaths'].plot(ax=axes[1,1], legend=True)
axes[0, 0].set_title("New Cases")
axes[0, 1].set_title("New Deaths")
axes[1, 0].set_title("Total Cases")
axes[1, 1].set_title("Total Deaths")
