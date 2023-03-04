# Create a function that decides if a list contains any odd numbers.
# return type: bool
# function name must be: contains_odd
# input parameters: input_list
def contains_odd(input_list: list) -> bool:
    for i in input_list:
        if type(i) == int and i % 2 != 0:
            return True
    return False


# Create a function that accepts a list of integers, and returns a list of bool.
# The return list should be a "mask" and indicate whether the list element is odd or not.
# (return should look like this: [True,False,False,.....])
# return type: list
# function name must be: is_odd
# input parameters: input_list
def is_odd(input_list: list) -> list:
    mask = []
    for i in input_list:
        if i % 2 != 0:
            mask.append(True)
        else:
            mask.append(False)
    return mask


# Create a function that accpects 2 lists of integers and returns their element wise sum.
# (return should be a list)
# return type: list
# function name must be: element_wise_sum
# input parameters: input_list_1, input_list_2
def element_wise_sum(input_list_1: list, input_list_2: list) -> list:
    return [i + j for i, j in zip(input_list_1, input_list_2)]


# Create a function that accepts a dictionary and returns its items as a list of tuples
# (return should look like this: [(key,value),(key,value),....])
# return type: list
# function name must be: dict_to_list
# input parameters: input_dict
def dict_to_list(input_dict: dict) -> list:
    return [(key, value) for key, value in input_dict.items()]
