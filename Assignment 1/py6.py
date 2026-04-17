# function that check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# in take the range 
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# find prime number
primes = [num for num in range(start, end + 1) if is_prime(num)]

# Display 
print(f"Prime numbers in the range {start} to {end}: {primes}")
print(f"Count of prime numbers: {len(primes)}")
print(f"Sum of prime numbers: {sum(primes)}")

