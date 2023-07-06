def check_option(option, menu):
    """
    Given an option, return "valid" if it is
    of type str and is a valid key in
    the provided collection.
    Otherwise, return "invalid".
    """
    if type(option) == str and option in menu.keys():
        return "valid"
    else:
        return "invalid"


def is_valid_index(idx, in_list):
    """
    Checks whether the provided index `idx` is a valid positive index that can retrieve
    an element from `in_list`. Returns False if `idx` is negative or exceeds the size of `in_list`.
    """
    if 0<=idx<len(in_list):
        value = in_list[idx]
        return True
    else:
        return False


def is_numeric(val):
    """
    Returns True if the string `val` contains a valid integer or a float.
    Returns False otherwise.
    """
    outcome = val.isdigit()
    if "." in val:
        if val.count(".") == 1:
            vals = val.split(".")
            first = vals[0]
            second = vals[1]
            if first.isdigit() == True and second.isdigit() == True:
                outcome = True
            else:
                outcome = False
        else:
            outcome = False
        
    return outcome


def validate_name(name):
    '''
    validates the "name" parameter
    Returns True if the name is between 3 and 15 characters long, inclusive
    Returns False otherwise
    '''
    if "," in name:
        return False
    elif 3 <= len(name) <= 15:
        return True
    else:
        return False


def validate_description(desc):
    '''
    validates the "desc" parameter
    Returns True if desc is a non-empty string
    Returns False otherwise
    '''
    if type(desc) != str:
        return False
    elif len(desc) == 0: 
        return False
    elif "," in desc:
        return False
    else:
        return True


def validate_date(date_string):
    '''
    validates the "date_string"
    Returns True if date_string is a valid date string
    in slashes format (lab 8.16)
    Returns False otherwise
    '''
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
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
        12: "December"
    }
        
    if "/" not in date_string:
        return False
    else:
        numbers = date_string.split("/")
        if numbers[0].isdigit() == True:
            if numbers[1].isdigit() == True:
                if numbers[2].isdigit() == True:
                    if "00" < numbers[0] < "13":
                        if 0 < int(numbers[1]) <= num_days[int(numbers[0])]:
                            return True
                            
                        else:
                            return False
                    else:
                        return False 
                else:
                    return False
            else:
                return False
        else:
            return False


def validate_priority(priority):
    '''
    validate the "priority" parameter
    Returns True if "priority" is a string containing a number 1-5
    Returns False otherwise
    '''
    if priority == "1":
        return True
    elif priority == "2":
        return True
    elif priority == "3":
        return True
    elif priority == "4":
        return True
    elif priority == "5":
        return True
    else:
        return False


def validate_completed(comp):
    '''
    validate the "comp" parameter.
    Returns True if s is one of: "yes", "no", "Yes", "No"
    Returns False otherwise
    '''
    if comp == "yes" or comp == "Yes" or comp == "no" or comp == "No":
        return True
    else:
        return False
