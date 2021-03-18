from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data, 'html.parser')

movie_titles = soup.find_all(name='h3', class_='jsx-4245974604')
print(movie_titles)