file = open("9-file-handling/testing.txt", "w")

file.write("testing...")
file.write("TESTING MORE...")

file.close()


with open("9-file-handling\ice-cream-flavours.txt", "a") as flavoursData:
  flavoursData.write("chocolate\nstrawberry\nvanilla")