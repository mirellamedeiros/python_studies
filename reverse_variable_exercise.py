variable = input("type something here! ")

reversed_variable = ""

for item in range(len(variable) -1, -1, -1):
  reversed_variable += variable[item]

print(reversed_variable)
