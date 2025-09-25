#!/bin/python3

import math
import os
import random
import re
import sys
import requests

#
# Complete the 'showsInProduction' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER startYear
#  2. INTEGER endYear
#
# Base url: https://jsonmock.hackerrank.com/api/tvseries
#
import requests


def get_runtime(runtime):
    parsed = runtime.replace("(", "").replace(")", "").replace("I", "")
    if "-" not in parsed:
        return (int(parsed), -1)
    
    start, end = parsed.split("-")
    if end is None or end.strip() == "":
        return (int(start), -1)
    return (int(start), int(end))
    

def showsInProduction(startYear, endYear):
    url = "https://jsonmock.hackerrank.com/api/tvseries"
    resp = requests.get(url).json()
    total_pages = resp.get("total_pages", 0)
    res = []
    
    for index in range(total_pages):
        url = f"https://jsonmock.hackerrank.com/api/tvseries?page={index}"
        resp = requests.get(url).json()
        print(resp.get("data"))
        

        for show in resp.get("data", []):
            runtime = show.get("runtime_of_series")
            start, end_time = get_runtime(runtime)
            if start <= startYear and end_time >= endYear:
                res.append(show.get("name"))
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    startYear = int(input().strip())

    endYear = int(input().strip())

    result = showsInProduction(startYear, endYear)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()