# -*- coding: utf-8 -*-
"""Sea Level Predictor

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CdpaeqXqwRCuS0hvVxSoEI6vffZHPtim

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

* Use Pandas to import the data from epa-sea-level.csv.
* Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axix.
* Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
Unit tests are written for you under test_module.py.

The boilerplate also includes commands to save and return the image.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

"""Use Pandas to import the data from epa-sea-level.csv."""

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('epa-sea-level.csv')
df.head()

"""Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axix."""

df.plot.scatter('Year', 'CSIRO Adjusted Sea Level')

"""Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050."""

slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

def linreg(_range, slope, intercept=0):
  return [intercept + x * slope for x in _range]

length = 170
_range = range(1880, 1880 + length)

plt.plot(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(_range, linreg(_range, slope, intercept))

"""Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000."""

starting_year = 2000

df_2000s = df[(df['Year'] >= starting_year)]
df_2000s.plot.scatter('Year', 'CSIRO Adjusted Sea Level')

slope, intercept, r, p, se = linregress(df_2000s['Year'], df_2000s['CSIRO Adjusted Sea Level'])

length = 50
_range = range(starting_year, starting_year + length)

plt.plot(df_2000s['Year'], df_2000s['CSIRO Adjusted Sea Level'])
plt.plot(_range, linreg(_range, slope, intercept))

"""The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level."""

import math 

slope, intercept, r, p, se = linregress(df_2000s['Year'], df_2000s['CSIRO Adjusted Sea Level'] / 2.54)

plt.ylabel('Sea Level (inches)')
plt.xlabel('Year')
plt.title("Rise in Sea Level")

plt.plot(_range, linreg(_range, slope, intercept))