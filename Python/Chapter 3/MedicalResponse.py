problem = input("What is your problem? ")

response = input("Have you had this problem before (yes or no)? ")

if response.lower() == "yes":
    print("Well, you have it again.")
else:
    print("Well, you have it now.")