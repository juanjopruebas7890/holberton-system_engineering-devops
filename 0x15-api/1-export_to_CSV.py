#!/usr/bin/python3
""" csv export data """
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    emp_id = argv[1]
    todo = requests.get(url_todo, params={'userID': emp_id})
    user = requests.get(url_user, params={'id': emp_id})
    todo_list = todo.json()
    user_list = user.json()
    employee = user_list[0].get('name')

    with open("{}.csv".format(emp_id), "a+") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo_list:
            st = t['completed']
            title = t['title']
            csvwriter.writerow(["{}".format(emp_id),
                                "{}".format(employee),
                                "{}".format(st),
                                "{}".format(title)])
