"""
Scraping Numbers from HTML using BeautifulSoup In this assignment you will
write a Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the sum of the numbers
in the file."""

"""We provide two files for this assignment. One is a sample file where
we give you the sum for your testing and the other is the actual data you need
to process for the assignment.

--Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
--Actual data: http://py4e-data.dr-chuck.net/comments_200956.html
(Sum ends with 99)

You do not need to save these files to your folder since your program will read
the data directly from the URL. Note: Each student will have a distinct data url
for the assignment - so only use your own data url for analysis.
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
#print(web_soup.find_all('span'))
count = 0
for num in web_soup.find_all('span'):
    kool = int(num.string)
    count += kool
    #print(kool)
print(count)
