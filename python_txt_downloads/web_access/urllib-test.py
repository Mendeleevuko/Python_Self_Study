import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

source = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
"""installation of lxml needs to be done 'pip install lxml' """
"""Then, we create the "soup." This is a beautiful soup object:"""
soup = BeautifulSoup(source, 'lxml')#use "html.parser" instead of lxml

"""If you do print(soup) and print(source), it looks the same, but the source
is just plain the response data, and the soup is an object that we can actually
interact with, by tag, now, like so:"""

''' title of the page:'''
print(soup.title)

''' get attributes:'''
print(soup.title.name)

''' get values:'''
print(soup.title.string)

''' beginning navigation:'''
print(soup.title.parent.name)

'''getting specific values:'''
print(soup.p)

"""Finding paragraph tags <p> is a fairly common task. In the case above,
we're just finding the first one. What if we wanted to find them all?"""
# print(soup.find_all('p'))

"""We can also iterate through them:"""
# for parag in soup.find_all('p'):
#     print(parag.string)
#     #print(str(parag.text))
#     #print(soup.get_text())
"""Finally, you may just want to grab text.You can use .get_text() on a
Beautiful Soup object, including the full soup:"""

"""The difference between string and text is that string produces a
NavigableString object, and text is just typical unicode text. Notice that,
if there are child tags in the paragraph item that we're attempting
to use .string on, we will get None returned."""

"""Another common task is to grab links. For example:"""
# for url in soup.find_all('a'):
#     print(url.get('href'))

"""In this case, if we just grabbed the .text from the tag, you'd get the anchor
text, but we actually want the link itself. That's why we're using .get('href')
to get the true URL."""


#we defind new soup "nav", then use it to grab all the links from the Ist nav bar.
"""Now, rather than working with the entire soup, we can specify a new
Beautiful Soup object. An example might be:.In this case, we're grabbing
the first nav tags that we can find (the navigation bar).Next, we can grab the
links from just the nav bar:"""
# nav = soup.nav
# for  url in nav.find_all('a'):
#     print(url.get('href'))


#defind soup for body section
"""You could also go for soup.body to get the body section,
then grab the .text from there:"""

# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)


'''Finally, sometimes there might be multiple tags with the same names,
but different classes, and you might want to grab information from a specific
tag with a specific class. For example, our page that we're working with has
a div tag with the class of "body". We can work with this data like so:'''

for div in soup.find_all('div', class_='body'):
    print(div.text)
"""Note the class_='body', which allows us to work with a specific class of tag."""
