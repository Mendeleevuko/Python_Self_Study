####Question #8.4
"""Open the file romeo.txt and read it line by line. For each line, split the
line into a list of words using the split() method. The program should build a
list of words. For each word on each line check to see if the word is already
in the list and if not append it to the list. When the program completes, sort
 and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt"""

file_name = input("Enter File Name:")
file_handle = open(file_name)
add_word = ''
file_list = list()
for line in file_handle:
    line_strip = line.rstrip()
    line_split = line_strip.split()

    #print(line_strip)
    #print(line_split)
    for word in line_split:
        if word not in file_list:
            file_list.append(word)
            #add_word += word
            #print(add_word)
            file_list.sort()



print(file_list)
file_handle.close()
