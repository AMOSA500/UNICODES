try:
  year = int(input("Enter age: "))
  print(year)
except ValueError:
  print("Enter an integer value only")