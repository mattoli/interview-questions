'''

Find missing elements from a list

Input: list1 - original list, list2 - items to check for in list1
Output: list of missing items

'''

# Find missing items using list comprehension
def find_missing(list1, list2):
    return [i for i in list1 if i not in list2]