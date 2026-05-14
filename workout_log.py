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
    - Time of day

Processes:
- Accumulate total workout time
- Calculate average workout duration
- Find longest workout

Outputs:
- Workout summary (by category): number of workouts, total time, average duration, average calories burned

"""
# collect inputs
name = input("Name: ")
num_workouts = int(input("How many workouts do you want to record? "))
workouts = []

for i in range(num_workouts):
    exercise_type = input(f"Workout {i+1} type (run, walk, yoga, pickleball, basketball, other): ")
    workout_duration = int(input(f"Workout duration (min): "))
    calories_burned = int(input("Calories burned: "))
    exercise_time = input("Time of day (morning, afternoon, evening): ")
    workouts.append({"type":exercise_type, "duration":workout_duration,"calories burned":calories_burned,"time of day":exercise_time})

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
    if workout["duration"]>long_workout["duration"]:
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






  
    
