#Q1. Write a function that finds the sum of the
#a) first n odd terms
num = int(input("Enter n: "))
sum = 0;

for i in range(1, num + 1):

    if(not (i % 2) == 0):
        sum += i;

print("\nSum of odd numbers from 1 to", num, "is :", sum)
