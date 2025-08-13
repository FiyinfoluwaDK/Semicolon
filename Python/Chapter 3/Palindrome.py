number = int(input("Enter a five-digit integer: "))

if 10000 <= number <= 99999:
    digit1 = number // 10000  
    digit2 = (number // 1000) % 10  
    digit3 = (number // 100) % 10  
    digit4 = (number // 10) % 10  
    digit5 = number % 10  
    
    if digit1 == digit5 and digit2 == digit4:
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
else:
    print("Error: Please enter a valid five-digit integer (10000 to 99999).")