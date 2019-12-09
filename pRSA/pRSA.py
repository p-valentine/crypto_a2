import random


def isPrime(n, k):

    if n == 1 or n == 2:
        return True
    else:
        d = n - 1
        s = 0

        while d % 2 == 0:
            s = s + 1
            d = int(d / 2)

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


def generate_p_q():
    pass


def compute_n_phi(p, q):
    pass


def main():
    k = getK()
    is_odd = False
    while is_odd is False:
        r = random.randint(2 ** (k - 1), (2 ** k) - 1)  # generates random k bit number
        # print(r)
        if r % 2 != 0:
            is_odd = True
    result = isPrime(31, 100)

    print("result", result)


if __name__ == "__main__":
    main()
