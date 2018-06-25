#!/usr/bin/python3
# -*- coding: utf-8 -*-
#filename: utf-8.py


def normalize(name):
	return name.capitalize()

#test

L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)
