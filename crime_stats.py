# python 3.5.1
# referencing http://learnpythonthehardway.org/book/ex15.html and
# https://www.dataquest.io/mission/2/files-and-loops
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


from sys import argv
# import io
# import codecs

filename = argv[1] # argv[0] is the name of the program script, i.e. crime_stats.py
file_object = open(filename, 'r', encoding='utf8')
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

for row in rows:
    print(row)
    
    

