from validate import *
from tasks import *

print("validate.py assert statements:")
print()
print("check_option tests")
my_menu0 = {}
my_menu1 = {'1': "One"}
my_menu2 = {'L': "List"}

result = check_option(1, my_menu0)
print(f"--> check_option(1, my_menu0) returned `{result}`")
assert result == "invalid"

result = check_option(1, my_menu1)
print(f"--> check_option(1, my_menu1) returned `{result}`")
assert result == "invalid"

result = check_option('1', my_menu1)
print(f"--> check_option('1', my_menu1) returned `{result}`")
assert result == "valid"

result = check_option('1', my_menu2)
print(f"--> check_option('1', my_menu2) returned `{result}`")
assert result == "invalid"

result = check_option('L', my_menu2)
print(f"--> check_option('L', my_menu2) returned `{result}`")
assert result == "valid"
print()


print("is_numeric tests")
result = is_numeric('123')
print(f"--> is_numeric('123') returned `{result}`")
assert result == True

result = is_numeric('abc')
print(f"--> is_numeric('abc') returned `{result}`")
assert result == False

result = is_numeric('5.5')
print(f"--> is_numeric('5.5') returned `{result}`")
assert result == True

result = is_numeric('5.5.')
print(f"--> is_numeric('5.5.') returned `{result}`")
assert result == False
print()


print("is_valid_index tests")
result = is_valid_index(5, [0,1,2,3,4,5])
print(f"--> is_valid_index(5, [0,1,2,3,4,5]) returned '{result}'")
assert result == True

result = is_valid_index(-2, [0,1,2,3,4,5])
print(f"--> is_valid_index(-2, [0,1,2,3,4,5]) returned '{result}'")
assert result == False

result = is_valid_index(9, [0,1,2,3,4,5])
print(f"--> is_valid_index(9, [0,1,2,3,4,5]) returned '{result}'")
assert result == False
print()


print("validate_name tests")
result = validate_name('run')
print(f"--> validate_name('run') returned '{result}'")
assert result == True

result = validate_name('go on long hike')
print(f"--> validate_name('go on long hike') returned '{result}'")
assert result == True

result = validate_name('XC')
print(f"--> validate_name('XC') returned '{result}'")
assert result == False

result = validate_name('play new super mario brothers')
print(f"--> validate_name('play new super mario brothers') returned '{result}'")
assert result == False

result = validate_name('dance, perform')
print(f"--> validate_name('dance, perform') returned '{result}'")
assert result == False
print()


print("validate_description tests")
result = validate_description('Stadard Description')
print(f"--> validate_description('Standard Description') returned '{result}'")
assert result == True

result = validate_description('')
print(f"--> validate_description('') returned '{result}'")
assert result == False

result = validate_description(15)
print(f"--> validate_description(15) returned '{result}'")
assert result == False

result = validate_description("hug, kiss, and cuddle my girlfriend")
print(f"--> validate_description(15) returned '{result}'")
assert result == False
print()


print("validate_date tests")
result = validate_date('01/02/2003')
print(f"--> validate_date('01/02/2003') returned '{result}'")
assert result == True

result = validate_date('01.02.2003')
print(f"--> validate_date('01.02.2003') returned '{result}'")
assert result == False

result = validate_date('01/35/2003')
print(f"--> validate_date('01/35/2003') returned '{result}'")
assert result == False

result = validate_date('14/30/2003')
print(f"--> validate_date('14/30/2003') returned '{result}'")
assert result == False

result = validate_date('january/30/2003')
print(f"--> validate_date('january/30/2003') returned '{result}'")
assert result == False
print()


print("validate_priority tests")
result = validate_priority('1')
print(f"--> validate_priority('1') returned '{result}'")
assert result == True

result = validate_priority('5')
print(f"--> validate_priority('5') returned '{result}'")
assert result == True

result = validate_priority('6')
print(f"--> validate_priority('6') returned '{result}'")
assert result == False
print()


print("validate_completed tests")
result = validate_completed('yes')
print(f"--> validate_completed('yes') returned '{result}'")
assert result == True

result = validate_completed('No')
print(f"--> validate_completed('No') returned '{result}'")
assert result == True

result = validate_completed('yeah')
print(f"--> validate_completed('yeah') returned '{result}'")
assert result == False
print()


print("tasks.py assert statements:")
print()

assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[0] == True
assert type(create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]) == dict
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['name'] == 'do dishes'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['description'] == 'wash the plates from dinner'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['deadline'] == '03/04/2022'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['priority'] == 2
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['completed'] == False

assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[1] == 'name'

# name too long
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[1] == 'name'

# description empty
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[1] == 'description'

# invalid dates empty
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[1] == 'deadline'

# invalid priority
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[1] == 'priority'

# invalid completion
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[1] == 'completed'

print("create_a_task checks out")
print()

my_list = [{
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
        'completed': True
        },
        {
        'name': 'compar. lit essay',
        'description': "finish comparative lit essay that's overdue",
        'deadline': '02/15/2022',
        'priority': 4,
        'completed': True
        }]


print("Update_task asserts:")
result = update_task(my_list, '5', 'name', 'go clubbing')
assert result[1] == "idx"
assert result[0] == False
print(f"--> update_task(my_list, '5', 'name', 'go clubbing') "+
          f"successfully returned error with `{result[1]}`\n")

result = update_task(my_list, '5', 'name', 'go clubbing')
assert result[1] == "idx"
assert result[0] == False
print(f"--> update_task(my_list, '5', 'name', 'go clubbing') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'Get Gift', 'I\'m quite hungry though')
assert result[1] == "field"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'Get Gift', 'I\'m quite hungry though') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'deadline', 'never')
assert result[1] == "deadline"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'deadline', 'never') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'priority', 'pants on FIRE!!!!')
assert result[1] == "priority"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'priority', 'pants on FIRE!!!!') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'completed', 'technically, yes')
assert result[1] == "completed"
assert result[0] == False
print(f"--> update_task(my_list, 1, 'completed', 'technically, yes') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, 1, 'deadline', '01/22/19')
assert result[0] == True
assert result[1]['deadline'] == '01/22/19'
print(f"--> update_task(my_list, '1', 'Deadline', '01/22/19' "+
      f"successfully returned updated task: \n{result[1]}\n")

result = update_task(my_list, 1, 'completed', 'no')
assert result[0] == True
assert result[1]['completed'] == False
print(f"--> update_task(my_list, 1, 'completed', 'no') "+
      f"successfully returned updated task: \n{result[1]}\n")

print(">>All assertions successfully run...\n")

my_list = [{
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
        'completed': True
        },
        {
        'name': 'compar. lit essay',
        'description': "finish comparative lit essay that's overdue",
        'deadline': '02/15/2022',
        'priority': 4,
        'completed': True
        }]

result = delete_task(0, my_list)
assert result == True
assert len(my_list) == 2

result = delete_task(0, my_list)
assert delete_task(4, my_list) == False

print("delete_task seems to be working")    





