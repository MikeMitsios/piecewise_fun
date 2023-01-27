import re

# A simple regex that allows specific characters for function format
# wanted to avoid the use of **. In this way a Polynomial function cannot be formed
math_function_regex=re.compile("(?: ?[0-9-+/()x]| ?pi| ?e| ?\*(?: ?[0-9-+/()x]|pi|e))+") 
#math_function_regex=re.compile(" ?-?(\d|x)( ?(?:[-+*/]) ?(\d|x))+") 

colorstring = 'bgkry' # A string for color cycle

def binary_search(arr, x: int):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid].end < x:
            low = mid + 1
        elif arr[mid].start > x:
            high = mid - 1
        else:
            if arr[mid].start < x < arr[mid].end:
                return mid
            elif arr[mid].start == x: # If x is a boarder we have to ensure that is within functions domain
                if arr[mid].equal[0]: 
                    return mid
                else:
                    high = mid - 1
            elif arr[mid].end == x:
                if arr[mid].equal[1]:
                    return mid
                else:
                    low = mid + 1
    # If we reach here, then the element was not present
    return -1
        



    
