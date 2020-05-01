from bs4 import BeautifulSoup
import requests

PAGE = "http://localhost:8000/auto_mpg.html"
results = requests.get(PAGE)
source = results.text

soup = BeautifulSoup(source, 'html.parser')


# print("\n.get_text() or .text")
# print(soup.get_text())
#
#
# print("\nGetting the head elements")
# print(soup.html.head)
#
# print("\nGetting the head elements parent , should be : html")
# print(soup.head.parent.name)
#
#
# print("\nGetting the html body")
# print(soup.body.text)
#
#
# print("\nGetting the first heading and paragraph")
# print(soup.body.h1)
# print(soup.body.p)
#
# print("\n Getting the h1's next sibling")
# print(soup.body.h1.next_sibling)
# print(soup.body.h1.next_sibling.next_sibling)
#
#
# print("\n Getting the attributes using attrs : attributes, here only 1")
# print(soup.body.a.attrs['href'])

# print("\n Finding the number of attributed")
# print(soup.find_all('a'))
#
# print("\n To get the inidividual divisions of car_block class")
# print(soup.find_all('div',class_ = 'car_block')[:10])

print("\n To get the first division of car_block class")
div = soup.find_all('div',class_ = 'car_block')[0]
print(div.prettify())
