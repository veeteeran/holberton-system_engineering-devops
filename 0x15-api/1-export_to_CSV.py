#!/usr/bin/python3
""" Building on task 0, export data in the CSV format"""
from sys import argv
import csv
from requests import get

if __name__ == "__main__":
    name_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    names = get(name_url).json()
    todos = get(todo_url)

    with open('USER_ID.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        write_list = []

        for todo in todos.json():
            write_list.append(names.get("id"))
            write_list.append(names.get("username"))
            write_list.append(todo.get("completed"))
            write_list.append(todo.get("title"))
            writer.writerow(write_list)
            write_list = []
