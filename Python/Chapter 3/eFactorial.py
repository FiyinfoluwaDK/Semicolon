e_approx = 0
factorial = 1

for n in range(10):
    if n > 0:
        factorial *= n
    e_approx += 1 / factorial

print(f"Estimated value of e after 10 terms: {e_approx:.10f}")