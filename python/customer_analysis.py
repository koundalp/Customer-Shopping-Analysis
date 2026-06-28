# Import
import pandas as pd
import matplotlib.pyplot as plt

# Load
df = pd.read_csv("C:/Users/POONAM/Desktop/project.csv")

# Basic Inspection
print(df.head())
# print(df.info())
# print(df.shape)
# print(df.columns)
# print(df.describe())
# print(df.isnull().sum())

# Analysis

# Revenue by category
# group = df.groupby("Category")["Purchase Amount (USD)"].sum()
# print(group)

# Spending by age group
# bins = [18, 25, 35, 45, 100]
# label = ['18-24', '25-34', '35-44', '45+']
# df['Age group'] = pd.cut(df['Age'], bins=bins, labels=label)
# age = df.groupby('Age group')['Purchase Amount (USD)'].sum()
# print(age)

# Average rating by category
# rate = df.groupby('Category')['Review Rating'].mean()
# print(rate)

# Discount Impact
discount = df.groupby('Discount Applied')['Purchase Amount (USD)'].mean()
print(discount)

# Subscription behavior
# subscription = df.groupby('Subscription Status')['Purchase Amount (USD)'].sum()
# print(subscription)

# Visualizations

# Category sales
# group.plot(kind='bar')
# plt.show()

# Seasonal sales
# season = df.groupby('Season')['Purchase Amount (USD)'].sum()
# season.plot(kind="bar")
# plt.show()

# Payment methods

# method = df['Payment Method'].value_counts()
# method.plot(kind="bar")
# plt.show()
