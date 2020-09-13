import sys


S = input().strip()
try:
    myInt = int(S)
    print(myInt)
except ValueError:
    print("Bad String")
