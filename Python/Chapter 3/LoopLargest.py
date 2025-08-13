largest = float('-inf')  # Start with negative infinity
second_largest = float('-inf')

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    
    if num > largest:
        second_largest = largest  
        largest = num            
    elif num > second_largest and num != largest:
        second_largest = num     

print(f"The largest value is: {largest}")
print(f"The second-largest value is: {second_largest}")