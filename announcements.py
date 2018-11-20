'''keeps track of rss feeds within a steamgroup and sends a mail on new 
announcement'''

import requests
import shelve
import json
import feedparser
import smtplib
import re

from bs4 import BeautifulSoup as bs
from email.message import EmailMessage

with open('files/announcements.json') as file:
    config = json.loads(file.read())


def main():
    announcement = parsing()
    details(announcement)
    return 0


def parsing(entry=0):
    'parse rss feed. Defaults to first item returned. entry=0'
    url = config['rsslink']
    fetched = requests.get(url)
    soup = bs(fetched.text, features='html.parser')
    items = soup.find_all('item')
    return items[entry]


def details(announcement):
    'checks whether title is in list in announcements.json and parse details'
    for names in config['bundlename']:
        regex = re.compile(names, re.IGNORECASE)
        title = announcement.title.text
        if regex.search(title):
            if saving(title) == 0:
                mail(announcement)
            else:
                # already existing
                return
        else:
            continue


def saving(title):
    file = shelve.open('files/announcements.shv')
    try:
        if title in file['announcements']:
            return 1
    except KeyError:
        try:
            file['announcements'] += [title]
            return 0
        except KeyError:
            file['announcements'] = [title]
            return 0


def mail(announcement):
    msg = EmailMessage()
    msg.set_content(announcement.guid.text)
    msg['Subject'] = announcement.title.text
    msg['From'] = config['from']
    msg['To'] = config['to']

    smtpconnect = smtplib.SMTP(
        host=config['smtpserver'], port=config['smtpport'])
    smtpconnect.send_message(msg)
    smtpconnect.quit()


if __name__ == '__main__':
    main()
