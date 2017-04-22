#!/usr/local/bin/python2
from lxml import html
from datetime import datetime
import requests
import string

# <bitbar.title>Train Tracker</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Daniel Parker</bitbar.author>
# <bitbar.author.github>danpker</bitbar.author.github>
# <bitbar.desc>Display the status of your train(s)</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

# These are the trains you wish you track
TRAINS = [
  'http://www.realtimetrains.co.uk/train/Y60840/',
  'http://www.realtimetrains.co.uk/train/Y61226/',
  'http://www.realtimetrains.co.uk/train/Y03218/',
]

date = datetime.now()
datestring = date.strftime('%Y/%m/%d')

long_statuses = []
short_statuses = []


def get_status(statuses):
    """Given a list of status, get the last one
    And convert into a shorter format"""
    return shorten(statuses[-1])


def shorten(message):
    """Convert message into a shorter form"""
    if message == 'On time':
        return '0'

    number = message.translate(None, string.ascii_letters).strip()
    sign = '+' if 'late' in message else '-'

    return '{}{}'.format(sign, number)


def main():

    for train in TRAINS:
        url = '{}{}'.format(train, datestring)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        delay = tree.xpath('//td[@class="delay"]/text()')

        long_statuses.append('{}|href={}'.format(delay[-1], url))
        short_statuses.append(get_status(delay))

    print('/'.join(short_statuses))

    print('---')
    for status in long_statuses:
        print(status)


if __name__ == '__main__':
    main()
