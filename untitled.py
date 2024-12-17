import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example dataset
data = pd.read_csv('Steel_industry_data.csv')
df = pd.DataFrame(data)

# Define a class for IQR-based outlier detection
class IQRDetector:
    def __init__(self, dataset):
        self.dataset = dataset

    def detect_outliers(self):
        outliers = {}
        for column in self.dataset.columns:
            Q1 = np.percentile(self.dataset[column], 25)
            Q3 = np.percentile(self.dataset[column], 75)
            IQR = Q3 - Q1

            # Define bounds for outliers
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Detect outliers
            outliers[column] = self.dataset[(self.dataset[column] < lower_bound) | (self.dataset[column] > upper_bound)][column]

        return outliers

    def plot_outliers(self):
        for column in self.dataset.columns:
            plt.figure(figsize=(6, 4))
            plt.boxplot(self.dataset[column], vert=False, patch_artist=True)
            plt.title(f'Boxplot for {column}')
            plt.xlabel('Values')
            plt.show()

# Create an instance of the class and detect outliers
iqr_detector = IQRDetector(df)
outliers = iqr_detector.detect_outliers()

# Display outliers
print("Detected Outliers:")
for col, outlier_values in outliers.items():
    print(f"{col}: {list(outlier_values)}")

# Plot boxplots to visualize outliers
iqr_detector.plot_outliers()
