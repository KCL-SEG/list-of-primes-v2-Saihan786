"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    current_prime = 2
    counter = number_of_primes

    while counter>0:
        isPrime = True
        for j in range(2,current_prime-1):
            if (current_prime%j) == 0:
                isPrime = False
                break
        if isPrime:
            list.append(current_prime)
            counter-=1
        current_prime+=1
    return list
