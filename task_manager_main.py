from tasks import *
import os
from sorting import *

if __name__ == "__main__":
    the_menu = {
    "P" : "Print tasks",
    "A" : "Add a task",
    "U" : "Update a task",
    "D" : "Delete a task",
    "SI" : "Show incomplete tasks", 
    "SC" : "Show completed tasks", 
    "SP" : "Show tasks sorted by priority, highest first",
    "SD" : "Show tasks sorted by due date, earliest first",
    "S" : "Save tasks",
    "L" : "Load tasks from file",
    "Q" : "Quit this program"
        }
    tasks_list = [
        {
        'name': 'Return books',
        'description': 'Need to return some books to the library',
        'deadline': '04/14/2022',
        'priority': 4,
        'completed': False
        },
        {
        'name': 'get groceries',
        'description': 'buy some jam and peanut butter',
        'deadline': '02/23/2022',
        'priority': 2,
        'completed': False
        },
        {
        'name': 'get some sleep',
        'description': '8 hours of sleep is necessary',
        'deadline': '02/03/2022',
        'priority': 3,
        'completed': False
        },
        {
        'name': 'lit essay',
        'description': "finish comparative lit essay that's overdue",
        'deadline': '02/15/2022',
        'priority': 4,
        'completed': True
        }
            ]
    opt = None

    while True:
        print_main_menu(the_menu)
        print("::: Enter an option")
        opt = input("> ")

        if opt == "Q" or opt == "q" : 
            print("See you next time!")
            break 
        else:
            if check_option(opt, the_menu) == "invalid": 
                print(f"WARNING: `{opt}` is an invalid option.\n")
                continue
            print(f"You selected option {opt} to > {the_menu[opt.upper()]}.\n")

        if opt == "P" or opt == "p" : 
            print_formatted_tasks(tasks_list)
        
        elif opt == "A" or opt == "a": 
            task_fields = ["name", "description", "due date", "priority", "completed"]
            response = []
            for field in task_fields:
                if field == "name":
                    print(f"Enter a task name between 3 and 15 characters:")
                    value = input()
                    response.append(value)
                elif field == "description":
                    print(f"Enter a Description:")
                    value = input()
                    response.append(value)
                elif field == "due date":
                    print(f"Enter a due date in the MM/DD/YYYY Format")
                    value = input()
                    response.append(value)
                elif field == "priority":
                    print(f"Enter a prioirty number 1-5, with 5 being the highest Priority")
                    value = input()
                    response.append(value)
                elif field == "completed":
                    print(f"Enter Yes or No on whether this task is completed or not")
                    value = input()
                    response.append(value)
            temp_dict = (create_task(task_fields, response))
            task_status = create_a_task(temp_dict['name'], temp_dict['description'], temp_dict['due date'], temp_dict['priority'], temp_dict['completed'])
            if task_status[0] == False:
                print(f"WARNING: invalid input entered for the `{task_status[1]}` field.\n")
            elif task_status[0] == True:
                tasks_list.append(task_status[1])
                print("Task succesfully added!")

        elif opt == "U" or opt == "u": 
            update_info = []
            print("Provide the index of the task from the task list that you would like to update:")
            index = input("> ")
            update_info.append(index)
            print("Provide the field of the task that you would like to update in all lowercase letters:")
            field = input("> ")
            update_info.append(field)
            if field == "name":
                print(f"Please enter a name that is between 3 and 15 characters long:")
                update = input("> ")
                update_info.append(update)
            if field == "description":
                print(f"Please enter a description:")
                update = input("> ")
                update_info.append(update)
            if field == "deadline":
                print(f"Please enter a date in MM/DD/YYYY format:")
                update = input("> ")
                update_info.append(update)
            if field == "priority":
                print(f"Please enter a number between 1 and 5:")
                update = input("> ")
                update_info.append(update)
            if field == "completed":
                print(f"Please enter yes or no:")
                update = input("> ")
                update_info.append(update)
                
            result = update_task(tasks_list, int(update_info[0]), update_info[1], update_info[2])
            if result[0] == False:
                if result[1] == "idx":
                    print(f"WARNING: invalid index entered.\n")
                elif result[1] == "field":
                    print(f"WARNING: invalid field type entered.\n")
                elif result[1] == "name":
                    print(f"WARNING: invalid input for name.\n")
                elif result[1] == "description":
                    print(f"WARNING: invalid input for description.\n")
                elif result[1] == "deadline":
                    print(f"WARNING: invalid input for deadline.\n")
                elif result[1] == "priority":
                    print(f"WARNING: invalid input for priority.\n")
                elif result[1] == "completed":
                    print(f"WARNING: invalid input for completed.\n")
                    
            elif result[0] == True:
                print(f'Task {index} succesfully updated {field} to {update}!')

        elif opt == "D" or opt == "d": 
            print(f"Please type the index of the task you wish to delete:")
            index = int(input(">"))
            print()
            if delete_task(int(index), tasks_list) == True:
                print(f'There are now only {len(tasks_list)} tasks in the task list.')
                print()
            elif delete_task(int(index), tasks_list) == False:
                print(f"WARNING: index not valid for task list.\n")

        elif opt == "SI" or opt == "si": 
            print_tasks_by_status(tasks_list, False)

        elif opt == "SC" or opt == "sc": 
            print_tasks_by_status(tasks_list, True)

        elif opt == "SP" or opt == "sp":
            print_sorted_priority(tasks_list)
            print()

        elif opt == "SD" or opt == "sd":
            print_sorted_deadline(tasks_list)

        elif opt == "S" or opt == "s":
            print("Please write what you would like your CSV file to be titled (please include .csv at the end)")
            file_name = input()
            if ".csv" not in file_name:
                print(f"WARNING: please include .csv when writing the file title.")
            else:
                save_to_csv(tasks_list, file_name)
                print(f"Tasks saved to a '{file_name}'")

        elif opt == "L" or opt == "l":
            print("Please enter a csv file to load from:")
            load_name = input(">")
            if ".csv" not in load_name:
                print(f"WARNING: please include .csv when writing the file title.") 
            
            result = os.path.isfile(load_name)
            if result == True:
                print()
                load_from_csv(load_name)
                print()
                print(f"Tasks succesfully loaded from {load_name}")
                print()
            elif result == False:
                print(f"WARNING: Cannot find a CSV file named '{load_name}'")
        
            
        
        else:
            print("This option is not yet implemented.") 

        opt = input("::: Press Enter to continue...")

    print("Have a productive day!")
