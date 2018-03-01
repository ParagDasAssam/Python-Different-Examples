"""
Create a program that asks the user for a number
and then prints out a list of all the divisors of that number.
"""
a = input("Enter a number: ")
num = []
for i in range(a):
    b = i + 1
    if (a % b == 0):
        num.append(b)

print num
