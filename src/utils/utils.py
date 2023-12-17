# This is a function - it's a piece of code that we can use over and over
# This function displays a piece of text and then waits for the user to enter a list of numbers separated
#      by commas and returns the list of numbers
# read_number_array is the *name* of the function
# the function takes one argument, prompt of type string
# the -> list[int] just means the function returns a list of integer. This is not mandatory, but 
#        it's helpful for the python compiler
def read_number_array(prompt: str) -> list[int]:
    # this will display the string in the *prompt* argument and wait for the user to type a string and press ENTER
    array_string = input(prompt)
    # this will take the string we read and split it up into parts (also strings) between the commas
    # this means we will have to enter the array as for example 1,4,8,2,7
    return_array = array_string.split(',')
    # this weird expression will convert every string in return_array to a number (an integer)
    return_int_array = [int(x) for x in return_array]
    # finally, we return the array
    # Note - once you become a coding ninja, you can write this in one line as:
    #    return [int(x) for x in input(prompt).split(',')]
    return return_int_array


# This is a function that reads a single number
def read_number(prompt: str) -> int:    
    return int(input(prompt))


# This function prints an array of integers with a prompt
def print_array(prompt: str, array: list[int]):
    print(f"{prompt}: {','.join([str(x) for x in array])}")
    

# read a number array from a file
def read_number_array_file(file: str) -> list[int]:
    with open(file, 'r') as f:
        array_string = f.read()
        return_array = array_string.split(',')
        return_int_array = [int(x) for x in return_array]
    return return_int_array