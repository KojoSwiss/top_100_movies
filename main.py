import requests
from bs4 import BeautifulSoup

URL = "https://serv-gh.herokuapp.com/tasks"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_listings = soup.select(selector=".index-content-card p a")

my_services = ''

listings = [listing.getText() for listing in all_listings]

for service in listings:
    if service != '0':
        my_services += f'{service}\n'


with open('My Listings.txt', 'w') as content:
    content.write(my_services)
