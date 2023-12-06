num1 = 50
num2 = 50

# if num1 < num2:
#   print("num1 is lesser!")

# if num1 <= num2:
#   print("num1 is less or equal!")


# if num1 < num2:
#   print("num1 is lesser!")
# else:
#   print("num1 is equal or greater!")

# if num1 < num2:
#   print("num1 is lesser")
# elif num1 == num2:
#   print("num1 is equal")
# else:
#   print("else")

option = 2

match option:
  case 1:
    print("option is 1")
  case 2:
    print("option is 2")
  case 3:
    print("option is 3")
  case _:
    print("option not found")