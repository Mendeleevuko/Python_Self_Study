# import re
# file_open = open("regex_sum_200954.txt")
# #print(file_open)
#
# count = 0
# look = []
# kool = []
# for line in file_open:
#     line = line.rstrip()
#     #kool = re.findall("^The .+\S", line)
#     cool = re.findall("[0-9]+", line)
#     if len(cool) > 0:
#         kool.append(cool)
#         #print(type(cool))#(cool)s
#
#     #print(line)
#     #print(kool)
#     count += 1
#     sum_num = 0
#     for num in cool:
#         dool = int(num)
#         look.append(dool)
#
#         #print(dool)
#         #sum_num += int(num)
#     for num in look:
#         sum_num += num
# #print(num)
# print(sum_num)
# #print(kool)
# print(count)
# #print(look)
# file_open.close()

#### QUESTION:
"""
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give
you the sum for your testing and the other is the actual data you need to
process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
(There are 90 values with a sum=445833)

Actual data: http://py4e-data.dr-chuck.net/regex_sum_200954.txt
(There are 82 values and the sum ends with 111)
These links open in a new window. Make sure to save the file into the same
folder as you will be writing your Python program. Note: Each student will have
a distinct data file for the assignment - so only use your own data file
for analysis. """


import re
file_open = open("regex_sum_200954.txt")
#print(file_open)

count = 0
look = []
kool = []
for line in file_open:
    line = line.rstrip()

    cool = re.findall("[0-9]+", line)
    if len(cool) > 0:
        kool.append(cool)

    count += 1
    sum_num = 0
    for num in cool:
        dool = int(num)
        look.append(dool)

    for num in look:
        sum_num += num

print(sum_num)
print(count)

file_open.close()
