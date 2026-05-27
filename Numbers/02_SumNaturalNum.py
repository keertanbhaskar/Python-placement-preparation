num = int(input("Enter a number: "))
sum = 0
for i in range(1,num+1):
  sum = sum + i
print(sum)


# maths formula
# time complexity => O(1)
Total = num*(num+1) //2
print("Sum of natural numbers: ",Total)



# sum of numbers in a given range
a=10
b=20
summ =0
for i in range(a,b+1): # range(a,b+1)
  summ = summ + i
print("Sum is: ",summ)

# mathematical Form
print( (b*(b+1)//2) - (a*(a+1)//2) + a)