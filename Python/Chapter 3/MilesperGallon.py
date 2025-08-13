total_miles = 0
total_gallons = 0
tankful_count = 0

for _ in range(10000):  # Large range to allow multiple tankfuls
    miles = float(input("Enter miles driven (-1 to quit): "))
    
    if miles == -1:
        break
    
    gallons = float(input("Enter gallons used: "))
    
    if gallons > 0:
        mpg = miles / gallons
        print(f"Miles per gallon for this tankful: {mpg:.2f}")
        
        total_miles += miles
        total_gallons += gallons
        tankful_count += 1

if tankful_count > 0:
    combined_mpg = total_miles / total_gallons
    print(f"\nCombined miles per gallon for all tankfuls: {combined_mpg:.2f}")
else:
    print("\nNo tankfuls were entered.")