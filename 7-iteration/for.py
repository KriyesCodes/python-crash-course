people = ["kriyes", "safari", "abed", "paul"]

# print(people)

# for person in people:
#   print(person)


# for i in range(len(people)):
#   print(str(i+1) + ". " + people[i])

persons = {
  "person1": {"firstName":"kriyes", "lastName":"mahendra"},
  "person2": {"firstName":"safari", "lastName":"i dont know your suname"}
}

# for person in persons:
#   print(person)


for key, value in persons.items():
  print(key, value)