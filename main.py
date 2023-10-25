def takeinput():
  print("""
  8b,dPPYba,  ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba,  
88P'   `"8a ""     `Y8 88P'   "88"    "8a a8P_____88  
88       88 ,adPPPPP88 88      88      88 8PP"""""""  
88       88 88,    ,88 88      88      88 "8b,   ,aa  
88       88 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
""")
  fn = input("Enter first name: ")
  sn = input("Enter surname: ")
  age = convertStringToInt("Please enter your age")
  print(f"Full Name: {fn} {sn} and you are {age} years old")
  
  
  """Use a separate function or method to prevent the code from starting over again.
  Create a new method and put the convertion of age into it.
  if(age.isnumeric):
    age = int(age)
  else:
    takeinput()

  NB: Remember to make your code generic so as to avoid repeation of same function for 
  several string to int convertion such as age, money or number of items - convertStringToInt()
  By using parameters in the function, you can make the function generic.
  This is known as Utility Function or Class
  """

takeinput()