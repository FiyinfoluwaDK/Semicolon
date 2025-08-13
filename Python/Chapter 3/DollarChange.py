price = float(input("Enter purchase price (in dollars, up to $1): "))

if price < 0 or price > 1:
    print("Price must be between $0 and $1.")
else:
    change_cents = round((1 - price) * 100)

    quarters = change_cents // 25
    change_cents %= 25

    dimes = change_cents // 10
    change_cents %= 10

    nickels = change_cents // 5
    change_cents %= 5

    pennies = change_cents

    print("Your change is:")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
