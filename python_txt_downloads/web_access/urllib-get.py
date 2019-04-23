import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

words_dict = {}
for line in file_handle:
    line = line.decode().strip()
    line_split = line.split()
    print(line_split)

    for words in line_split:
        if words not in words_dict:
            words_dict[words] = 1
        else:
            words_dict[words] = words_dict[words] + 1
print(words_dict)
    #print(line.decode().strip()) # rstrip() can be used


# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
