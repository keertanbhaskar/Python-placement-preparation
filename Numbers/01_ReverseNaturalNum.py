# Way - 1 => use for loop

number = int(input("Enter a number: "))
for i in range(number,0,-1):
  print(i,end=" ")


print("\n")

# Way - 2 => use for loop
i = number
while i > 0:
  print(i,end=" ")
  i -= 1
