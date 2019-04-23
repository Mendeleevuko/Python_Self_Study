###Question # 10.2
""" Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the hour
out from the 'From ' line by finding the time and then splitting the string a
second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below."""

name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
word_catch = list()
word_dict = dict()
date_catch = list()
date_split_catch = list()
for line in handle:
    if not line.startswith('From '):
        continue
    line_split = line.split()
    line_list = line_split[5]
    #print(line_split[5])
    line_split_2 = line_list.split(':')
    #date_catch.append(line_split_2)
    date_split = line_split_2[0]
    #print(date_split)
    date_split_catch.append(date_split)
#print(date_split_catch)
num_dict = dict()
for num in date_split_catch:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] = num_dict[num] + 1
#print(num_dict)

list_num = list()
for key, val in list(num_dict.items()):
    list_num.append((key, val))
    list_num.sort()
for key, val in list_num:
    print(key, val)
#print(list_num)
    #print(key, val)
#tuple_num = num_dict.items()
#print(tuple_num)
#list_tuple_num = list(tuple_num)
#print(list_tuple_num)



#print(date_catch)
    #print(line_split_2)
#     for word in line_split:
#         if word == line_split[1]:
#             word_catch.append(word)
#             count += 1
#     #print(word_catch)
# for word in word_catch:
#         if word not in word_dict:
#             word_dict[word] = 1
#         else:
#             word_dict[word] = word_dict[word] + 1
#
#
#
# val = list(word_dict.values())
# max_val = max(val)
#
# for key in word_dict:
#     if word_dict[key] == max_val:
#         print(key, word_dict[key])

#print(word_dict)
handle.close()

"""Use this as your code sample for job applications"""

# name = input("Enter file:")
# handle = open(name)
#
# word_catch = list()
# word_dict = dict()
# date_catch = list()
# date_split_catch = list()
#
# for line in handle:
#     if not line.startswith('From '):
#         continue
#     line_split = line.split()
#     line_list = line_split[5]
#     line_split_2 = line_list.split(':')
#     date_split = line_split_2[0]
#     date_split_catch.append(date_split)
#
# num_dict = dict()
# for num in date_split_catch:
#     if num not in num_dict:
#         num_dict[num] = 1
#     else:
#         num_dict[num] = num_dict[num] + 1
#
#
# list_num = list()
# for key, val in list(num_dict.items()):
#     list_num.append((key, val))
#     list_num.sort()
# for key, val in list_num:
#     print(key, val)
# #print(list_num)
# handle.close()

    
