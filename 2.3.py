try:
    SetA = {1, 2, 3, 4, 5}
    SetB = {5, 7, 8, 9, 2, 10}

    SetA.difference_update(SetB)

    print(SetA)

except ValueError:
    print("error")