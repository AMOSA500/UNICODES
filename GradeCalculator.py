import OddEven


# Function to calculate the grade
def gradeCalc(grade):
  if grade > 100:
    return "Grade cannot be greater than 100"
  elif grade >= 70:
    return "You have Distinction!"
  elif grade >= 60 and grade < 69:
    return "2.1!"
  elif grade >= 50 and grade < 59:
    return "2.2!"
  elif grade >= 40:
    return "Pass"
  else:
    return "Fail"


def enterGrade():
  grade = int(input("Enter your grade:  "))
  odd_or_even = OddEven.OddEven(grade)
  remark = gradeCalc(grade)
  print(f"The number {grade} is {odd_or_even}.Your Grade: {remark}")




print('''
                                       88           
                                ,d    88           
                                88    88           
88,dPYba,,adPYba,  ,adPPYYba, MM88MMM 88,dPPYba,   
88P'   "88"    "8a ""     `Y8   88    88P'    "8a  
88      88      88 ,adPPPPP88   88    88       88  
88      88      88 88,    ,88   88,   88       88  
88      88      88 `"8bbdP"Y8   "Y888 88       88  
''')
enterGrade()

