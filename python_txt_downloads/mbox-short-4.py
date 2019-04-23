import re

file_name = input("Enter a file name:")
try:
    file_handle = open(file_name)

except:
    print("Wrong file name:", file_name)

line_collect = list()
for line in file_handle:
    line = line.rstrip()
    if re.search('^From:.+@', line): # ('From:', line) or ('^F..m:', line) or ('^From:.+@', line)
        print(line)
##         line_collect.append(line)
## print(line_collect)

file_handle.close()

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
Ist = re.findall('\S+@\S+', s)
print(Ist)


file_name = input("Enter a file name:")
try:
    file_handle = open(file_name)
except:
    print("Wrong file name:", file_name)

for line in file_handle:
    line = line.rstrip()
    k =  re.findall('\S+@\S+', line)
    if len(k) > 0:
        print(k)

file_handle.close()

file_name = input("Enter a file name:")
try:
    file_handle = open(file_name)
except:
    print("Wrong file name:", file_name)

for line in file_handle:
    line = line.rstrip()
    cool = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(cool) > 0:
        print(cool)

file_handle.close()
