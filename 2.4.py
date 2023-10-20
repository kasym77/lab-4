try:
    set_A = {1, 2, 3, 4, 7}
    set_B = {8, 7, 9, 4, 2, 0, 10}
    set_C = {4, 0, 1}

    set_A.difference_update(set_C)

    set_B.update(set_C)

    print(set_C)
except ValueError:
    print("error")