import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

# Reading the Excel file
df = pd.read_excel("C:\\Users\\Yatharth Rai\\Desktop\\Book4.xlsx")


# Grabbing the "Electric Range" column as our key numeric buddy!
price = df["Electric Range"]

# Dropping missing values
df = df.dropna()

# Time for some visuals! Starting with a histogram of electric ranges.
plt.figure(figsize=(8, 4))
sns.histplot(df['Electric Range'], kde=False, bins=30, color='skyblue')
plt.title('Histogram of Electric Ranges')
plt.xlabel('Frequency')
plt.ylabel('Electric Range (miles)')
plt.tight_layout()
plt.show()

# Now, a bar plot for average range by vehicle type—looking good!
plt.figure(figsize=(6, 4))
ax = sns.barplot(x='Electric Vehicle Type', y='Electric Range', hue='Electric Vehicle Type', data=df, estimator=np.mean, palette='muted')
ax.legend_.remove()
plt.title('Average Electric Range by Vehicle Type')
plt.ylabel('Average Range (miles)')
plt.tight_layout()
plt.show()


# Boxplot time—let’s see range spread by vehicle type!
plt.figure(figsize=(10, 6))
ax = sns.boxplot(x='Electric Vehicle Type', y='Electric Range', hue='Electric Vehicle Type', data=df, palette='Set3')
ax.legend_.remove()
plt.title('Boxplot: Electric Range by Vehicle Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# New! Let’s add a line plot—how’s electric range changed over the years?
plt.figure(figsize=(8, 5))
sns.lineplot(x='Model Year', y='Electric Range', data=df, marker='o')
plt.title('Trend of Electric Range Over Model Years')
plt.xlabel('Model Year')
plt.ylabel('Electric Range (miles)')
plt.grid(True)
plt.tight_layout()
plt.show()

