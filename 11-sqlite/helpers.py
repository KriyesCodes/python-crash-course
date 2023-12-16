def getMenuText(menuOptions, menuTitle="MENU"):
  textWidth = 30
  text = "\n" + "{:^{width}}".format(menuTitle, width=textWidth) + "\n"
  for key, value in menuOptions.items():
    text = text + str(key) + ". " + value + "\n"
  return text

def getMenuInput(menuOptions, menuTitle):
  while True:
      print(getMenuText(menuOptions, menuTitle))
      try:
        choice = int(input("What would you like to do? "))
        if (choice in menuOptions.keys()):
          return choice
        else:
          raise Exception()
      except:
        print("\nIncorrect input, enter the number correlating to your choice")