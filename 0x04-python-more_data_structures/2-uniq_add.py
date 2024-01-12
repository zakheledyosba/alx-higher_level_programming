#!/usr/bin/python3

def uniq_add(my_list=[]):
    results = 0
    for  x in set(my_list):
        results += x
    return (results)
