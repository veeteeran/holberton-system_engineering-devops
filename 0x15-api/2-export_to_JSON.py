#!/usr/bin/python3
""" Building on task 0, export data in the CSV format"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    name_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    names = get(name_url).json()
    todos = get(todo_url)

    output_dict = {}
    write_list = []
    wl_dict = {}
    for todo in todos.json():
        wl_dict.update({"task": todo.get("title")})
        wl_dict.update({"completed": todo.get("completed")})
        wl_dict.update({"username": names.get("username")})
        write_list.append(wl_dict)
        wl_dict = {}

    output_dict.update({names.get("id"): write_list})

    filename = "{}.json".format(argv[1])
    with open(filename, 'w') as file:
        json.dump(output_dict, file)
