import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("storesales.csv")

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Remove rows with missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Check the cleaned dataframe
print(df.head())

# Summary statistics
print(df.describe())

# Visualize sales over time
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['Sales'], color='b')
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
