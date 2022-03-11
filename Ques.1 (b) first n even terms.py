#Q1. Write a function that finds the sum of the
#b) first n even terms
num = int(input("Enter n: "))
sum = 0

for i in range(1, num + 1):

    if((i % 2) == 0):
        sum += i

print("\nSum of even numbers from 1 to", num, "is :", sum)
