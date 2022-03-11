#Q1. Write a function that finds the sum of the
#c) 1, 2, 4, 3, 5, 7, 9, 6, 8, 10, 11, 13.. till n-th term
num =int(input("enter"))
if num < 0:
    print("Enter a positive number")
else:
    sum = 0
   
while(num > 0):
    sum += num
    num -= 1
print("The sum is", sum)
