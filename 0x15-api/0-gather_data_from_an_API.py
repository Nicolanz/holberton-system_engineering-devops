#!/usr/bin/python3
"""Returns information about list progress of employee"""
import json
import requests
import sys

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users'
    tasks_done = 0
    lista = []

    try:
        name = json.loads(requests.get("{}/{}".format(
            url, sys.argv[1])).text)['name']
        obj = json.loads(requests.get('{}/{}/todos'.format(
            url, sys.argv[1])).text)
    except:
        sys.exit(1)
    
    for i in obj:
        if i['completed'] == True:
            tasks_done = tasks_done + 1
            lista.append(i['title'])

    print("Employee {} is done with tasks({}/{}):".format(
        name,
        tasks_done,
        len(obj)
    ))
    for i in lista:
        print("\t {}".format(i))
