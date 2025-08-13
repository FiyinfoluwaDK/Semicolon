numbers = []
sum_numbers = 0
product = 1

for i in range(4):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)
    sum_numbers += num
    product *= num

average = sum_numbers / 4

smallest = min(numbers)
largest = max(numbers)

print(f"Sum: {sum_numbers}")
print(f"Average: {average:.2f}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")