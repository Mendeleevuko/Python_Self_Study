"""
Extracting Data from JSON
In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the
JSON data from that URL using urllib and then parse and extract the comment
counts from the JSON data, compute the sum of the numbers in the file and enter
the sum below:

We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process
for the assignment.

°°Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
°°Actual data: http://py4e-data.dr-chuck.net/comments_200959.json (Sum ends with 4)
You do not need to save these files to your folder since your program will read
the data directly from the URL. Note: Each student will have a distinct data url
for the assignment - so only use your own data url for analysis.
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#Surf the urllib
#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_200959.json'
print('Retrieving:', url)
"""This opens the location"""
uh = urllib.request.urlopen(url, context=ctx)
'''the location is read'''
uh_read = uh.read()

'''The data is decoded for json fit from UTF-8 to Unicode for computers'''
uh_read_decode = uh_read.decode()
#length_data = len(uh_read_decode)
"""The decoded data is loaded into json """
info_json = json.loads(uh_read_decode)

"""json.dumps allows the data to be printed much desired specified indentation"""
print(json.dumps(info_json, indent=4))


# ##for tag in info_json:
#     ##count = info_json["comments"][49]["count"]
#     ##print(count)
### print(type(info_json["comments"]))
# ##print(len(info_json["comments"]))

"""selected the one the strings in the single list contained in the dictionary
from json"""

"""iterated over the strings 'comments' in the one single list in the dictionary"""
count_num = 0
for tag in info_json["comments"]:
    count = tag['count']
    count_num += count
print(count_num)
