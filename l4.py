import pandas as pd
# download csv from https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
csv_file=pd.read_csv('cities.csv')

print(csv_file.head())

import requests

# this is a public GitHub API endpoint that lists repositories of a user
url = 'https://api.github.com/users/EveWangUW/repos'

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Select only the first 3 responses
    first_1_repos = data[:1]
    # Print each response on a new line
    for repo in first_1_repos:
        print(repo)
        print('\n')  # Add a new line between responses
else:
    # If the request was not successful, print the status code
    print(f"Error: {response.status_code}")


import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://en.wikipedia.org/wiki/Harry_Potter'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Get the first 10 lines of the HTML
first_5_lines = '\n'.join(str(line) for line in soup.prettify().split('\n')[:5])

# Print the first 10 lines of the HTML
print(first_5_lines)
