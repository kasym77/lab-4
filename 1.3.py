TupleA = (1, 2, 3, 4, 5, 6, 7)
TupleB = (5, 6, 7, 9, 7, 1, 10, 10)


halfA = len(TupleA) // 2


result = TupleA[:halfA] + TupleB[halfA + halfA:]

print(result)