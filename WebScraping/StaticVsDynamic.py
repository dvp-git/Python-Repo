# Demo of static vs Dynamic pages:

# Static : https://en-gb.wordpress.org/plugins/browse/popular/
# Dynamic ( Uses JavaScript engine while loading) :https://www.google.com/

import requests
result_static = requests.get("https://en-gb.wordpress.org/plugins/browse/popular/")

with open('wordpress.html','w') as fileObj:
    fileObj.write(result_static.text)


result_dynamic = requests.get("https://google.com")

with open('google.html','w') as fileObj:
    fileObj.write(result_dynamic.text)


# DataPlaybook> wget -O google_wget.html "https://google.com"
# PS C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\WebScraping_DataPlaybook>
