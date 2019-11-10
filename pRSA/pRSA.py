import math
import random
import sys


def isPrime(n, k):

    if n == 1 or n == 2:
        return True
    else:
        d = n - 1
        s = 0

        while d % 2 == 0:
            s = s + 1
            d = int(d / 2)

        for i in range(1, k):
            a = random.randint(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == (n - 1):
                continue
            for k in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    print("x = 1")
                    return "Composite"
                elif x == (n - 1):
                    print("x = n-1")
                    break 
            if x == 1 or x == (n - 1):
                continue
            return "composite"

        return "prime"


def getK():
    print("Input number of bits: ")
    k = int(input())
    return k


def generateRandom(k):
    r = random.getrandbits(k)
    return r


def main():
    k = getK()
    is_odd = False
    while is_odd is False:
        r = random.randint(2 ** (k - 1), (2 ** k) - 1)  # generates random k bit number
        print(r)
        if r % 2 != 0:
            is_odd = True
    result = isPrime(r, 30)

    print(result)


if __name__ == "__main__":
    main()
