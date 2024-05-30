# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


# Load four datasets
monthly_data_1 = pd.read_csv("monthly_data.csv")

three_hour_data_1 = pd.read_csv("three_hour_data.csv")



monthly_data_1['DATE'] = pd.to_datetime(monthly_data_1['DATE'])
three_hour_data_1['DATE'] = pd.to_datetime(three_hour_data_1['DATE'])


plt.figure(figsize=(10, 6))
sns.histplot(monthly_data_1['MonthlyMeanTemperature'], bins=20, kde=True)
plt.title('Distribution of Monthly Mean Temperature - Dataset 1')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()


result_1 = seasonal_decompose(monthly_data_1['MonthlyMeanTemperature'], model='additive', period=12)
result_1.plot()
plt.title('Seasonal Decomposition - Dataset 1')
plt.show()

'''
result_2 = seasonal_decompose(monthly_data_2['MonthlyMeanTemperature'], model='additive', period=12)
result_2.plot()
plt.title('Seasonal Decomposition - Dataset 2')
plt.show()'''


heatwave_threshold_1 = monthly_data_1['MonthlyMaximumTemperature'].quantile(0.9)
heatwave_events_1 = monthly_data_1[monthly_data_1['MonthlyMaximumTemperature'] > heatwave_threshold_1]
'''
heatwave_threshold_2 = monthly_data_2['MonthlyMaximumTemperature'].quantile(0.9)
heatwave_events_2 = monthly_data_2[monthly_data_2['MonthlyMaximumTemperature'] > heatwave_threshold_2]
'''

