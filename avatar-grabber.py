import time
import requests
import os
import csv

urlprefix = 'https://a.ppy.sh/'
directory = 'data/players'
apiKey = 'ba71704f528f2fc288bb0dda61f07905431c95b1'

with open("data/players.txt") as f:
    # Filters out any empty lines
    ids = list(filter(None, (line.rstrip() for line in f)))

for i, id in enumerate(ids):
    req = requests.get(f'https://osu.ppy.sh/api/get_user?k={apiKey}&u={id}&m=0')
    if req.status_code != 200:
        print('\rSomething went wrong getting info for', id)
        continue
    user_info = req.json()[0]
    username, user_id = user_info['username'], user_info['user_id']

    img_data = requests.get(urlprefix + user_id).content
    if i + 1 < 10:
        i = "0" + str(i + 1)
    else:
        i = i + 1
    with open(f'{directory}/{i}${username}.jpg', 'wb') as handler:
        handler.write(img_data)

    print(f'\r[{i}/{len(ids)}]', end='')