####Question #9.4
"""Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file. After the dictionary
is produced, the program reads through the dictionary using a maximum loop to
find the most prolific committer."""

file_name = input("Enter a file name: ")
try:
    file_handle = open(file_name)
except:
    print("Wrong file name:", file_name)
    exit()

word_catch = list()
emai_dict = dict()
words_list = list()
words_dict = dict()
count_line = 0
for line in file_handle:
    if not line.startswith('From '):
        continue
    line_split = line.split()
    for word in line_split:
        if word == line_split[1]:
            word_catch.append(word)
    count_line += 1
count = 0
for email in word_catch:
    if email not in words_dict:
        words_dict[email] = 1
    else:
        words_dict[email] = words_dict[email] + 1
    count += 1

#print("count =",count)
#print("count_line =",count_line)
#print(word_catch)
#print(words_dict)
val = list(words_dict.values())
max_val = max(val)
for key in words_dict:
    if words_dict[key] == max_val:
        #print("The most occuring email sender:", key, words_dict[key])
        print( key, words_dict[key])

        # line_list = line_split[1]
        # word_catch.append(line_split)
print(max_val)
print(words_dict)
print(word_catch)



    #print(line_list)
    #print(line_split)
    ## for emai in line_list:
    ##     if emai not in emai_dict:
    ##         emai_dict[emai] = 1
    ##     else:
    ##         emai_dict[emai] = emai_dict[emai] + 1


    ##words_list.append(line_split)
#     for words in line_split:
#         if words not in words_dict:
#             words_dict[words] = 1
#         else:
#             words_dict[words] = words_dict[words] + 1
#
# val = list(words_dict.values())
# max_val = max(val)
# print(max_val)
# for key in words_dict:
#     if key == max_val:
#         print(key, words_dict[key])

##print(emai_dict)
##print(words_list)

#print(words_dict)
file_handle.close()


"""This code below is exact same as the one displayed above. You can chose
to uncomment this and comment the above and use it. Anyone works for same problem"""
####### this is same as above code but more concise


# name = input("Enter file:")
# ##if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# count = 0
# word_catch = list()
# word_dict = dict()
# for line in handle:
#     if not line.startswith('From '):
#         continue
#     line_split = line.split()
#     line_list = line_split[1]
#     ##print(line_split[1])
#     for word in line_split:
#         if word == line_split[1]:
#             word_catch.append(word)
#             count += 1
#     ##print(word_catch)
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
#
#
#
# ##print(word_dict)
# handle.close()
