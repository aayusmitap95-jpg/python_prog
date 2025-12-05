#Provide a value for x such that only the last print statement is executed.
x = 6

if x > 6:
    print('x is greater than 6')

if x < 6:
    print('x is less than 6')
    
if x >= 6:
    print('x is greater than or equal to 6')

# Given a number x print out the following:

# If x is positive, print out x is positive.
# If x is negative, print out x is negative.
# If x is 0, print out x is 0.
x = -87
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negetive")
else:
    print("x is 0")

#Write a while loop that prints out the numbers 0 to 9.
x = 0
while x < 10:
    x = x + 1
    print(x)
#Write a for loop that prints out the numbers 0 to 9.
for x in range(10):
    print(x)

#Given a number x, use continue to print out even numbers from 0 to x. Use break Stop if you reach a number greater than 20.
x = 34 
for i in range(x + 1):
    if i % 2 != 0:
         continue
    if i > 20:
        break
    print(i)

#Given the variables x,y, and z, print the sum of the values that are not None.
x = 2
y = 3
z = 4
sum = x + y + z
print(sum)

# Given the variables x,y, and z print the following:

# if x and y are greater than 10, print step 1 is True
# if z or y is greater than x, print step 2 is True
# if step 2 is False, print step 2 is False
x = 6
y = 67
z = 44
if x > 10 and y > 10:
    print("step 1 is true")
elif z > x or y > x:
    print("step 2 is true")
else:
    print("step 2 is false")    
