#Modify the code below to print 0-9 on a single line.
for i in range(10):
    print(i)
print()
#Write a function named add that takes two arguments and returns their sum.
def add(a, b):
    sum = a + b
    return sum

#create a function called add_two that takes x as an argument and returns the value of x plus 2
x = 5
def add_one():
    global x 
    x = x + 1
    return x
def add_two(x):
    return x + 2
    
print(add_one())
print(add_two(5))