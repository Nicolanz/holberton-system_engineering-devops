#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":

    new_dict = {}
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

    with open('{}.json'.format(filename), mode="a") as file:

        for i in obj:
            new_dict.update({filename: [{
                "task": i['title'],
                "completed": i["completed"],
                "username": username
            }]})
            json.dump(new_dict, file)
