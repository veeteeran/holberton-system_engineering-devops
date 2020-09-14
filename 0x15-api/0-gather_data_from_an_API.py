#!/usr/bin/python3
""" for a given employee ID, returns information about TODO list progress """
from sys import argv
from requests import get

if __name__ == "__main__":
    name_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    EMPLOYEE_NAME = get(name_url).json().get("name")
    todos = get(todo_url)
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(todos.json())
    completed_list = []

    for todo in todos.json():
        if todo.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            completed_list.append(todo.get("title"))

    line_1 = "Employee {} is done with tasks({}/{}):".format(
                EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    print(line_1)

    for complete in completed_list:
        print("\t{}".format(complete))
