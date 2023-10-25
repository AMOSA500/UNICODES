print("""

   _
     _( )_          _      Keith R. Fulton | keith.fulton@chinalake.navy.mil
   _(     )_      _( )_
  (_________)   _(     )_
    \  \  \    (_________)
      \  \       \  \  \
                   \  \
""")
print("Welcome to Temperature Converter")

def convertStringToInt(msg):
  temperature = input(msg)
  if temperature.isnumeric():
    return int(temperature)
  else:
    print("Enter a numeric value")
    return convertStringToInt(msg)

# Centigrade temperature (c) into Fahrenheit (f)
celcius = convertStringToInt("Please enter celcius value: ")
#Convertion f = (c * 1.8) + 32
fahrenheit = (celcius * 1.8) + 32
print(f"{celcius} celcius to Fahrenheit = {fahrenheit}")