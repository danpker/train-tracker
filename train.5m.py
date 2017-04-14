#!/usr/local/bin/python2
from lxml import html
from datetime import datetime
import requests

TRAINS = [
  'http://www.realtimetrains.co.uk/train/Y60840/',
  'http://www.realtimetrains.co.uk/train/Y61226/',
  'http://www.realtimetrains.co.uk/train/Y03218/',
]

date = datetime.now()
end = date.replace(hour=18, minute=0)
datestring = date.strftime('%Y/%m/%d')

delays = []
shorts = []

for train in TRAINS:
    url = '{}{}'.format(train, datestring)  # 2016/09/22
    page = requests.get(url)
    tree = html.fromstring(page.content)
    delay = tree.xpath('//td[@class="delay"]/text()')

    if len(delay) == 0 or date > end:
        delays.append('')
    else:
        delays.append('{}|href={}'.format(delay[-1], url))

    try:
        if delay[-1] == 'On time' or 'early' in delay[-1]:
            shorts.append('+')
        else:
            shorts.append(delay[-1])
    except:
        shorts.append('+')


print '-'.join(shorts)
print '---'
for delay in delays:
    print delay
