#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":

    new_dict = {}
    lista = []
    url = 'https://jsonplaceholder.typicode.com/users'

    obj = json.loads(requests.get('{}/{}/todos'.format(url, sys.argv[1])).text)

    username = json.loads(requests.get("{}/{}".format(
        url,
        sys.argv[1]
    )).text)['username']
    filename = json.loads(requests.get("{}/{}/todos".format(
        url,
        sys.argv[1]
    )).text)[0]['userId']

    for i in obj:
        lista.append({
            "task": i['title'],
            "completed": i["completed"],
            "username": username
            })

    with open('{}.json'.format(filename), mode="w") as file:
        new_dict[filename] = lista
        json.dump(new_dict, file)
