# If statement
age = 25
if age >= 18:
    print("You are eligible to vote.")

# If-Else statement
age = 15
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Elif statement (else-if)
age = 30
if age < 18:
    print("You are not eligible to vote.")
elif age >= 18 and age < 21:
    print("You are eligible to vote, but not to buy alcohol.")
else:
    print("You are eligible to vote and buy alcohol.")