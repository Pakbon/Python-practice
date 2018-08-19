'''Checks Steam inventory for boosterpacks and writes to csv.
Expects id.txt to be in the same folder with data:
{"steam64" : "<steam64id>", "bot":"<botname>", "apikey":"<steamapikey>"}
where bot= botname as is known in ASF
'''

import json, requests, re, datetime, csv

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
day=datetime.datetime.now()
day=day.replace(hour=0,minute=1,second=0,microsecond=0)-datetime.timedelta(1) #we want to track YESTERDAY's haul

def main():
    b,c=bpacks()
    try:
        t=trades()
        write(b,c,t)
    except:
        write(b,c)

def bpacks():
    #scrape inventory
    with open('id.txt') as input:
        j=json.loads(input.read())
        url='https://steamcommunity.com/inventory/{}/753/6?count=10'.format(j['steam64'])
        r=requests.get(url, headers=header)

    #count boosters
    regex=re.compile(r'.*Booster Pack')
    boosters=[]
    counter=0
    for i in r.json()['descriptions']:
        found=regex.search(i['name'])
        if found==None:
            break
        else:
            boosters+=[found.group()]
            counter+=1
    if len(boosters) == 0:
        boosters=''
    else:
        boosters=', '.join(map(str, boosters))

    #unpack boosterpacks
    with open('id.txt') as input:
        j=json.loads(input.read())
        url='http://127.0.0.1:1242/Api/Command/unpack%20{}'.format(j['bot'])
        r=requests.post(url, data='')
    return(boosters, counter)

def trades():
    with open('id.txt') as input:
        j=json.loads(input.read())
        epoch=day.timestamp()
        url='https://api.steampowered.com/IEconService/GetTradeHistory/v1/'
        args='?key={}&max_trades=500&start_after_time={}&navigating_back=1&include_failed=0'.format(j['apikey'], int(epoch))
        r=requests.get(url+args, headers=header)
        if r.status_code != 200:
            raise Exception('Request failed with {}'.format(r.status_code))
        else:
            return(len(r.json()['response']['trades']))

def write(b,c,t=0):
    with open('bpacks.csv','a', newline='') as output:
            writer=csv.writer(output)
            writer.writerow([day.strftime("%Y-%m-%d"), c, b, t])

if __name__=='__main__':
    main()
