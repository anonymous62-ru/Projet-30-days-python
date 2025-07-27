from list_basics import create_list, get_elements, slice_list
from list_methods import add_element, insert_element, remove_element, pop_element, clear_list
from list_analysis import sort_list, count_occurrence, find_index
from list_operations import join_lists, copy_list, slice_middle

if __name__ == "__main__":
    techs = create_list()
    print("Liste originale:", techs)
    print("Eléments:", get_elements(techs))
    print("Slices:", slice_list(techs))

    add_element(techs, 'Python')
    insert_element(techs, 2, 'SQL')
    print("Après insertion:", techs)

    print("Index de 'React':", find_index(techs, 'React'))
    print("Occurrence de 'JS':", count_occurrence(techs, 'JS'))

    new_stack = join_lists(['Node'], ['MongoDB'])
    full_stack = join_lists(techs, new_stack)
    print("Full stack:", full_stack)

    sorted_stack = sort_list(full_stack.copy())
    print("Trié:", sorted_stack)
