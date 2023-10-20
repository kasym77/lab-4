try:
    N = (55, 6, 777, 70.0, '7', ' А')


    tuple1 = (N[0], N[1], N[2])
    tuple2 = (N[3])
    tuple3 = (N[4], N[5])


    print(tuple1)
    print(tuple2)
    print(tuple3)
except ValueError:
    print("error")