from tasks import *

def print_sorted_priority(all_tasks):
    """
    Prints tasks from all_tasks, but sorted by priority,
    highest priority first
    """
    temp_list = []
    for dictionary in all_tasks:
        if dictionary['priority'] == 5:
            print(f'"{dictionary["name"].upper()}" is of {priority_message(dictionary["priority"])} priority: {dictionary["priority"]}')
            temp_list.append(dictionary)

    for dictionary in all_tasks:
        if dictionary['priority'] == 4:
            print(f'"{dictionary["name"].upper()}" is of {priority_message(dictionary["priority"])} priority: {dictionary["priority"]}')
            temp_list.append(dictionary)

    for dictionary in all_tasks:
        if dictionary['priority'] == 3:
            print(f'"{dictionary["name"].upper()}" is of {priority_message(dictionary["priority"])} priority: {dictionary["priority"]}')
            temp_list.append(dictionary)

    for dictionary in all_tasks:
        if dictionary['priority'] == 2:
            print(f'"{dictionary["name"].upper()}" is of {priority_message(dictionary["priority"])} priority: {dictionary["priority"]}')
            temp_list.append(dictionary)

    for dictionary in all_tasks:
        if dictionary['priority'] == 1:
            print(f'"{dictionary["name"].upper()}" is of {priority_message(dictionary["priority"])} priority: {dictionary["priority"]}')
            temp_list.append(dictionary)
    print()
    print_formatted_tasks(temp_list)


def print_sorted_deadline(all_tasks):
    """
    Prints tasks from all_tasks, but sorted by deadline
    earliest first
    """
    deadlines = []
    task_and_date = {}
    for dictionary in all_tasks:
        deadlines.append(dictionary["deadline"])
        task_and_date[dictionary["deadline"]] = dictionary["name"]
        
    
    deadlines.sort()
    for task in deadlines:
        print(f'{task_and_date[task].upper()} is due on {task}.')
        print()

