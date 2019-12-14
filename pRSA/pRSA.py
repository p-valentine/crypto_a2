import random


def isPrime(n, k):

    if n == 1 or n == 2:
        return True
    else:
        d = n - 1
        s = 0

        while d % 2 == 0:
            s = s + 1
            d >>= 1

        for i in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x != 1 and x != (n - 1) and not innerLoop(x, s, n):
                return False

        return True


def innerLoop(x, s, n):
    for i in range(s):
        x = pow(x, 2, n)
        if x == 1:
            print("x = 1 inner loop")
            return False
        elif x == (n - 1):
            return True
    return False


def getK():
    print("Input number of bits: ")
    k = int(input())
    return k


def generateRandom(k):
    r = random.getrandbits(k)
    return r


def generate_e_d():
    pass


def generate_p_q(k):
    result = False
    p, q = None, None
    while p is None:
        p = random.randint(2 ** (k - 1), (2 ** k) - 1)
        if p % 2 != 0:
            result = isPrime(p, 30)
            print("done testing isPrime")
        if result is True:
            print("P is prime")
        else:
            p = None
            print("p is not prime :( ", p)
    while q is None and q != p:
        q = random.randint(2 ** (k - 1), (2 ** k) - 1)
        if q % 2 != 0:
            result = isPrime(q, 30)
            print("done testing isPrime")
        if result is True:
            print("q is prime")
        else:
            q = None
            print("q is not prime :( ", q)

    return p, q


def compute_n_phi(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    return n, phi


def main():
    k = getK()
    p, q = generate_p_q(k)
    print("P= ", p, " Q= ", q)
    n, phi = compute_n_phi(p, q)
    print("N= ", n, "Phi= ", phi) 


if __name__ == "__main__":
    main()
