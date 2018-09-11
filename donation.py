'''commentaar geven op profile'''

import json
import requests
from bs4 import BeautifulSoup as bs
from boosterpack import trades
import time

import functions




file = functions.load_id()
api_url = 'http://api.steampowered.com/'
apikey = file['apikey']
steamid = file['steam64']
steam_exceptions = file['exceptions']


def main():
    Donation()

def Donation():
    'donations will get a comment on own and their steamprofile'
    history = trades(func=1)
    session = functions.login()
    for array in history['response']['trades']:
        try:
            array['assets_given']
        except:
            #this is a donation
            #find out the user, the item traded
            other_steamid = array['steamid_other']
            #add exceptions to steamid
            if int(other_steamid) in steam_exceptions:
                continue
            r = requests.get(api_url+'ISteamUser/GetPlayerSummaries/v0002/?key='+apikey+'&steamids='+other_steamid)
            other_profile = r.json()
            other_name = other_profile['response']['players'][0]['personaname']
            functions.post_comment('donating', other_name, other_steamid, session)


if __name__ == '__main__':
    main()