try:
    SetA = {1, 2, 3, 4, 5}
    SetB = {5, 7, 8, 9, 2, 10}


    diffSet = SetA - SetB


    diffSet.update(SetB - SetA)


    print(diffSet)
except ValueError:
    print("error")