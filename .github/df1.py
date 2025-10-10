import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

#load our dataframe
df = pd.read_csv("pennData.csv")
pennData = pd.DataFrame(df)

print("-_" * 20)
print("Head of the Dataframe") #first five rows of the dataframe
print(pennData.head())

print("-_" * 20)
print("Tail of the Dataframe") #final five rows of the dataframe
print(pennData.tail())

print("-_" * 20)
print("Summary of the Dataframe") #summary of the dataframe
print(pennData.info())

print("-_" * 20)
print("Statistical Analysis") #mean, standard deviations, min, etc. of dataframe
print(round(pennData.describe())) #Round removes excess zeros

print("-_" * 20)
print("Counts of Students in Pathways") #number of values with key
print(pennData['Pathway'].value_counts())

print("-_" * 20)
print("Average GPA Per Year") #average of the values in one key per another key
print(pennData.groupby('Year')['GPA'].mean()) #SYNTAX MATTERS () then []

print("-_" * 20)
print("Top 3 Students By GPA") #students with highest GPA
print(pennData.sort_values(by = 'GPA', ascending = False).head(3))

print("-_" * 20)
print("Students With GPA > 3.5") #prints student's data who have a GPA higher than 3.5
print(pennData[pennData['GPA']> 3.5])

print("-_" * 20)
print("First Student Data") #first student's data
print(pennData.iloc[0]) #index location 