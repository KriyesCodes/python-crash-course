from connect import *

c.execute("""INSERT INTO menuItems(name, price, type) VALUES
          ("McSpicy", 699, "Burger"),
          ("Hash Brown", 99, "Breakfast"),
          ("Latte", 199, "McCafe"),
          ("McChicken Sandwich", 499, "Burger")
          """)

conn.commit()