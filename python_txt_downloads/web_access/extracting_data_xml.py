"""
Extracting Data from XML
In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL,
read the XML data from that URL using urllib and then parse and extract the
comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process
for the assignment.

--- Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
-- Actual data: http://py4e-data.dr-chuck.net/comments_200958.xml (Sum ends with 86)

You do not need to save these files to your folder since your program will
read the data directly from the URL. Note: Each student will have a distinct
data url for the assignment - so only use your own data url for analysis.
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# # Surfing a web_name
"""The input will request for a location on the web in form of strings"""
url = input("Enter a location:")
'''You can copy this link as the input when prompted'''
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = 'http://py4e-data.dr-chuck.net/comments_200958.xml'
print('Retrieving:', url)
"""This opens the location"""
uh = urllib.request.urlopen(url, context=ctx)
'''the location is read'''
uh_read = uh.read()

'''The data is decoded for xml fit'''
uh_read_decode = uh_read.decode()
length_data = len(uh_read_decode)

'''Parse it into xml in python'''
tree = ET.fromstring(uh_read_decode)
tags = tree.findall('comments/comment')

count_num = 0
for tag in tags:
    '''runs through the comment and extract count text values'''
    '''then converted to integers for summation'''
    got_tag = int(tag.find("count").text)
    count_num += got_tag
    print(got_tag)
    #print('Count', type(tag.find('count').text))
print("Total count number:",count_num)


#print(uh)
#print(uh_read)
# print(uh_read_decode)
# print(length_data)
#print("comment:", len(comment))
#print(tree)
#print('tag:', len(tags))



'''These lines of code are for different purpose'''

# api_key = False
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)
#
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
#
#     print('lat', lat, 'lng', lng)
#     print(location)
