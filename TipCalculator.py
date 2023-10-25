print("""
   _
 _( )_          _      Keith R. Fulton | keith.fulton@chinalake.navy.mil
_(     )_      _( )_
(_________)   _(     )_
  \\  \\  \\    (_________)
    \\  \\       \\  \
               \\  \
""")
print("Welcome to Tip Calculator")

cost_of_meal = int(input("Enter Cost of Meal:  "))

rating = int(input("Enter Meal rating. \n 1. Totally Satisfied \n 2. Satisfied \n 3. Dissatisfied😒:   "))

total_satisfied = 20
satisfied = 15
dissatisfied = 10

if rating == 1:
  tip = cost_of_meal * (total_satisfied/100)
  new_cost_meal = cost_of_meal + tip
  print(f"Your meal is: {cost_of_meal} - Rating: Totally Satisfied. Tip: {tip}. Total Cost Of Meal 🤑 : {new_cost_meal}")
elif rating == 2:
  tip = cost_of_meal * (satisfied/100)
  new_cost_meal = cost_of_meal + tip
  print(f"Your meal is: {cost_of_meal} - Rating: Satisfied. Tip: {tip}. Total Cost Of Meal 🤑 : {new_cost_meal}")
else:
  tip = cost_of_meal * (dissatisfied/100)
  new_cost_meal = cost_of_meal + tip
  print(f"Your meal is: {cost_of_meal} - Rating: Dissatisfied 😡. Tip: {tip}. Total Cost Of Meal 🤑 : {new_cost_meal}")
  
  