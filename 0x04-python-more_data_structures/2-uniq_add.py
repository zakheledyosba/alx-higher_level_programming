#!/usr/bin/python3

def uniq_add(my_list=[]):
    results = 0

    for  i in set(my_list):
        results += i
    return (results)
