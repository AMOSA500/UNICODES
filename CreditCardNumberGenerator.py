print("Credit Card Generator")


def credit_card():
  cc_number = input("Enter 16 Digits Credit Card Number: ")
  return cc_number


def len_cc_digits(cc_number):
  return len(cc_number)


start = 0
while start == 0:
  # Variable Declaration
  cc_number = credit_card()
  credit_card_digits = []
  total = 0

  if len_cc_digits(cc_number) == 16:
    print("Thank you! Validating Now...")

    for char in cc_number:
      if char.isdigit():
        digit = int(char)
        credit_card_digits.append(digit)
      else:
        print("Warning!!! Credit Card Number Cannot Contain Alphabets")

    # Check Credit Card
    for x, _ in enumerate(credit_card_digits):
      if x % 2 == 0:
        s_digit = (credit_card_digits[x] * 2)
        if s_digit > 9:
          s_digit -= 9
          total += s_digit
        else:
          total += s_digit
      else:
        total += credit_card_digits[x]

    if total % 10 == 0:
      print(credit_card_digits)
      print("This is a valid Credit Card Number")
      start = 1  #End Loop
    else:
      print(f"{credit_card_digits} - is NOT a valid credit card number")

  else:
    print("Invalid Digits. 16 Digits is Expected: ")
