import numpy as np 
import math
import random
import sys

def isPrime(n, k):

  if(n ==1 or n == 2):
    return True
  elif( n % 2 == 0 ):
    return False
  else:
    print("other case")
    pass

  pass

def miller(n, k):
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
  r = random.randint(2 ** (k - 1), (2 ** k) - 1) #generates random k bit number

  print(r)
  result = isPrime(r,4)

  if(result == False):
    print("not a prime number")
  else:
    print("Prime number!")
  print(result)


if __name__ == "__main__":
  main()