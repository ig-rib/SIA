def printNumber(numMatrix):
    for i in range(numMatrix.shape[0]):
        for j in range(numMatrix.shape[1]):
            print('%.0g' % 1 if numMatrix.item((i, j)) > 0.5 else '_', end='') #(numMatrix.item((i, j)))
        print()