from validate import *
import csv
import os

def print_main_menu(menu):
    '''
    Prints the menu of items in the
    specified format
    '''
    print("**************************")
    print("What would you like to do?")
    for number, action in menu.items():
        print(f'{number} - {action}')
    print("**************************")


def check_option(option, menu):
    """
    Given an option, return "valid" if it is
    of type str and is a valid key in
    the provided collection.
    Otherwise, return "invalid".
    """
    if type(option) == str and option.upper() in menu.keys():
        return "valid"
    else:
        return "invalid"


def print_formatted_tasks(tasks_list):
    """
    Given a list of dictionaries, print all of
    the dictionary keys and their corresponding values
    in the format requested for each dictionary in the list
    """
    for index, task in enumerate(tasks_list):        
        print(f'{index}:  {tasks_list[index]["name"].upper()}')
        keys_list = list(tasks_list[index])
        description = keys_list[1].capitalize()
        deadline = keys_list[2].capitalize()
        priority = keys_list[3].capitalize()
        completed = keys_list[4].capitalize()
        #print(description, deadline, priority, completed)
        print(f'    {description}: {tasks_list[index]["description"]}')
        print(f'    {priority}: {priority_message(tasks_list[index]["priority"])}')
        print(f'    {deadline}: {written_date(tasks_list[index]["deadline"])}')
        print(f'    {completed}: {completion_message(tasks_list[index]["completed"])}')
        print()


def priority_message(number):
    """
    Check the input of a task's priority
    and replaces the number with the corresponding
    message for that level of priority
    """
    messages = {
        1 : "Lowest",
        2 : "Low",
        3 : "Medium",
        4 : "High",
        5 : "Highest"
        }
    return messages[number]

    
def completion_message(word):
    """
    Check whether a task is marked as
    commpleted or not and replace the input
    with Yes if completed or No if not
    """
    messages = {
        True : "Yes",
        False : "No"
        }  
    return messages[word]

    
def written_date(string):
    """
    takes a date thats been written with slashes
    in the american calendar style and returns a
    written date
    """
    date_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
        }
        
    date_info = string.split("/")
    month = int(date_info[0])
    day = str(int(date_info[1]))
    year = date_info[2]
    month_name = date_names[month]
    date = month_name + " " + day + "," + " " + year
    return date
    

def create_task(keys, vals):
    """
    The function takes a list with the keys and a list 
    with the corresponding values and returns a dictionary 
    with the provided keys mapping to the corresponding values.
    """
    task = {}
    for i in range(0, len(keys)):
        for j in range(i, len(vals)):
            task[keys[i]] = vals[j]
            break
    return task           
    


def create_a_task(name, description, date, priority, completion):
    '''
    validate each parameter starting from "name" and until "completion"
    If one of them fails, return (False, <name of parameter>)
    ex. (False, "name") if "name" is not 3-15 characters long
    or (False, "completion") if completion is not a "yes" or "no"
    If all validations pass, return (True, <dictionary with fields name, description...>)
    '''
    dictionary = {}
    if validate_name(name) == False:
        return (False, "name")
    elif validate_description(description) == False:
        return (False, "description")
    elif validate_date(date) == False:
        return (False, "deadline")
    elif validate_priority(priority) == False:
        return (False, "priority")
    elif validate_completed(completion) == False:
        return (False, "completed")
    else:
        dictionary["name"] = name
        dictionary["description"] = description
        dictionary["deadline"] = date
        dictionary["priority"] = int(priority)
        if completion == "no" or completion == "No":
            dictionary["completed"] = False
        elif completion == "yes" or completion == "Yes":
            dictionary["completed"] = True
        return (True, dictionary)




def update_task(task_list, task_id, task_field, task_update):
    """ Given
    * the task list (`task_list`)
    * the task index that has been selected (`task_id`)
    * the field of the selected task (`task_field`)
    * the updated information (`task_update`)
    Validate the parameters to check for syntax and structure. 
    If all validations passed, return a tuple with a boolean True and 
    the updated task (a dictionary from the `task_list` at the provided `task_id`).
    Ff validations fail, return a tuple with a boolean False and 
    a string with the task_field that caused the error during validation.
    """

    fields = [
    'name',
    'description',
    'deadline',
    'priority',
    'completed'
    ] #you may use this to validate field_name
    if type(task_id) !=  int:
        return (False, 'idx')
    elif is_valid_index(task_id,task_list) == False:
        return (False, 'idx')
    elif task_field not in fields:
        return (False, 'field') 
    elif task_field == 'name': # use the correct function call(s)
        if validate_name(task_update) == False:
            return (False, 'name')
        else:
            task_list[int(task_id)][task_field] = task_update
            return (True, task_list[int(task_id)])
    elif task_field == 'description': # use the correct function call(s)
        if validate_description(task_update) == False:
            return (False, 'description')
        else:
            task_list[int(task_id)][task_field] = task_update
            return (True, task_list[int(task_id)])
    elif task_field == 'deadline': # use the correct function call(s)
        if validate_date(task_update) == False:
            return (False, 'deadline')
        else:
            task_list[int(task_id)][task_field] = task_update
            return (True, task_list[int(task_id)])
    elif task_field == 'priority': # use the correct function call(s)
        if validate_priority(task_update) == False:
            return (False, 'priority')
        else:
            task_list[int(task_id)][task_field] = task_update
            return (True, task_list[int(task_id)])
    elif task_field == 'completed': # use the correct function call(s)
        if validate_completed(task_update) == False:
            return (False, 'completed')
        else:
            if task_update == "no" or task_update == "No":
                task_list[int(task_id)][task_field] = False
                return (True, task_list[int(task_id)])
            elif task_update == "yes" or task_update == "Yes":
                task_list[int(task_id)][task_field] = True
                return (True, task_list[int(task_id)])


def delete_task(idx, tasks):
    """
    Checks if idx, which is an integer, is a valid index inside Tasks
    If not, returns False
    If a valid index, removes the element at index 'idx'
      from tasks, and returns True
    """
    if is_valid_index(int(idx), tasks) == True:
        print(f'Task "{tasks[idx]["name"].upper()}" has been deleted')
        del tasks[idx]
        return True
    else:
        return False


def print_tasks_by_status(all_tasks, completed=False):
    """
    Prints tasks from 'all_tasks',
    based on the value of 'completed' of each task.
    If there are no tasks that are incomplete,
    prints 'You do not have incomplete tasks.'
    If there are no tasks that are completed,
    prints 'You do not have completed tasks.'
    Otherwise, prints the requested tasks.
    """
    temp_list = []
    if completed == False:
        count = 0
        for dictionary in all_tasks:
            if dictionary['completed'] == False:
                print(f'The task "{dictionary["name"].upper()}" is incomplete.')
                print()
                temp_list.append(dictionary)
                count += 1           
        if count == 0:
            print('You do not have incomplete tasks.')

    elif completed == True:
        count = 0
        for dictionary in all_tasks:
            if dictionary['completed'] == True:
                print(f'The task "{dictionary["name"].upper()}" is complete.')
                print()
                temp_list.append(dictionary)
                count += 1
        if count == 0:
            print('You do not have completed tasks.') 
    print_formatted_tasks(temp_list)  




def save_to_csv(my_list, filename):
    """
    takes in a list of dictionaries for input
    reads through each dictionary in the list
    writes all the dictionary values for a single dictionary
    in a single row in a csv file
    closes after doing so for all the dictionaries
    """
    with open(filename, 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile)
        for current_dict in my_list:
            task_data = list(current_dict.values())
            task_writer.writerow(task_data)
                

def load_from_csv(filename):
    '''
    Reads the csv file and creates a new list of tasks using
    the data in that file. Loop through the lines of data and 
    in each iteration, call create_a_task() to get the data 
    as a dictionary. Save each valid dictionary into the list 
    tasks (i.e., dictionaries).
    Note that this function is responsible for converting
    the last (Boolean) field of the task from "True"/"False"
    to "yes"/"no", so that the task can be correctly created
    using the create_a_task() function.

    Return the resulting list of dictionaries, which will be 
    empty, if the file is empty or the data in it is invalid.
    '''
    
    new_list = [] # empty list to store the data from the csv file
    
    with open(filename, 'r') as csvfile:
        reader_object = csv.reader(csvfile, delimiter =',')
        for values in reader_object:
            if len(values) == 5:
                if values[4] == 'True':
                    result = create_a_task(values[0], values[1], values[2], values[3], 'yes')
                elif values[4] == 'False':
                    result = create_a_task(values[0], values[1], values[2], values[3], 'no')

                print(result)

                if result[0] == True:
                    new_list.append(result[1])
                else:
                    print("WARNING: invalid data -", values)
                    return "invalid data"

            else: #if data formatting is inconsistent
                print("WARNING: invalid data -", values)
                print("WARNING: Data formatting is inconsistent with the task manager!")
                return "inconsistent format"

    return new_list


def slashes_to_written(date_list):
    """
    takes in a list of three numbers
    replaces the number of the month with the name of the month
    returns the date in a written format
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = month_names[int(date_list[0])]
    day = int(date_list[1])
    day = str(day)
    date = month + " " + day + "," + " " + date_list[2]
    return date



        

