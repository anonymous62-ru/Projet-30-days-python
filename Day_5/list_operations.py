def join_lists(*lists):
    result = []
    for l in lists:
        result.extend(l)
    return result

def copy_list(lst):
    return lst.copy()

def slice_middle(lst):
    mid = len(lst) // 2
    return lst[mid-1:mid+2] if len(lst) >= 3 else lst
