#!/usr/bin/env python2
import os
import json

DIR = 'april-25-stats-downloads'

def members(filename):
    h = open(filename)
    rsvps = json.load(h)
    h.close()
    return set([r['member']['name'] for r in rsvps['results'] if r['response'] == 'yes'])

dk = members(os.path.join(DIR, 'datakind.json'))
r  = members(os.path.join(DIR, 'nyhackr.json'))
i = dk.intersection(r)

print 'Currently attending DataKind: %d people' % len(dk)
print '\n'.join(dk)
print ''

print 'Currently attending nyhackr: %d people' % len(r)
print '\n'.join(r)
print ''

print 'Currently attending both, at the same time: %d people' % len(i)
print '\n'.join(i)
print ''

import re

dk_alltime = set()
r_alltime  = set()
for filename in os.listdir(DIR):
    path = os.path.join(DIR, filename)
    if re.match(r'^nyhackr-.+json$', filename):
        r_alltime = r_alltime.union(members(path))
    elif re.match(r'^datakind-.+json$', filename):
        dk_alltime = dk_alltime.union(members(path))
i_alltime = dk_alltime.intersection(r_alltime)

print 'These people were once listed in each event, not necessarily at the same time (%d people).' % len(i_alltime)
print '\n'.join(i_alltime)
