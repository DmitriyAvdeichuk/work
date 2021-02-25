import pymysql.cursors
import yaml
import datetime

with open('d:/python practice/testtask/games.yaml') as file:
    a = yaml.load(file, Loader=yaml.FullLoader)

lst = []

for i in a.values():
    lst = i

list_with_values = []

for elem in lst:
    for values in elem.values():
        if type(values) == datetime.date:
            values = int(str(values).replace('-', ''))
        list_with_values.append(values)

chunked = list(list_with_values[i:i + 3] for i in range(0, len(list_with_values), 3))

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='37661600zz',
                             db='helloworld',
                             charset='utf8')

cursor = connection.cursor()
for element in range(0, int(len(list_with_values) / 3), 3):
    request = ("INSERT games(game_id, name, date) VALUES (%s, %s, %s)")
    cursor.executemany(request, chunked)
connection.commit()

cursor.close()

connection.close()

