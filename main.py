import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")
all_movies = [movies.getText() for movies in soup.find_all(name="h3", class_="title")]
print(all_movies)

print(all_movies[0])
with open("movie.txt", "w",encoding="utf-8") as file:
    for movie in all_movies[::-1]:
        file.writelines("\n"+ movie)