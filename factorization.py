def prime_factors(n):
    factors = []
    # Divide by 2 until it is an odd number
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Divide by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage
number = int(input("Enter a number: "))
result = prime_factors(number)
print(f"Prime factors of {number}: {result}")
