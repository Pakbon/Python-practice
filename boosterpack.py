'''Checks Steam inventory for boosterpacks and writes to csv.
Expects id.txt to be in the same folder with {"steam64" : <steam64id>}
'''

import json, requests, re, datetime, csv

def main():
    'call and pass around data between functions'
    data=ScrapeInventory()
    bpacks,bpack_counter=FindBpacks(data)
    write_data(bpacks,bpack_counter)


def ScrapeInventory():
    'find profile from file'
    #boosterpack.txt profile id
    with open('id.txt') as input:
        j=json.loads(input.read())
        url='https://steamcommunity.com/inventory/{}/753/6'.format(j['steam64'])
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
        r=requests.get(url, headers=header)
        return r.text

def FindBpacks(data):
    'jsonize and find boosterpacks, using the name and regex magic'
    data=json.loads(data)
    regex=re.compile(r'.*Booster Pack')
    lijstje=[]
    counter=0
    for i in data['descriptions']:
        found=regex.search(i['name'])
        if found==None:
            break
        else:
            lijstje+=[found.group()]
            counter+=1
    return(lijstje, counter)


def write_data(lijstje,counter):
    'write data to sql/rrd/plaintext/csv'
    dt=datetime.date.today()
    dt.strftime('%Y-%m-%d')
    with open('boosterpacks.csv','a', newline='') as output:
        writer=csv.writer(output)
        writer.writerow([dt.strftime("%Y-%m-%d"), lijstje, counter])

if __name__=='__main__':
    main()
