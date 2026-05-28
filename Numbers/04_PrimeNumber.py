# Method 1

# Algorithm 1

n = 5
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count > 2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")




# Algorithm 2

n = 5
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if n == 0 or n == 1:
    print(f"{n} is not a Prime Number")
elif count > 2:
    print(f"{n} is not a Prime Number")
else:
    print(f"{n} is a Prime Number")




# Algorithm 3

n = 5
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if n < 2 or count > 2:
    print(f"{n} is not a Prime Number")
else:
    print(f"{n} is a Prime Number")





# Method 2

isprime = True
n = 5

if n < 2:
    isprime = False
else:
    for i in range(2, n):
        if n % i == 0:
            isprime = False
            break

if isprime:
    print("Number is a Prime Number")
else:
    print("Number is not a Prime Number")




# Method 3

isprime = True
n = 5

if n < 2:
    isprime = False
else:
    x = n // 2
    for i in range(2, x + 1):
        if n % i == 0:
            isprime = False
            break

if isprime:
    print("Number is a Prime Number")
else:
    print("Number is not a Prime Number")