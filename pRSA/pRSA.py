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


def generate_e_d(phi):
    gcd = 0
    while gcd != 1:
        e = random.randint(3, phi - 1)
        gcd, _, d = pulverizer(phi, e)

    a = e % phi
    b = d % phi
    return a, b


def pulverizer(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


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
    e, d = generate_e_d(phi)
    print("e= ", e, "d= ", d)


if __name__ == "__main__":
    main()
