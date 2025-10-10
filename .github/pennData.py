import pandas as pd
import random

fNames = ["Mac", "Danielle", "Aiden", "Ben", "Emily", "Jack", "Andrew", "Bella", "Joe", "Noah", "Chloe", "Sarah", "Alexis", "Emma", "Kyan", "Lisa", "Max", "Amelia"]
lNames = ["Smith", "Jones", "Johnson", "Williams", "Brown", "Garcia", "Davis", "Miller", "Wilson", "Moore", "Foster", "Anderson", "Manukyan", "DeFreitas", "Fogarty"]
years = ["Freshman", "Sophomore", "Junior", "Senior", "Victory Lap"]
pathways = ["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Childhood Education", "Culinary", "Criminsl Justice", "Construction", "Biomed"]
names = []

for i in range(20000):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.3), 2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]  
}

pennData = pd.DataFrame(data)

print(pennData)

pennData.to_csv("pennData.csv", index = False)