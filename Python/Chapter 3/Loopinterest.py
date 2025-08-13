principal = 1000 
rate = 0.07       
print("Year  Amount")

for n in range(1, 31):
    amount = principal * (1 + rate) ** n
    print(f"{n:<5} ${amount:.2f}")