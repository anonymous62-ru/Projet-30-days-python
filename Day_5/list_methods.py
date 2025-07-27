def add_element(lst, value):
    lst.append(value)
    return lst

def insert_element(lst, index, value):
    lst.insert(index, value)
    return lst

def remove_element(lst, value):
    if value in lst:
        lst.remove(value)
    return lst

def pop_element(lst, index=None):
    return lst.pop(index) if index is not None else lst.pop()

def clear_list(lst):
    lst.clear()
    return lst
