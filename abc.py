#Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load theana dataset and print the data
data = pd.read_csv("Steel_industry_data.csv")
print(data.head())

#Considering one specific column
lag_power_factor = data["Lagging_Current_Power_Factor"]
print(lag_power_factor)

#Plot a boxplot to view how the data is speard
plt.boxplot(lag_power_factor, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# Add labels and title
plt.title("Boxplot of the Dataset")
plt.xlabel("Values")

#Show the plot
plt.show()

#For finding the quantile of that particular column, we use numpy function
lag_power_factor_quantile = np.quantile(lag_power_factor,[0.25,0.50,0.75])
print(lag_power_factor_quantile)

#Visualisation form of the quantiles
#vert= makes the plot verticle, can be removed if we dont want that
#patch_artist: customisation of the color
plt.boxplot(lag_power_factor_quantile, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# Add labels and title
plt.title("Boxplot of the Dataset with quantiles")
plt.xlabel("Values")

# Show the plot
plt.show()