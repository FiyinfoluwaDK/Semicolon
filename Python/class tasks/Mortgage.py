
Principal = int(input("Input Principal amount = "))

annualRate = float(input("Input Annual Rate = "))

yearlyDuration = int(input("Input Yearly Duration = "))

monthlyrate = (annualRate / 100) / 12
monthlyduration = yearlyDuration * 12

m = Principal *(((monthlyrate * ((1 + monthlyrate)** monthlyduration))) / ((((1 + monthlyrate)** monthlyduration)-1)))

print("monthly payment =", m)

