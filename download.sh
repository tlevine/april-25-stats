#!/bin/sh

cd 'april-25-stats-downloads'
../wsync/wsync 'https://api.meetup.com/2/rsvps?key=803940432c422f755061152b71458030&sign=true&event_id=112727792&page=300' datakind json
../wsync/wsync 'https://api.meetup.com/2/rsvps?key=803940432c422f755061152b71458030&sign=true&event_id=112271042&page=300' nyhackr  json
