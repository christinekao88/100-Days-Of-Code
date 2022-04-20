import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())

all_movies = soup.find_all(name="h3",class_="title")
print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]

# reverse order #1 (從名單最末端開始到0)
for n in range(len(movie_titles)-1,-1, -1):
    print(movie_titles[n])

# reverse order #2
print(movie_titles[::-1])

with open("movies.txt",mode="w") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")


