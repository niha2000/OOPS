import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class IQRDetection:
    def __init__(self, filepath, column):
        self.filepath = "Steel_industry_data.csv"
        self.data = None
        self.column = None

    def read_dataset(self):
        #Load the dataset and print the data
        self.data = pd.read_csv(self.filepath)
        print(self.data.head())

    def column1(self):
        #Considering one specific column
        self.column = self.data[self.column]
        print(self.column)

    def plot_column1(self):
        lag_power_factor = self.column()
        #Plot a boxplot to view how the data is speard
        plt.boxplot(self.column, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
        
        # Add labels and title
        plt.title("Boxplot of {self.column}")
        plt.xlabel("Values")
        
        #Show the plot
        plt.show()

    def quantile(self):
        lag_power_factor = self.column()
        #For finding the quantile of that particular column, we use numpy function
        lag_power_factor_quantile = np.quantile(lag_power_factor,[0.25,0.50,0.75])
        print(lag_power_factor_quantile)

    def plot_quantile(self):
        quantiles=self.lag_power_factor_quantile()
        #Visualisation form of the quantiles
        #vert= makes the plot verticle, can be removed if we dont want that
        #patch_artist: customisation of the color
        plt.boxplot(quantiles, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
        
        # Add labels and title
        plt.title("Boxplot of the Dataset with quantiles")
        plt.xlabel("Values")
        
        # Show the plot
        plt.show()

if __name__ == "__main__":
    analysis = IQRDetection("Steel_industry_data.csv","Lagging_Current_Power_Factor")
    analysis.read_dataset()
    analysis.column1()
    analysis.plot_column1()
    analysis.quantile()
    analysis.plot_quantile()

