def move(my_list, direction=None):
    index_of_one = my_list.index(1)
    my_list[index_of_one] = 0

    if direction == 'right':
        new_index = (index_of_one + 1) % len(my_list)
    elif direction == 'left':
        new_index = (index_of_one - 1) % len(my_list)
    else:
        new_index = index_of_one  # no move

    my_list[new_index] = 1
    return my_list
