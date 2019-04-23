"""
Following Links in Python
In this assignment you will write a Python program that expands on
http://www.py4e.com/code3/urllinks.py. The program will use urllib to read
the HTML from the data files below, extract the href= vaues from the anchor
tags, scan for a tag that is in a particular position relative to the first
name in the list, follow that link and repeat the process a number of times and
report the last name you find.

We provide two files for this assignment. One is a sample file where we give you
the name for your testing and the other is the actual data you need to process
for the assignment

--Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link.
Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
---Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Derrie.html
Find the link at position 18 (the first name is 1). Follow that link.
Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: K

--Strategy
The web pages tweak the height between the links and hide the page after a few
seconds to make it difficult for you to do the assignment without writing a
Python program. But frankly with a little effort and patience you can overcome
these attempts to make it a little harder to complete the assignment without
writing a Python program. But that is not the point. The point is to write a
clever Python program to solve the program.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

web_name = input("Enter web name:")
web_open = urllib.request.urlopen(web_name, context=ctx).read()
web_soup = BeautifulSoup(web_open, "html.parser")

#print(web_soup)
##print(web_soup.title)
# print(web_soup.title.name)
# print(web_soup.title.string)
# print(web_soup('a'))
# print(web_soup.string)
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
for tag in web_soup.find_all('a'):
    # print(tag.string)
    # print(tag.get('href'))
    #print(tag.string[0:])
    a += 1
    if a == 18:
        tag_1 = tag.get('href')
        #print(tag.string)
        #print(tag.get('href'))
print('Retrieving:',tag_1)
web_open = urllib.request.urlopen(tag_1, context=ctx).read()
web_soup = BeautifulSoup(web_open, "html.parser")
for tag in web_soup.find_all('a'):
    b += 1
    if b == 18:
        tag_2 = tag.get('href')
        print(tag.string)
print('Retrieving:',tag_2)

web_open = urllib.request.urlopen(tag_2, context=ctx).read()
web_soup = BeautifulSoup(web_open, "html.parser")
for tag in web_soup.find_all('a'):
    c += 1
    if c == 18:
        tag_3 = tag.get('href')
        print(tag.string)
print('Retrieving:',tag_3)

web_open = urllib.request.urlopen(tag_3, context=ctx).read()
web_soup = BeautifulSoup(web_open, "html.parser")
for tag in web_soup.find_all('a'):
    d += 1
    if d == 18:
        tag_4 = tag.get('href')
        print(tag.string)
print('Retrieving:',tag_4)

web_open = urllib.request.urlopen(tag_4, context=ctx).read()
web_soup = BeautifulSoup(web_open, "html.parser")
for tag in web_soup.find_all('a'):
    e += 1
    if e == 18:
        tag_5 = tag.get('href')
        print(tag.string)
print('Retrieving:',tag_5)

web_open = urllib.request.urlopen(tag_5, context=ctx).read()
web_soup = BeautifulSoup(web_open, "html.parser")
for tag in web_soup.find_all('a'):
    f += 1
    if f == 18:
        tag_6 = tag.get('href')
        print(tag.string)
print('Retrieving:',tag_6)

web_open = urllib.request.urlopen(tag_6, context=ctx).read()
web_soup = BeautifulSoup(web_open, "html.parser")
for tag in web_soup.find_all('a'):
    g += 1
    if g == 18:
        tag_7 = tag.get('href')
        print(tag.string)
print('Retrieving:',tag_7)
