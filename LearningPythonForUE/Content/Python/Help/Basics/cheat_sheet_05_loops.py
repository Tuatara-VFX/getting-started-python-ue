# For loop
for number in range(1, 11):
    print(number)

# While loop
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# Break statement
for number in range(1, 11):
    if number == 5:
        break
    print(number)

# Continue statement
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)