#!/usr/bin/python

import datetime
from subprocess import call


i = datetime.datetime.now()

if i.month < 5 and (i.hour > 18 and i.hour < 22):
	call('echo password | sudo -S shutdown -P now', shell=True)