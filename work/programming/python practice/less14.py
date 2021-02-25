import requests
from bs4 import BeautifulSoup
import re


class Track:
    def __init__(self, i, name, art):
        self.track_position = str(i)
        self.song_name = name
        self.artist_name = art

    def __str__(self):
        return self.track_position + ' ' + self.song_name + ' ' + self.artist_name


r = requests.get('https://music.yandex.ru/chart/tracks')
content = r.text
soup = BeautifulSoup(content, features="html.parser")
content1 = soup.find_all('div',
                         {'class': 'd-track typo-track d-track_selectable d-track_with-cover d-track_with-chart'})
str_content = str(content1)

soup_1 = BeautifulSoup(str_content, features="html.parser")

list_positions = soup_1.find_all('div', 'd-track__chart-number typo deco-typo')

# print(list_positions)

titles = soup_1.find_all('div', {'class': 'd-track__name'})
singers = soup_1.find_all('div', {'class': 'd-track__meta'})
list_titles = []
list_singers = []
for tags in titles:
    list_titles.append(tags.text)
for song in singers:
    list_singers.append(song.text)

# print(list_titles)
# print(list_singers)

tracks = []

for i, (name, art) in enumerate(zip(list_titles, list_singers)):
    track = Track(i, name, art)
    tracks.append(track)

# print(tracks[0].song_name)

lst = []

# for track in tracks:
#     if re.fullmatch(r'\w+', track.song_name) == None:
#         continue
#     else:
#         lst.append(track)


for track in tracks:
    if len(track.song_name.split()) == 1:
        lst.append(track)

print(lst[0])

# на оснвое  списка tracks другой список у которых название состоит из одного слова
