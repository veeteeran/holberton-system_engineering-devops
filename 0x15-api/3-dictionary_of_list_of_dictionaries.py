#!/usr/bin/python3
""" Building on task 0, export data in the CSV format"""
from requests import get
import json

if __name__ == "__main__":
    name_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    names = get(name_url).json()
    todos = get(todo_url)

    output_dict = {}
    write_list = []
    wl_dict = {}
    user = 1
    for name in names:
        for todo in todos.json():
            if user == todo.get("userId"):
                wl_dict.update({"task": todo.get("title")})
                wl_dict.update({"completed": todo.get("completed")})
                wl_dict.update({"username": name.get("username")})
                write_list.append(wl_dict)
                wl_dict = {}

        output_dict.update({name.get("id"): write_list})
        write_list = []
        user += 1

    with open('todo_all_employees.json', 'w') as file:
        json.dump(output_dict, file)
