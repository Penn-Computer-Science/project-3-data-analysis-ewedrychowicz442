import pandas as pd
import random
import matplotlib.pyplot as plt

df = pd.read_csv("sleep_ScreensData.csv")
sleep_ScreensData = pd.DataFrame(df)

print("-_" * 20)
print("Statistical Analysis") 
print(round(sleep_ScreensData.describe())) 

print("-_" * 20)
print("Head of the Dataframe") 
print(sleep_ScreensData.head())

print("-_" * 20)
print("Summary of the Dataframe") 
print(sleep_ScreensData.info())


