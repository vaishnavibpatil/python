def prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num= 17  
if prime(num):
    print(f"No is a prime number")
else:
    print(f"No. is not a prime number")
