from connect import *

def readMenu():
  c.execute("SELECT * FROM menuItems")

  return c.fetchall()

if __name__ == "__main__":
  print(readMenu())