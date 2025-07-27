def sort_list(lst, reverse=False):
    lst.sort(reverse=reverse)
    return lst

def count_occurrence(lst, item):
    return lst.count(item)

def find_index(lst, item):
    return lst.index(item) if item in lst else -1
