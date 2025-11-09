#Must use recursion and docstrings in all problems

#Problem 1
def create_countdown(seconds):
    '''Prints a countdown from the given number to zero.

    The function prints each number on its own line, counting down recursively.
    If the input is 0 or negatice, the function prints nothing.

    Parameters:
        seconds(int): the starting number of seconds for the countdown'''

    #base case
    if seconds <= 0:
        return 
    
    if seconds ==1:
        print(seconds)
        print(0)
        
    #recursive case
    else:
        print(seconds)
        create_countdown(seconds - 1)
    

#Problem 2
def hourglass(base):
    '''Prints an hourglass to the screen using asterisks.

    Parameters:
        base (int): an integer that indicates how many asterisks will be used at the top and bottom levels of the hourglass'''
    #call the helper function starting at the full base width
    

    def hourglass_helper(current_level, base):
        '''Recursive helper function that prints each level of the hourglass.
        Parameters:
            current_level (int): the number of asterisks to print at this level
            base (int): the original base width to help with centering'''

        #base case: if current level is 1 or 2, print it and stop shrinking
        if current_level <= 2:
            print(('*' * current_level).center(base))
            print(('*' * current_level).center(base))
            return  #stops recursion at smallest level

        #recursive case
        print(('*' * current_level).center(base))  #prints the current level
        hourglass_helper((current_level - 2), base) #each successive level should have 2 less asterisks
        print(('*' * current_level).center(base))
    hourglass_helper(base, base)



#Problem 3
def progress_bar(completion_percent):
    '''Returns a progress bar representing the completion percentage.

    Parameters:
        complete_percent (int):Completion percentage from 0 to 100.

    Returns:
        str: Progress bar string; "[###        ]'''

    #Calculate how many hashes to show (round down)
    num_hashes = completion_percent // 10

    def progress_helper(count):
        '''Recursive helper function to build progress bar.

        Parameters:
            count (int): number of characters added so far

        Returns:
            str: partial progress bar'''
        
    #base case: 10 characters added to bar
        if count == 10:
            return "]"  #closes the bracket

        #Does a '#' or a space need to be added?
        if count < num_hashes:
            return "#" + progress_helper(count + 1)
        else:
            return " " + progress_helper(count + 1)
        
    return "[" + progress_helper(0)

#Problem 4
import os #

def num_occurrences(filename, path):
    '''Counts the number of times a file filename appears in the path or subdirectories.'''
    #base case: path doesn't exist
    if not os.path.exists(path):
        return 0 #stops recursion

    count = 0

    #recursive case
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            if item == filename:
                count += 1
        elif os.path.isdir(item_path):
            count += num_occurrences(filename, item_path)
    
    return count
