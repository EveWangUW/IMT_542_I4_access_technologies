# Instructions:
# To run the python code, in the 'IMT_542_I4_access_technologies' folder, open the terminal, run:

### source venv/bin/activate
### python3 IMT_542_I4_access_technologies.py

# And you should be able to see the results printed in the terminal
# (The print results are also saved in the 'IMT_542_I4_access_technologies' folder, with the names 'Print_Result_1.png' and 'Print_Result_2.png'.

# 1. Manually downloading a csv file from a website and load/read it locally
# information structure: csv
# access technologies: Manual file download and read/load
import pandas as pd
# download the 'cities.csv' from https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
csv_file=pd.read_csv('cities.csv')

print("1. Manually downloading a csv file from a website and load/read it locally")
print(csv_file.head())
print('\n')

# pros of the access methodology:
# 1. Manual doowloads allow users to have direct control over the data they acquire. They won't need to rely on information provided by third-party APIs. 
# 2. It is easy to do, even for people without any programming background.
# 3. The CSV file can be accessed offline, allowing the users to access the file without the internet access.

# cons of the access methodology:
# 1. The user needs to manually download the data every time there is an update. It can be quite time-consuming.
# 2. There is potential for human error, since the person may accidently download the wrong file or save it incorrectly, leading to errors in future analytics. 

# 2. Make API calls to the GitHub API endpoints
# information structures: JSON
# access technologies: API connection over HTTP for structured data to the GitHub API endpoints (GitHub website)
import requests

# this is a public GitHub API endpoint that lists repositories of a user
# using my GitHub account: EveWangUW as an example:
url = 'https://api.github.com/users/EveWangUW/repos'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    first_2_repos = data[:2]
    print("2. Make API calls to the GitHub API endpoints")
    for repo in first_2_repos:
        print(repo)
        print('\n') 
else:
    print(f"Error: {response.status_code}")
print('\n') 

# pros of the access methodology:
# 1. The API endpoints provide users with real-time data, ensuring the users can have the most up-to-date information.
# 2. API calls are more automated compared to manual downloads of data, saving time and preventing human error.

# cons of the access methodology:
# 1. API endpoints may have rate limits and users may only be allowed a limited number of requests, leading to access restrictions.
# 2. Making API calls requires technical background, and is more complex compared to the manual download process. 
    
# 3. Use the BeautifulSoup library to scrap a website
# information structures: HTML
# access technologies: library to extract information from a website
import requests
from bs4 import BeautifulSoup

# using the Harry Potter wikipedia page as an example
url = 'https://en.wikipedia.org/wiki/Harry_Potter'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

first_10_lines = '\n'.join(str(line) for line in soup.prettify().split('\n')[:10])

print("3. Use the BeautifulSoup library to scrap a website")
print(first_10_lines)

# pros of the access methodology:
# 1. BeautifulSoup, as a popular web scraping library, has many useful resources and tutorials that can help users learn and improve their scraping abilities. 
# 2. BeautifulSoup is also compatible with many Python libraries and frameworks, allowing users and developers to easily integrate it into projects. 

# cons of the access methodology:
# 1. As a web scraping library, BeautifulSoup relies heavily on the website HTML structure. If the HTML structure changes, the BeautifulSoup scraping code may break and users need to adjust the code based on the new HTML structure.
# 2. If web scraping is conducted without permission from the website, it may violate terms of service or copyright laws. It is important to have the ethical and legal considerations and check with the website before you start scraping. 