#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:30:47 2019

@author: Yssubhi
"""

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similar("Cult is an energy drink with a lot of caffiene and it helps you stay energized through out the day","Cult A / S is a Danish company with headquarters in Lystrup near Aarhus. The company produces energy drinks and cider products with and without alcohol. The company's best-known and sold drinks are CULT Shaker, Cult Raw Energy and Mokaï."))
