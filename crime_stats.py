# python 3.5.1
# referencing http://learnpythonthehardway.org/book/ex15.html and
# https://www.dataquest.io/mission/2/files-and-loops
# invoke this script with the "crime_stats.csv" file in the same directory
# invoke from the cmd line like so: "python crime_stats.py crime_stats.csv"

from sys import argv

file = argv[1] # argv[0] is the name of the program script, i.e. crime_stats.py
filename = open(file, 'r')
file_contents = filename.read()

print("Here's the file: %r: " % file)
# print("Here's the file object: %r: " % filename) # I forget what the diff of %s and %r
# print("Here's the file object: %s: " % filename) #'s'tring and 'r'aw?
print("Here's the file object: {}".format(filename))
print("Here's the file contents: \n{}".format(file_contents))

