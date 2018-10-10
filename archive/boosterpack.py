'''Checks Steam inventory for boosterpacks and writes to csv.
'''

import json
import requests
import re
import datetime
import csv

import functions


day = datetime.datetime.now()
day = day.replace(hour=0,minute=1,second=0,microsecond=0) - datetime.timedelta(1) #tracking YESTERDAY's haul

file = functions.load_id()

def main():
    boosters, counter=bpacks()
    try:
        comptrades=trades()
        write(boosters, counter, comptrades)
    except:
        write(boosters, counter)

def bpacks():
    #scrape inventory
    url = f'https://steamcommunity.com/inventory/{file["steam64"]}/753/6?count=10'
    resp = requests.get(url)

    #count boosters
    regex = re.compile(r'.*Booster Pack')
    boosters = []
    counter = 0
    for i in resp.json()['descriptions']:
        found = regex.search(i['name'])
        if found == None:
            break
        else:
            boosters += [found.group()]
            counter += 1
    if len(boosters) == 0:
        boosters = ''
    else:
        boosters = ', '.join(map(str, boosters))

    #unpack boosterpacks
    url = f'{file["asfcommand"]}/unpack%20{file["bot"]}'
    requests.post(url, data='')
    return(boosters, counter)

def trades(func=0):
    'if func=0, return amount of trades in a day. func=1 returns jsondict of all trades in a day'
    epoch = day.timestamp()
    url = 'https://api.steampowered.com/IEconService/GetTradeHistory/v1/'
    args = f'?key={file["apikey"]}&max_trades=500&start_after_time={int(epoch)}&navigating_back=1&include_failed=0'
    resp = requests.get(url+args)
    if resp.status_code != 200:
        raise Exception(f'Request failed with {resp.status_code}')
    else:
        if func == 0:
            return len(resp.json()['response']['trades'])
        if func == 1:
            return resp.json()

def write(boosters, counter, comptrades=0):
    with open('bpacks.csv', 'a', newline='') as output:
            writer = csv.writer(output)
            writer.writerow([day.strftime("%Y-%m-%d"), comptrades, counter, boosters])

if __name__ == '__main__':
    main()
