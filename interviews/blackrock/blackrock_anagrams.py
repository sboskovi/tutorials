#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#
import copy
from collections import defaultdict

anagrams = ["code", "cdeo", "captain", "apple", "edeco"]

def funWithAnagrams(text):
    res = []
    for index, word in enumerate(text):
        d = defaultdict(int)
        for c in word:
            d[c] += 1
        
        for j in range(index + 1, len(text)):
            d_copy = copy.deepcopy(d)
            second_word = text[j]
            for c in second_word:
                d_copy[c] -= 1

            flag = True
            for value in d_copy.values():
                if value != 0:
                    flag = False
                    break
            if flag is True:
                res.append(second_word)
    return sorted(res)

# def 

# def funWithAnagrams(text):
#     res = []
#     for word in text:
        
#     return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()