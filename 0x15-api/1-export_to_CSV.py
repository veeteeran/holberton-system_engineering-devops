#!/usr/bin/python3
""" Building on task 0, export data in the CSV format"""
import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    name_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    names = get(name_url).json()
    todos = get(todo_url)
    filename = "{}.csv".format(argv[1])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        write_list = []

        for todo in todos.json():
            write_list.append(names.get("id"))
            write_list.append(names.get("username"))
            write_list.append(todo.get("completed"))
            write_list.append(todo.get("title"))
            writer.writerow(write_list)
            write_list = []
