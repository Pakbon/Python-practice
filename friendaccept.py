import requests
from bs4 import BeautifulSoup as bs
import json
import re
import time
import logging
from steam import webauth

import functions

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start')

api_url = 'http://api.steampowered.com/'

def main():
    'run program'
    session = functions.login()
    fl_pending = souping(session)
    accept(fl_pending, session)


def souping(session):
    #if cookies not set by login():
    file = functions.load_id()
    r = session.get(f'https://steamcommunity.com/id/{file["vanityurl"]}/friends/pending')
    #else:
    #get cookies
    soup = bs(r.text)
    fl_pending = soup.select('.invite_row')
    logging.debug('pending invites:')
    logging.debug(len(fl_pending))
    return fl_pending

def accept(fl_pending, session):
    file = functions.load_id()
    url = f'https://steamcommunity.com/id/{file["vanityurl"]}/friends/action'
    apikey = file['apikey']
    for i in fl_pending:
        attrs = i.attrs
        post = {
            'sessionid' : session.cookies.get('sessionid', domain='steamcommunity.com'),
            'steamid' : file['steam64'],
            'ajax' : '1',
            'action' : 'accept',
            'steamids[]' : attrs['data-steamid']
        } 
        logging.debug(post)
        session.post(url, data=post)
        r = requests.get(api_url+'ISteamUser/GetPlayerSummaries/v0002/?key='+apikey+'&steamids='+attrs['data-steamid'])
        other_profile = r.json()
        other_name = other_profile['response']['players'][0]['personaname']
        functions.post_comment('adding me as a friend', other_name, attrs['data-steamid'], session)

if __name__ == '__main__':
    main()