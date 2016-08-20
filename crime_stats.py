# python 3.5.1
# referencing http://learnpythonthehardway.org/book/ex15.html and
# https://www.dataquest.io/mission/2/files-and-loops
# working with this data: https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate_(2014)
# invoke this script with the "crime_stats.csv" file in the same directory
# invoke from the cmd line like so: "python crime_stats.py crime_stats.csv"
# In lesson one of DataQuests Data Analyst track We went over the basics of
# Variables (bindings)
# Comments
# Print Function
# Types
# Type Functions
# Arithmetic Operators
# Converting Types
# OOP basics
# Lists
# List function - append
# Lists values - multiple types or the same
# List indexes
# List length
# List slicing
# In lesson two we are dealing with a data set
# Opening Files
# Reading in files
# Splitting data in files
# For-Loops
# lists of lists
# splitting elements in a list
# double bracket notation


from sys import argv
# import io
# import codecs

filename = argv[1] # argv[0] is the name of the program script, i.e. crime_stats.py
file_object = open(filename, 'r') #, encoding='utf8')
file_contents = file_object.read()
file_list = file_contents.split("\\n") # HAHAHA - it took me a LOOOONG TIME to remember the leading slash here
# http://stackoverflow.com/questions/39051835/python-3-split-n/39051836#39051836
# BUT I am still not really sure why??? (see TEXT.split('\n')) below)

print("1.) Here's the name of the file: %r: " % filename)
# print("Here's the file object: %r: " % file) # I forget what the diff of %s and %r
# print("Here's the file object: %s: " % file) # 's'tring and 'r'aw?
print("2.) Here's the file object info: {}".format(file_object))
print("3.) Here's the files contents:\n{}".format(file_contents))
print("4.) Here's a list of the file contents:\n{}".format(file_list))

# weird, WHY DO I NEED THE EXTRA \ FOR THE FILE BUT NOT FOR THE STRING?
# print()
# print()
# print(type(file_contents))
# print(type(file_list))
# TEXT = "Albuquerque,749\nAnaheim,371\nAnchorage,828\nArlington,503\nAtlanta,1379\nAurora,425\nAustin,408\nBakersfield,542\nBaltimore,1405\nBoston,835\nBuffalo,1288\nCharlotte-Mecklenburg,647\nCincinnati,974\nCleveland,1383\nColorado Springs,455\nCorpus Christi,658\nDallas,675\nDenver,615\nDetroit,2122\nEl Paso,423\nFort Wayne,362\nFort Worth,587\nFresno,543\nGreensboro,563\nHenderson,168\nHouston,992\nIndianapolis,1185\nJacksonville,617\nJersey City,734\nKansas City,1263\nLas Vegas,784\nLexington,352\nLincoln,397\nLong Beach,575\nLos Angeles,481\nLouisville Metro,598\nMemphis,1750\nMesa,399\nMiami,1172\nMilwaukee,1294\nMinneapolis,992\nMobile,522\nNashville,1216\nNew Orleans,815\nNew York,639\nNewark,1154\nOakland,1993\nOklahoma City,919\nOmaha,594\nPhiladelphia,1160\nPhoenix,636\nPittsburgh,752\nPlano,130\nPortland,517\nRaleigh,423\nRiverside,443\nSacramento,738\nSan Antonio,503\nSan Diego,413\nSan Francisco,704\nSan Jose,363\nSanta Ana,401\nSeattle,597\nSt. Louis,1776\nSt. Paul,722\nStockton,1548\nTampa,616\nToledo,1171\nTucson,724\nTulsa,990\nVirginia Beach,169\nWashington,1177\nWichita,742"
# TEXT_WHAT = TEXT.split("\n")
# print(TEXT_WHAT)
# print(type(TEXT_WHAT))
# print(type(TEXT))
# print(TEXT)

# on with the DataQuest lesson

rows = file_contents.split("\\n")
print(len(rows))
print(rows)

for row in rows:
    print(row)

# # Splitting a list of lists
# three_rows = ['Albuquerque, 740', 'Anaheim, 371', 'Anchorage, 828']
# final_list = []
# for row in three_rows:
    # split_list = row.split(',')
    # final_list.append(split_list)
# print(final_list)
# print(final_list[0])
# print(final_list[1])
# print(final_list[2])

# # list comprehension
# x = [row.split(',') for row in three_rows]
# print("list comprehension: {}".format(x))

# # splitting elements in a list
# final_data_for = []
# for row in rows:
    # split_list = row.split(',')
    # final_data_for.append(split_list)
# print(final_data_for)

# list comprehension version:
final_data = [row.split(',') for row in rows]
print(final_data)

# make separate lists of crime rate and cities
crime_rates = []
for row in final_data:
    crime_rate = row[1]
    crime_rates.append(crime_rate)
print(crime_rates)

cities_list = []
for row in final_data:
    city = row[0]
    cities_list.append(city)
print(cities_list)

# convert the crime rates to integers
crime_rates_int = []
for row in final_data:
    crime_rate = int(row[1])
    crime_rates_int.append(crime_rate)
print(crime_rates_int)




# My solution: 
# f = open('crime_rates.csv', 'r')   # These work in the DataQuest environment
# data = f.read()
# rows = data.split('\n')
f = open('./crime_stats.csv', 'r')   # These work with local files/cmds
data = f.read()
rows = data.split('\\n')
# print(rows[0:5])
int_data = []
for row in rows:
    split_list = row.split(',')
    crime_rate = int_data.append(int(split_list[1]))
int_crime_rates = int_data
print()
print(int_crime_rates)

# Their solution
# f = open('crime_rates.csv', 'r')
# data = f.read()
# rows = data.split('\n')
# print(rows[0:5])
# int_crime_rates = []
# for row in rows:
    # values = row.split(',')
    # crime_rate = int(values[1])
    # int_crime_rates.append(crime_rate)

file_object.close()
print(file_object)
# mystr = file_object.read() # This will throw an error - use try/except?

f.close()
print(f)
# c = f.read() # This will throw an error - use try/except?

# DON'T FORGET TO CLOSE FILES!
# THERE IS ALSO THE with ... as ... technique:

with open('.\crime_stats.csv', 'r') as with_open:
    print(with_open.read())

# with_open is automatically closed


###MORE MESSING ABOUT TO FOLLOW

# # # # from sys import argv     # the name of the file is to be entered
# # # # file_name = argv[1]      # when python script (argv[0]) is invoked
# # # file_name = ("crime_stats.csv")
# # # file_object = open(file_name, 'r')
# file_object = open('./crime_stats.csv', 'r') # either \ or / seem to work for indicating directories
# file_contents = file_object.read()

#### Grand master "with-as-list comprehension":
# with open('./crime_stats.csv', 'r') as file_object:
    # file_contents = [cell.split(',') for cell in file_object.read().split('\\n')]

with open('./crime_stats.csv', 'r') as file_object:
    # print(file_object.read())
    file_contents = file_object.read()

# print(file_contents)
# print(file_object.read()) # THROWS an EROR cuz the file has been closed by "with...as"
# try:
    # print(file_object.read())
# except:
    # print('file is closed') 
# except ValueError:

file_list = file_contents.split('\\n')
# print(file_list)

value_list = [cell.split(',') for cell in file_list]
# value_list = [cell.split(',') for cell in file_contents.split('\\n')]
print(value_list)

###LIST COMPREHENSIONS
# make separate lists of crime rate and cities
# crime_rates = []
# for row in final_data:
    # crime_rate = row[1]
    # crime_rates.append(crime_rate)
# # print(crime_rates)

# # convert the crime rates to integers
# crime_rates_int = []
# for row in final_data:
    # crime_rate = int(row[1])
    # crime_rates_int.append(crime_rate)
crime_rates_int = [int(row[1]) for row in final_data]
print("Crime Rates (integers):\n", crime_rates_int)

# cities_list = []
# for row in final_data:
    # city = row[0]
    # cities_list.append(city)
cities_list = [row[0] for row in final_data]
print("Cities:\n", cities_list)


