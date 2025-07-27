def create_list():
    return ['HTML', 'CSS', 'JS', 'React', 'Redux']

def get_elements(lst):
    first = lst[0]
    middle = lst[len(lst)//2]
    last = lst[-1]
    return first, middle, last

def slice_list(lst):
    return lst[1:4], lst[::-1]
