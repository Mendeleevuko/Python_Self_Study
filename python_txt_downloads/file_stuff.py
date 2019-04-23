##Question #7.2
""" Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name."""
## Use the file name mbox_short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count_line = 0
line_float_add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line_find = line.find(' ')
    line_float = float(line[line_find+1:])
    line_float_add += line_float ### line_float_add=line_float_add+line_float
    count_line += 1
    #print(line)
avg_float = line_float_add/count_line
print("Average spam confidence:",avg_float)
print("Done")

##### Alternative to the above solution#####
######
####
###
file_name = input("Enter File Name: ")
file_open = open(file_name)
####file_handle = file_open.read()

count = 0
line_float_add = 0
for line in file_open:
    if line.startswith('X-DSPAM-Confidence:'):
        line_num = len(line)
        line_index = line.find(' ')
        line_get = line[line_index+1:]
        line_get_float = float(line_get)
        line_float_add += line_get_float  #+ line_get_float

        #print(line)
        #print(line_num)
        #print(line_get)
        print(line_get_float)


        count += 1
Avg_spam_confidence = line_float_add/count
print("count:",count)
print("line_float_add:",line_float_add)
print('Avg_spam_confidence:',(Avg_spam_confidence))

print("Done")
#print(line_index)
file_open.close()

#####
