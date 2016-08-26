# https://www.dataquest.io/mission/158/challenge-files-loops-and-conditional-logic
# DQ Challenges - Unisex Names
# https://github.com/fivethirtyeight/data/blob/master/unisex-names/unisex_names_table.csv


# # # # Read The File Into String
# # file = open('dq_unisex_names.csv', 'r')
# # print(file)
# # data = file.read()
# # print(data)
# # file.close()
# # print(file)
# # try: c = file.read()
# # except: print("file is closed")

with open('dq_unisex_names.csv', 'r') as file_object:
    # print(file_object)
    data = file_object.read()
    # print(data)
# print(file_object)
# try: c = file_object.read()
# except: print("file object is closed")
# # # http://stackoverflow.com/questions/8011797/open-read-and-close-a-file-in-1-line-of-code


# # # # Convert The String To A List
data_list = data.split('\n')

# first_five = data_list[0:5]
# print(first_five)


# # # # Convert The List Of Strings To A List Of Lists
# # # For-Loop:
# string_data = []
# for data in data_list:
    # comma_list = data.split(',')
    # string_data.append(comma_list)
# print(string_data[0:5])

# # # List comprehension:
string_data = [data.split(',') for data in data_list]
# print(string_data[0:5])


# # # # Convert Numerical Values
# numerical_data = []
# for data in string_data:
    # name = data[0]
    # num = float(data[1])
    # converted = [name, num]
    # numerical_data.append(converted)
# # print(numerical_data)

numerical_data = [[data[0], float(data[1])] for data in string_data]
# print(numerical_data)


# # # # Filter The List
# print(len(numerical_data))
# thousand_or_greater = []
# for list in numerical_data:
    # if list[1] >= 1000:
        # thousand_or_greater.append(list[0])
# print(thousand_or_greater[0:10])

# # # List comprehension with conditional
hun_thou_or_more = [list[0] for list in numerical_data if list[1] >= 100000]
print(hun_thou_or_more)


