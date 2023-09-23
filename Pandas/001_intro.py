
# Pandas is a popular Python library for data manipulation and analysis. 

# It provides data structures like DataFrames and Series for working with structured data, 
# supports data input/output from various file formats, offers tools for cleaning and preprocessing data, 
# performs data analysis and statistics, and integrates with data visualization libraries. 

# It's widely used in data science, analytics, and research for its ease of use and powerful data manipulation capabilities.


import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Perform basic operations
print(df.head())  # Display the first few rows of the DataFrame
print(df['Name'])  # Select a specific column
print(df.describe())  # Generate summary statistics


