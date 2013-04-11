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

print 'Attending DataKind: %d people' % len(dk)
print '\n'.join(dk)
print ''

print 'Attending nyhackr: %d people' % len(r)
print '\n'.join(r)
print ''

print 'Attending both, at the same time: %d people' % len(i)
print '\n'.join(i)
