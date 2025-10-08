import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

df = pd.read_csv(".github\sleep_ScreensData.csv")
sleep_ScreensData = pd.DataFrame(df)

print("-_" * 20)
print("Head of the Dataframe") 
print(sleep_ScreensData.head())

print("-_" * 20)
print("Tail of the Dataframe") 
print(sleep_ScreensData.tail())

print("-_" * 20)
print("Statistical Analysis") 
print(round(sleep_ScreensData.describe())) 

print("-_" * 20)
print("Summary of the Dataframe") 
print(sleep_ScreensData.info())


sleep_ScreensData.groupby('Hours_of_Sleep')['   Hours_of_Screens'].mean().plot(kind = 'bar', color = 'teal', edgecolor = 'black') 
plt.title('Average Hours of Screen Time Per Day Related to Hours of Sleep')
plt.xlabel('Hours of Sleep')
plt.ylabel('Hours of Screen Time')
plt.show()

sleep_ScreensData['Hours_of_Sleep'].plot(kind = 'hist', bins = 5, edgecolor = 'black')  #sorts data based on how many buckets
plt.title('Hours of Sleep Distribution Among Students')
plt.xlabel('Hours of Sleep')
plt.ylabel('Number of Students')
plt.show()


sleep_ScreensData['   Hours_of_Screens'].value_counts().plot(kind = 'pie')  #sorts data based on how many buckets
plt.title('When do Students Put Their Phones Down Before Bed')
plt.ylabel('Number of Students')
plt.show()