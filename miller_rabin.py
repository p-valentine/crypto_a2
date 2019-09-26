import secrets
import numpy as np


def main():
  print("hello world")
  print(generate_random_number(7))


def generate_random_number(num_bits):
  random_number = secrets.randbits(num_bits)
  return random_number



if __name__ == "__main__":
  main()