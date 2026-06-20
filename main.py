import math
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
def main():
    print(is_prime(7))
    print(is_prime(4))
if __name__ == "__main__":
    main()