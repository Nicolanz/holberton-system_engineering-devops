#!/usr/bin/python3
"""Records all tasks from all employees in JSON format"""
import json
import requests
import sys

if __name__ == "__main__":

    new_dict = {}
    lista = []
    url = 'https://jsonplaceholder.typicode.com/users'
    allUsers = json.loads(requests.get(url).text)

    for i in range(1, len(allUsers) + 1):
        obj = json.loads(requests.get('{}/{}/todos'.format(url, i)).text)
        username = json.loads(requests.get("{}/{}".format(
            url, i)).text)['username']
        filename = json.loads(requests.get("{}/{}/todos".format(
            url, i)).text)[0]['userId']

        for j in obj:
            lista.append({
                "username": username
                "task": j['title'],
                "completed": j["completed"],
            })

        new_dict[filename] = lista
        lista = []

    with open('todo_all_employees.json'.format(filename), mode="w") as file:
        new_dict[filename] = lista
        json.dump(new_dict, file)
