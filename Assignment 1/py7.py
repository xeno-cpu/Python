# find numbers divisible by 9 but not by 6 in a user-defined range

#nput range  
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

#calculation 

numbers = [num for num in range(start, end + 1) if num % 9 == 0 and num % 6 != 0]

# Display 
print(f"Numbers between {start} and {end} divisible by 9 but not by 6: {numbers}")

