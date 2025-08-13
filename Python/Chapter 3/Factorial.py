n = int(input("Enter a nonnegative integer: "))

if n < 0:
    print("Error: Please enter a nonnegative integer.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    print(factorial)