#!/usr/bin/python3
"""For a given employee ID, returns information
about his/her TODO list progress"""
import json
import requests
import sys

if __name__ == "__main__":
    num = 0
    lista = []
    url = 'https://jsonplaceholder.typicode.com/users'

    name = json.loads(requests.get('{}/{}'.format(
        url, sys.argv[1])).text)['name']

    obj = requests.get('{}/{}/todos'.format(url, sys.argv[1]))

    for i in json.loads(obj.text):
        if i['completed'] is True:
            num = num + 1
            lista.append(i['title'])

    print("Employee {} is done with tasks ({}/{})".format(
        name,
        num,
        len(json.loads(obj.text))
    ))
    for i in lista:
        print("\t {}".format(i))
