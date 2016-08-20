# DataQuest: Booleans & Ifs
# https://www.dataquest.io/mission/154/booleans-and-if-statements

# cat = True
# dog = False
# print(type(cat))
# print(type(dog))


with open('./crime_stats.csv', 'r') as file_object:
    final_data = [cell.split(',') for cell in file_object.read().split('\\n')]
# print(final_data)

crime_rates = [int(row[1]) for row in final_data]
# print("Crime Rates (integers):\n", crime_rates)

cities = [row[0] for row in final_data]
# print("Cities:\n", cities)

# booleans
first_alb = cities[0] == "Albuquerque"          # True
print(first_alb)
second_alb = cities[1] == "Albuquerque"         # False
print(second_alb)
print(crime_rates[0], crime_rates[1], crime_rates[-1])
# first_last = cities[0] == cities[len(cities) - 1]
first_last = cities[0] == cities[-1]            # False
print(first_last)
first_500 = crime_rates[0] > 500                # True
print(first_500)
first_749 = crime_rates[0] >= 749               # True
print(first_749)
# first_last = crime_rates[0] >= crime_rates[len(crime_rates) - 1]
first_last = crime_rates[0] >= crime_rates[-1]  # True
print(first_last)
second_500 = crime_rates[1] < 500               # True
print(second_500)
second_371 = crime_rates[1] <= 371              # True
print(second_371)
# second_last = crime_rates[1] <= crime_rates[len(crime_rates) - 1]
second_last = crime_rates[1] <= crime_rates[-1] # True
print(second_last)
# conditionals (if:)
result = 0
if cities[2] == "Anchorage":
    result = 1
print(result)


# Nesting if statements, note the indenting - per Z.A.S. - always have an else: clause.
value = 1500
if value > 500:
    if value > 1000:
        print("This number is HUGE!")
    else:
        print()
else: print('no')

results = 0
if crime_rates[0] > 500:
    if crime_rates[1] > 300:
        results = 3
    else:
        print()
else: print('whoa')


# if statements and for loops NOTE ENDS WITH THE FIRST INSTANCE of city == "Washington"
found = False
for city in cities:
    if city == 'Washington':
        found = True
    else:
        break
print(found)


# using a counter NOTE the "index" will contain the last found location city == "Washington"
counter = 0
index = 0

for city in cities:
    if city == "Washington":
        index = counter
    counter += 1
print(index)

five_hundred_list = []
for rate in crime_rates:
    if rate > 500:
        five_hundred_list.append(rate)
print(five_hundred_list)

