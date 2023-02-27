# Module Scrapper.py
import requests
import re
import pickle
import os
import csv # for exporting to csv file
from bs4 import BeautifulSoup

PAGE = "http://localhost:8000/auto_mpg.html"

def process_car_blocks(soup):
    """Extract information from repeated divisions"""
    car_blocks = soup.find_all('div',class_='car_block')
    rows = []
    for cb in car_blocks:
        row = extract_data(cb)
        rows.append(row)
    print(f"We have {len(rows)} rows of scrapped car data")
    # Print statements for sanity check, to see if the data is scrapped
    print(rows[0])
    print(rows[-1])

    # Writing to .CSV file
    with open("scraped_cars.csv","w") as f:
        writer = csv.DictWriter(f, fieldnames = row.keys())
        writer.writeheader()
        writer.writerows(rows)




def extract_displacement(text):
    # Scraping desplacement unit . This does not ahave a span element tage in HTML. Use RegEx
    displacement_str = re.findall(r'.* (\d+.\d+) cubic inches',text)[0]          # [0] index because only the float value, not cubic inches text
    displacement = float(displacement_str)
    # displacement = 0 Test : AssertionError: Expecting a reasonable displacement, not 0
    assert displacement > 60 , f"Expecting a reasonable displacement, not {displacement}"
    return displacement



def extract_territory(cb):
    #Scrapping from (year and territory)
    str_from = cb.find('span',class_="from").get_text()   #str_from : '(1970, USA)'
    #Use strippgin methods and split to remove brackets and comma
    year, territory = str_from.strip('()').split(',')
    year = int(year)
    # year = -1  Test: AssertionError: Expecting year to be positive not -1
    assert year > 0 , f"Expecting year to be positive not {year}"
    territory = territory.strip()
    #territory = 'x'  Test: AssertionError: Expecting territory to be valid territory, not x
    assert len(territory) > 1 , f"Expecting territory to be valid territory, not {territory}"
    return territory,year


def extract_data(cb):
    # Find a class "car_name" fromt a span element and ignore the element tags, and get only text information

    #Scrapping Car names
    str_name = cb.find('span',class_="car_name").get_text()

    #Scrapping Cylinders
    str_cylinders = cb.find('span',class_="cylinders").get_text()
    cylinders = int(str_cylinders)
    # cylinders = -1 Test: Testing the assert values. Sometimes the scraped data will contain invalid values.
    assert cylinders > 0 , f"Expecting cylinders to be positive not {cylinders}"

    #Mapping, car-names to cylinders
    # row = dict(name=str_name,cylinders=cylinders) # dictionary {name:car_name, cylinder:cylinder size}
    # rows.append(row)  # rows becomes a list of dictionarys

    # Scrapping weight
    str_weight = cb.find('span', class_="weight").get_text()
    # weight = int(str_weight)  # Test: Fails as there is comma in the string: ValueError: invalid literal for int() with base 10: '3,504'
    # Remove the comma using replace method of string.
    weight = int(str_weight.replace(',',''))
    assert weight > 0 , f"Expecting weight to be positive not {weight}"

    #Scrapping territory,year
    territory, year = extract_territory(cb)

    #Scraping acceleration
    acceleration =  float(cb.find('span',class_="acceleration").get_text())
    assert acceleration > 0 , f"Expecting acceleration to be positive"

    #Miles Per Gallon (mpg)
    mpg_str = cb.find('span',class_="mpg").get_text() # '18.0 mpg'
    # To encounter the missing values
    try:
        mpg = float(mpg_str.split(' ')[0])         # Getting only the first value and converiting to float
        # mpg = 0 Test:  AssertionError: Expecting reasonable mpg, not 0
        assert mpg > 7, f"Expecting reasonable mpg, not {mpg}"

    except ValueError:
        mpg = "NULL"


    #Scraping Horse Power
    hp_str = cb.find('span',class_="horsepower").get_text()  # "130 hp"
    # To encounter the missing values
    try:
        hp = float(hp_str)
        # hp = 0 Test: AssertionError: Expecting reasonable hp, not 0
        assert hp > 7, f"Expecting reasonable hp, not {hp}"

    except ValueError:
        hp = "NULL"

    # Scraping desplacement unit.
    displacement = extract_displacement(cb.text)

    row = dict(name=str_name,
            cylinders=cylinders,
            weight=weight,
            year=year,
            territory=territory,
            acceleration=acceleration,
            mpg=mpg,
            hp=hp,
            displacement=displacement)

    return row


if __name__ == "__main__":
    filename = "scrapped_page_result.pickle"
    # If the pickle file doesn't exist , then the pickle module will fetch the file from the web, and store it.
    # Next time the file is called, it will check the pickle file, without going online.
    if os.path.exists(filename):
        with open(filename,'rb') as f:
            print(f"Loading Cached {filename}")
            result = pickle.load(f)
    else:
        print(f"Fetching {PAGE} from internet")
        result = requests.get(PAGE)
        with open(filename,'wb') as f:
            print(f"Writing Cached {filename}")
            pickle.dump(result,f)
    assert result.status_code == 200, f"Got status code : {result.status_code} which isn't a success"
    # Cannot use get_text() here, since this is an object of requests, and not of BeautifulSoup
    source = result.text
    soup = BeautifulSoup(source, 'html.parser')
    process_car_blocks(soup)
