#!/usr/bin/env python3

from __future__ import print_function
import sys
import os
import requests
import json
import functions
from macros import *
from pprint import pprint

funcNames = ["getMoney"]
nb_funcs = 1

def getMoney(paramTab):
    i = 0
    for param in paramTab:
        print(param)

def getFuncs():
    funcs = []
    funcs.append(getMoney)
    return (funcs)

def mainloop():
    i = 0
    entry = input(entryMsg)
    paramList = entry.split(" ")
    funcArray = getFuncs()
    while (i < nb_funcs and paramList[0] != funcNames[i]):
        i = i + 1
    if (i < nb_funcs):
        funcArray[i](paramList)
