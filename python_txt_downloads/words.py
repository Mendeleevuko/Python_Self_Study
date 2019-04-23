file_name = input("Enter a file name:")
try :
    file_handle = open(file_name)
except:
    print("Please give the correct file name:", file_name)
    exit()

count_words = 0
count_line = 0
words_in = []
words_list = list()
words_dict = dict()
for line in file_handle:
    #line_strip = line.rstrip()## not necessary because the split function strips spaces automatically
    line_split = line.split()
    words_list.append(line)# this forms a better list for count
    #print(line_split)
    for words in line_split:
        #words_dict[words] = words_dict.get(words, 0) + 1
        count_words += 1
        #words_in.append(words) ### this is normal adding things together
        if words not in words_dict: # from here to the end of else, the get function does it better
            words_dict[words] = 1
        else:
            words_dict[words] = words_dict[words] + 1

val = list(words_dict.values())
val_2 = str(list(words_dict.values()))
max_val = max(val)
print("The maximum value:",max_val)

for key in words_dict:
    if words_dict[key] == max_val:
        print(key, words_dict[key])
        #print("The highest key:", key, words_dict[key])## same as the immediate previous print



    #print(line)
    count_line += 1


# count_val = 0
# val_max = None
# val_min = None
# for value in val:
#     if val_max < value and val_min < value:
#         val_max = value
#         val_min = value
#
#     elif val_min < value:
#         val_min = val_min
#
#     elif val_max < value:
#         val_max = value


##print(str(val))
#print(type(val))
# print("The least value in dictionary:",val_min)
# print("Highest value in dictionary:", val_max)
print(val)

print(words_dict)
print("Number of words in file:",count_words)
#print(words_list)
print("Number of lines in file:",count_line)
file_handle.close()
