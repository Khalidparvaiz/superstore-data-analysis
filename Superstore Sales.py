import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load CSV file
df = pd.read_csv(r"C:\Users\Khaled\Desktop\Data Analyst\superstore.csv", encoding="latin1")

# Step 2: Remove duplicates
df.drop_duplicates(keep='first', ignore_index=True, inplace=True)

# Step 3: Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Step : Convert 'Ship Date' to datetime format
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Step 4: Drop rows with any NA values
df.dropna(inplace=True)

#Step 5 Clean text columns (strip + title case)
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].str.strip()
    df[col] = df[col].str.title()  


# print(df.isna().sum())       # Missing values count
# print(df.duplicated().sum()) # Duplicate rows count
# print(df.dtypes)   
# print(df.info())

# print(df.describe())

# DATA EXPLORATION

# Set the figure size first
sns.set(rc={'figure.figsize': (15,7)})

# Plot countplot of Sub-Category
plt.figure()  # Start a new figure
sns.countplot(x='Sub-Category', data=df, hue='Sub-Category', palette='Set2', legend=False)
plt.xticks(rotation=60)
plt.title('Count of Sub-Category')
plt.show()


# Best Performing Category
sns.countplot(x='Category', data=df, hue='Category', palette='Set2', legend=False)  # Count of each category
plt.title('Count of Categories')  # Title
plt.xlabel('Category')  # X-axis label
plt.ylabel('Count')     # Y-axis label
plt.show()


# Which customer segment is the most profitable?
df2 = pd.DataFrame(df.groupby(['Segment'])[['Profit']].mean())
df2.reset_index(inplace=True)  

plt.figure(figsize=(8,5))
sns.barplot(data=df2, x='Segment', y='Profit', hue='Segment', palette='Greens', legend=False)
plt.title('Average Profit by Segment')
plt.ylabel('Average Profit')
plt.xlabel('Segment')
plt.show

# Which is the preferred Ship Mode?
# Taking subset and grouping

# Subset and group by 'Ship Mode'
df_stackb = df[['Ship Mode', 'Sales', 'Profit']]
df_stackb = df_stackb.groupby('Ship Mode').sum().reset_index()

# Plotting
plt.figure(figsize=(10,6))

plt.bar(x=df_stackb['Ship Mode'], height=df_stackb['Sales'], color='skyblue', label='Sales')
plt.bar(x=df_stackb['Ship Mode'], height=df_stackb['Profit'], bottom=df_stackb['Sales'], color='green', label='Profit')

plt.title("Sales & Profit Across Ship Modes", fontsize=20, pad=20)
plt.xlabel('Ship Mode')
plt.ylabel('Amount')
plt.legend()
plt.show()

#  Customer Regional Analysis
# Group the data by 'Region' and calculate the total profit for each region
region_analysis = pd.DataFrame(df.groupby(['Region'])['Profit'].sum().reset_index())

# Display the resulting DataFrame
region_analysis

# Set the figure size
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0', '#ffb3e6']

plt.figure(figsize=(8,8))
plt.pie(region_analysis['Profit'], 
        labels=region_analysis['Region'], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors[:len(region_analysis)])  # Slice colors to match number of regions

plt.title('Profit Distribution by Region')
plt.axis('equal')
plt.show()