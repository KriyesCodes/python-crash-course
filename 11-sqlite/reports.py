from connect import *

def getAllOrderByType(isDescending=False):
  if (not(isDescending)):
    c.execute("SELECT * FROM menuItems ORDER BY type ASC")
  else:
    c.execute("SELECT * FROM menuItems ORDER BY type DESC")

  return c.fetchall()


if __name__ == "__main__":
  data = getAllOrderByType()
  for row in data:
    print(row)