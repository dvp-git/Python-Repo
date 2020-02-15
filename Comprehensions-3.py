# Dictionary comprehensions
from pprint import pprint as pp

# General form  : {key_expr: value_expr for item in iterable}

country_to_capital = {
                      'UK':'London',
                      'Brazil':'Brazila',
                      'Morocco':'Rabat',
                      'Swedan':'Stockholm'
                      }
capital_to_country = {capital : country for country,capital in country_to_capital.items() }

pp(country_to_capital)
pp(capital_to_country)


""" Practical example:
import os
import glob
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)
"""
