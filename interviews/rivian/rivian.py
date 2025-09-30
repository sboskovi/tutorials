#!/bin/python3

import math
import os
import random
import re
import sys

# Zadatak: dobijes listu vremenskih intervala i trebas da spojis sve intervale koji se preklapaju
# npr: input = [[1,2],[2,3],[6,11],[7,7]] -> output = [[1,3],[6,11]]
# intevali nisu sortirani

#
# Complete the 'getMergedIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

# 1. Problem:
# Pozurio si da das rjesenje jer ga nisi odmah vidio - pa si predlozio hash map-u, tu te intervjuer ispravio - kako ces da cuvas interval? Sta je kljuc sta je vrijednost?
# 2. Problem:
# Nisi se vratio na postavku zadatka - intervjuer ti je predlozio da preispitas da li ima tamo nesto sto bi moglo da pomogne? - stoji da treba da bude sortirano u postavci
# 3. Problem:
# Sto ti nije palo na pamet da sortiras niz nizova - nisi se sam sjetio toga
# Nisam siguran da li sam sam procitao tamo ili mi je on sugresao da treba da bude sortirano
# 4. Problem:
# sort funkcija, ok sto nisi znao da li ce da sortira niz nizova, nije ok sto se nisi sjetio da mozes da napises compare funkciju
# 1. Dobro:
# Sto si prepoznao da je to sliding window problem
# 5. Problem:
# Naprijed nazad sa for / while - pokazao si nesigurnost
# 6. Problem:
# Uzastopni intervali - while umjesto if-a
# 7. Problem:
# extended_interval - ti si nastavio da koristis prvi interval, cak nakon sto si ga prosirio - imao si first_end =  




def getMergedIntervals(intervals):
    # _intervals = [[1,2],[2,3],[6,11],[7,7]]
    # _intervals = [[1,5],[2,3],[6,11],[7,7],[14,18]]
    sortedIntervals = sorted(intervals)
    print(sortedIntervals)
    i, j = 0, 1
    res = []
    
    while j < len(sortedIntervals):
        first_start = sortedIntervals[i][0]
        first_end = sortedIntervals[i][1]
        second_start = sortedIntervals[j][0]
        second_end = sortedIntervals[j][1]
        extended_interval = [first_start, first_end]
        
        while second_start <= first_end:
            first_end = max(first_end, second_end)
            extended_interval = [first_start, first_end]
            
            j += 1
            if j >= len(sortedIntervals):
                break
            second_start = sortedIntervals[j][0]
            second_end = sortedIntervals[j][1]

        res.append(extended_interval)
        i = j
        
    return res
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = getMergedIntervals(intervals)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()