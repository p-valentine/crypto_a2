import numpy as np 
import math
import random
import sys

def isPrime():
  pass

def getK():
  print("Input a positive integer 'K' as the security parameter: ")
  k = int(input())
  return k

def generateRandom(k):
  r = random.getrandbits(k)
  return r


def main():
  if(len(sys.argv) <= 1):
    print("Error: integer argument required")
    exit()
  j = sys.argv[1]
  k = int(j)
  r = generateRandom(k)
  print(r)


if __name__ == "__main__":
  main()