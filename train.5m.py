#!/usr/local/bin/python2
from lxml import html
from datetime import datetime
import requests
import string
# These are the trains you wish you track
TRAINS = [
  'http://www.realtimetrains.co.uk/train/Y60840/',
  'http://www.realtimetrains.co.uk/train/Y61226/',
  'http://www.realtimetrains.co.uk/train/Y03218/',
]

date = datetime.now()
datestring = date.strftime('%Y/%m/%d')

delays = []
shorts = []


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


for train in TRAINS:
    url = '{}{}'.format(train, datestring)  # 2016/09/22
    page = requests.get(url)
    tree = html.fromstring(page.content)
    delay = tree.xpath('//td[@class="delay"]/text()')

    delays.append('{}|href={}'.format(delay[-1], url))
    shorts.append(get_status(delay))


print ':'.join(shorts)
print '---'
for delay in delays:
    print delay
