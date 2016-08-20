# DataQuest: Booleans & Ifs
# https://www.dataquest.io/mission/154/booleans-and-if-statements

# cat = True
# dog = False
# print(type(cat))
# print(type(dog))


with open('./crime_stats.csv', 'r') as file_object:
    final_data = [cell.split(',') for cell in file_object.read().split('\\n')]
# print(final_data)

crime_rates_int = [int(row[1]) for row in final_data]
# print("Crime Rates (integers):\n", crime_rates_int)

cities_list = [row[0] for row in final_data]
# print("Cities:\n", cities_list)

