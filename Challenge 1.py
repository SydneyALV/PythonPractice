#Person's information
name = input("Give me your name. ")
age = int(input("How old are you? "))
future_age = int(input("What age would you like to know? "))

year = str(2021 + (future_age - age))

#Year they will turn requested age
print(name + " will be " + str(future_age) + " in the year " + year + ".")
