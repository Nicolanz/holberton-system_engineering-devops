#!/usr/bin/python3
"""Export data in the CSV format"""
import csv
import json
import requests
import sys

if __name__ == "__main__":

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

    with open('{}.csv'.format(filename), mode='w') as file:

        csv_file = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in obj:
            csv_file.writerow([filename, username, i['completed'], i['title']])
