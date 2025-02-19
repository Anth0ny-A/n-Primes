import sys
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def find_primes(n):
    counter=1
    x=3
    print(2)
    while counter<n:
        if(x%2 == 0):
            x+=1
            continue
        elif(is_prime(x)):
            print(x)
            counter+=1
        x+=1

try:
    n=int(sys.argv[1])
    if n<=0:
        print("Error. N must be positive.")
        exit(1)
    print(f"List of {n} primes:")

    find_primes(n)
    
except IndexError:
    print("No input provided. Please enter an n value between 1 and 100.")
except ValueError:
    print("Invalid input. Please enter an integer value.")