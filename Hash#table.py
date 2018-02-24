# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:56:38 2018

Author: hamdymostafa

A simple implementation of a hash table in Python that avoids collision.
"""



table = [ [] for _ in range(10)]

def hashing_function(key):
    # input: key
    # output: index
    
    return key%10


def insert(table,key,value):
    
    table[hashing_function(key)].append(value)
    
