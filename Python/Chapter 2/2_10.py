num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

total_sum = num1 + num2 + num3
average = total_sum / 3
product = num1 * num2 * num3

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
