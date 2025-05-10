import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('owid-covid-data.csv')

# Display the first few rows of the dataframe
cols = df.columns

# display rows
rows = df.head()


#missing values
missing_values = df.isnull().sum()

