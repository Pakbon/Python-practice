import requests
import feedparser
import smtplib
import json

from bs4 import BeautifulSoup as bs
from email.message import EmailMessage

with open('announcements.json') as config:
    config = json.loads(config.read())

def main():
    articledict = parsing()
    mail(articledict)

def parsing():
    url = config['rsslinks'][0]
    newsfeed = feedparser.parse(url)
    soup = bs(newsfeed['entries'][2]['summary'], features='html.parser')
    articledict = {}
    articledict['articlelink'] = newsfeed.entries[0]['links'][0]['href']
    articledict['title'] = newsfeed.entries[0]['title']
    articledict['games'] = {}
    articledict['bundlelink'] = soup.contents[0].text

    test = soup.select('.bb_ul')
    gamelinks = test[0].find_all('a', 'bb_link')
    gamedict = []
    for items in gamelinks:
        game = items.contents[0]
        link = items.get('href')
        try:
            items.contents[1]
            stc = 1
        except IndexError:
            stc = 0
        gamedict += [{'game' : game, 'link' : link, 'stc' : stc}]
    articledict['games'] = gamedict
    return articledict

def mail(articledict):
    msg = EmailMessage()
    msg['Subject'] = articledict['title']
    msg['from'] = config['from']
    msg['to'] = config['to']
    content = 'Bundlelink: {}\n'.format(articledict['bundlelink'])
    content += 'Game, has cards?\n\n'
    for game in articledict['games']:
        content += '{},{} : {}\n'.format(game['stc'], game['game'], game['link'])
    msg.set_content(content)

    with smtplib.SMTP(config['smtpserver'], config['smtpport']) as smtpobj:
        smtpobj.ehlo()
        smtpobj.send_message(msg)


if __name__ == '__main__':
    main()
