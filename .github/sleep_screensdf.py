import pandas as pd
import random

hours_screen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

time_down = ["Right before bed", "30 minutes before bed", "1 hour before bed"]

in_room = ["Yes", "No"]

screenlimit = ["Yes", "No"]

hours_sleep = []

for i in range(15):
    hours_sleep.append([random.randint(5, 10)])

data = {
    "Hours_of_Sleep": hours_sleep,
    "Hours_of_Screens": [random.randint(1, 10) for _ in hours_sleep],
    "Time_Down": [random.choice(time_down) for _ in hours_sleep],
    "In_Room": [random.choice(in_room) for _ in hours_sleep],
    "Screenlimit":[random.choice(screenlimit) for _ in hours_sleep] 
}

sleep_ScreensData = pd.DataFrame(data)

sleep_ScreensData.to_csv("sleep_ScreensData.csv", index = False)
