import numpy as np 
import math

#do the pulverisor
#if negative d add phi to d until you get a positive number
#once find d - decrypt y^d mod n, then chop it up and take the ascii


def find_phi(encrypted_vlaues):
  phi_as_list = []
  with open("encrypted_phi.txt", "r") as f:
    for line in f:
      n = int(line)
      if n in encrypted_vlaues: #checks to make sure phi is actually an ascii digit
        phi_as_list.append(str(encrypted_vlaues[n]))

  print(phi_as_list)
  phi_string = "".join(phi_as_list)
  phi_as_int = int(phi_string)
  print("\n\n", "Phi: ", phi_as_int)
  return phi_as_int

def generate_encrypted_digits(e, n):

  encrypted_values = {}
  for i in range(48, 58):
    encrypted_values[(pow(i, e, n))] = i - 48
  return encrypted_values

def main():
  f = open("numbers/e.txt", "r")
  e = int(f.readline())
  f.close()

  f = open("numbers/n.txt", "r")
  n = int(f.readline())
  f.close()

  encrypted_phi = generate_encrypted_digits(e,n)
  print(encrypted_phi, "\n\n")
  phi = find_phi(encrypted_phi)

  print("\n\n GCD:\n")
  print(math.gcd(phi, e))

if __name__ == "__main__":
  main()