import re

math_function_regex=re.compile("(?:[0-9-+*/()x]|pi|e)+") #a simple regex that represent simple function format for x parameter

colorstring = 'bgkry'

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
            if arr[mid].start < x and x < arr[mid].end:
                return mid
            elif arr[mid].start == x:
                if arr[mid].equal[0]: #if x is a boarder we have to ensure that if within functions domain
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
        



    
