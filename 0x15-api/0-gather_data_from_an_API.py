#!/usr/bin/python3
""" gather data from api """
import requests
from sys import argv


if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    
    emp_id = argv[1]
    todo = requests.get(url_todo, params={'userID': emp_id})
    user = requests.get(url_user, params={'id': emp_id})
    todo_list = todo.json()
    
    user_list = user.json()
    tasks = []
    all_tasks = len(todo_list)
    employee = user_list[0].get('name')

    for t in todo_list:
        if t.get('completed') is True:
            tasks.append(t)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(tasks), all_tasks))

    for t in tasks:
        print("\t {}".format(t.get('title')))
