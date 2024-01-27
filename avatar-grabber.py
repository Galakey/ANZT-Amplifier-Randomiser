import time
import requests
import os
import csv

urlprefix = 'https://a.ppy.sh/'
directory = 'data/teams'
apiKey = 'ba71704f528f2fc288bb0dda61f07905431c95b1'
invalid_chars = [':', '?', '*', '"', '<', '>', '|', '/']


with open("teams.txt") as f:
    # Filters out any empty lines
    ids = list(filter(None, (line.rstrip() for line in f)))

for i, id in enumerate(ids):
    team, matchblock, id1, rank1, id2, rank2 = id.split(',')
    team_rank = int(rank1) + int(rank2)
    req = requests.get(f'https://osu.ppy.sh/api/get_user?k={apiKey}&u={id1}&m=0')
    if req.status_code != 200:
        print('\rSomething went wrong getting info for', id1)
        continue
    user_info1 = req.json()[0]
    username1, user_id1 = user_info1['username'], user_info1['user_id']

    req = requests.get(f'https://osu.ppy.sh/api/get_user?k={apiKey}&u={id2}&m=0')
    if req.status_code != 200:
        print('\rSomething went wrong getting info for', id2)
        continue
    user_info2 = req.json()[0]
    username2, user_id2 = user_info2['username'], user_info2['user_id']

    img_data1 = requests.get(urlprefix + user_id1).content
    img_data2 = requests.get(urlprefix + user_id2).content

    cleansed_team = team
    for char in invalid_chars:
        cleansed_team = cleansed_team.replace(char, '_')

    os.mkdir(f'{directory}/{team_rank}${matchblock}${cleansed_team}')

    with open(f'{directory}/{team_rank}${matchblock}${cleansed_team}/{rank1}${username1}.jpg', 'wb') as handler:
        handler.write(img_data1)
    with open(f'{directory}/{team_rank}${matchblock}${cleansed_team}/{rank2}${username2}.jpg', 'wb') as handler:
        handler.write(img_data2)

    print(f'\r[{i + 1}/{len(ids)}]', end='')
    time.sleep(1)