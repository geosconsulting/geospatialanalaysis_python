# -*- coding: utf-8 -*-
"""
Created on Sat Feb 08 15:37:23 2014

@author: Fabio
"""

import urllib

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"
earthquakes= urllib.urlopen(url)
earthquakes.readline()

for record in earthquakes:
    print record