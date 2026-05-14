"""
IS 303 - A03
Jeremy Eldredge
Expense Tracker

Description: Workout log. Logs workout sessions and produces fitness statistics.

Inputs:
- Name
- Number of workouts
- For each workout:
    - Exercise type
    - Workout duration
    - Calories burned

Processes:
- Accumulate total workout time
- Calculate average workout duration
- Find longest workout

Outputs:
- Workout summary (by category): number of workouts, total time, average duration, average calories burned

"""
# collect inputs
workout_types = ["run", "walk", "yoga", "pickleball", "basketball", "other"]

name = input("Name: ").capitalize()
num_workouts = int(input("How many workouts do you want to record? "))
workouts = []

for i in range(num_workouts):
    while True:
        exercise_type = input(f"Workout {i+1} type (run, walk, yoga, pickleball, basketball, other): ").lower()
        if exercise_type in workout_types:
            break
        else:
            print("Invalid workout type. Enter one of the given options.")
    while True:
        try:
            workout_duration = int(input(f"Workout duration (min): "))
            if workout_duration > 0:
                break
            else:
                print("Please enter a whole number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")
    while True:
        try:
            calories_burned = int(input("Calories burned: "))
            if calories_burned > 0:
                break
            else:
                print("Please enter a whole number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")
workouts.append({"type":exercise_type, "duration":workout_duration,"calories burned":calories_burned})

# processes

total_time = 0
total_calories = 0

for workout in workouts:
    total_time += workout["duration"]
    total_calories += workout["calories burned"]

avg_duration = total_time/len(workouts)
avg_calories = total_calories/len(workouts)

long_workout = workouts[0]
for workout in workouts:
    if workout['duration']>long_workout['duration']:
        long_workout = workout

runs=[]
total_time_runs = 0
total_cal_runs = 0
walks=[]
total_time_walks = 0
total_cal_walks = 0
yogas=[]
total_time_yogas = 0
total_cal_yogas = 0
pickles=[]
total_time_pickleball = 0
total_cal_pickleball = 0
baskets=[]
total_time_basketball = 0
total_cal_basketball = 0
others=[]
total_time_others = 0
total_cal_others = 0

for workout in workouts:
    if workout["type"] == "run":
        runs.append(workout)
        total_time_runs += workout["duration"]
        total_cal_runs += workout["calories burned"]
        avg_duration_runs = total_time_runs / len(runs)
        avg_calories_runs = total_cal_runs / len(runs)
    elif workout["type"] == "walk":
        walks.append(workout)
        total_time_walks += workout["duration"]
        total_cal_walks += workout["calories burned"]
        avg_duration_walks = total_time_walks / len(walks)
        avg_calories_walks = total_cal_walks / len(walks)
    elif workout["type"] == "yoga":
        yogas.append(workout)
        total_time_yogas += workout["duration"]
        total_cal_yogas += workout["calories burned"]
        avg_duration_yogas = total_time_yogas / len(yogas)
        avg_calories_yogas = total_cal_yogas / len(yogas)
    elif workout["type"] == "pickleball":
        pickles.append(workout)
        total_time_pickleball += workout["duration"]
        total_cal_pickleball += workout["calories burned"]
        avg_duration_pickleball = total_time_pickleball / len(pickles)
        avg_calories_pickleball = total_cal_pickleball / len(pickles)
    elif workout["type"] == "basketball":
        baskets.append(workout)
        total_time_basketball += workout["duration"]
        total_cal_basketball += workout["calories burned"]
        avg_duration_basketball = total_time_basketball / len(baskets)
        avg_calories_basketball = total_cal_basketball / len(baskets)
    elif workout["type"] == "other":
        others.append(workout)
        total_time_others += workout["duration"]
        total_cal_others += workout["calories burned"]
        avg_duration_other = total_time_others / len(others)
        avg_calories_other = total_cal_others / len(others)

# output message
"""Outputs:
- Workout summary (by category): number of workouts, total time, average duration, average calories burned"""

print(f"--- {name}'s Workout Report ---")
print("--------------------------------")
print(f"Number of workouts: {len(workouts)} ")
print(f"Total time: {total_time} minutes")
print(f"Total calories burned: {total_calories}")
if len(runs) > 0:
    print("--------------------------------")
    print("Running Report")
    print("--------------------------------")
    print(f"Number of runs: {len(total_time_runs)}")
    print(f"Average run duration: {avg_duration_runs} minutes")
    print(f"Average calories burned: {avg_calories_runs}")
if len(walks) > 0:
    print("--------------------------------")
    print("Walking Report")
    print("--------------------------------")
    print(f"Number of walks: {len(walks)}")
    print(f"Average walk duration: {avg_duration_walks} minutes")
    print(f"Average calories burned: {avg_calories_walks}")
if len(yogas) > 0:
    print("--------------------------------")
    print("Yoga Report")
    print("--------------------------------")
    print(f"Number of yoga sessions: {len(yogas)}")
    print(f"Average yoga duration: {avg_duration_yogas} minutes")
    print(f"Average calories burned: {avg_calories_yogas}")
if len(pickles) > 0:
    print("--------------------------------")
    print("Pickleball Report")
    print("--------------------------------")
    print(f"Number of pickleball sessions: {len(pickles)}")
    print(f"Average pickleball duration: {avg_duration_pickleball} minutes")
    print(f"Average calories burned: {avg_calories_pickleball}")
if len(baskets) > 0:    
    print("--------------------------------")
    print("Basketball Report")
    print("--------------------------------")
    print(f"Number of basketball sessions: {len(baskets)}")
    print(f"Average basketball duration: {avg_duration_basketball} minutes")
    print(f"Average calories burned: {avg_calories_basketball}")
if len(others) > 0:
    print("--------------------------------")
    print("Other Workout Report")
    print("--------------------------------")
    print(f"Number of other workouts: {len(others)}")
    print(f"Average other workout duration: {avg_duration_other} minutes")
    print(f"Average calories burned: {avg_calories_other}")
    
