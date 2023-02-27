# Setting Up BeautifulSoup

# For parsing HTML pages
from bs4 import BeautifulSoup

# For getting the data from HTML rendering of pages
import requests


PAGE = "http://localhost:8000/auto_mpg.html"

# This will return an HTTP response
results = requests.get(PAGE)

# ============================
# HTTP Response Codes:
# ============================
# 200 - OK
# 404 - Error : Page not Found
# 500 - Internal Server Error
# 418 - I'm a teapot. Included in the HTTP protocols, when coffee is requested. As an experiment

# The results will be an HTTP response
print(f"results : {results}")

# TO get response codes:
print(f"Status Code: {results.status_code}")

# <class results.models.Response>
print(f"The class of results is :{type(results)}")


# In order to get the whole content , use the below command. Getting the first 50 characters , since the page is large
# The results.content will be rendered as bytes when retrieved from the page.
print(results.content[:50])

# # To get the content in text format, a different syntax to be used. This will provide the file in str datatype
# print(results.text)

# String format obtained before parsing to BeautifulSoup
source = results.text

################# Using BeautifulSoup #################

# Can use any parser here. If content is XML, use 'xml.parser'
soup = BeautifulSoup(source,'html.parser')

# Soup object is a string as well, hence it supports slicing to get cetain content of the html page.
print(f"Soup: {type(soup.prettify())}")

# # Checking contents of soup can be messy
print(f"Contents of soup using prettify()")

# prints all the HTML webpage content in HTML format.
print(soup.prettify())
