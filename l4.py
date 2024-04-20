# 1. Manually downloading a csv file from a website and load/read it locally
import pandas as pd
# download csv from https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
csv_file=pd.read_csv('cities.csv')

print(csv_file.head())

# 2. Make API calls to the GitHub API endpoints
import requests

# this is a public GitHub API endpoint that lists repositories of a user
url = 'https://api.github.com/users/EveWangUW/repos'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    first_1_repos = data[:1]
    for repo in first_1_repos:
        print(repo)
        print('\n') 
else:
    print(f"Error: {response.status_code}")

# 3. Use the BeautifulSoup library to scrap a website
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Harry_Potter'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

first_5_lines = '\n'.join(str(line) for line in soup.prettify().split('\n')[:5])

print(first_5_lines)
