import itertools
import math

def check(l):
    order = int(math.sqrt(len(l)))
    sums = []
    sumOfDig1 = 0
    sumOfDig2 = 0
    for r in range(order):
        sumOfRow = 0
        sumOfCol = 0
        for c in range(order):
            sumOfRow += l[order * r + c]
            sumOfCol += l[order * c + r]
            if r == c:
                sumOfDig1 += l[order * r + c]
                sumOfDig2 += l[order * r + (order - c - 1)]
        sums.append(sumOfRow)
        sums.append(sumOfCol)
    sums.append(sumOfDig1)
    sums.append(sumOfDig2)
    return all([i == sums[0] for i in sums])

                
def printsquare(l):
    order = int(math.sqrt(len(l)))
    for r in range(order):
            print l[r*order:r*order+order]
    print "*******************"

    
if __name__ == "__main__":    
    n = 3
    for item in itertools.permutations(range(n*n)):
        if check(item):
            printsquare(item)
    
