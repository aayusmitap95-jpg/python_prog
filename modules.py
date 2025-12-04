#Use the sys module to print the current Python version and platform.
import sys

print("Python Version:", sys.version)
print("Platform:", sys.platform)

#Using randint create a random number x from 1 to 4. Then, print the number as a word. For example, if the number is 1, print one.
import random
x = random.randint(1, 4)
if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
else:
    print("four")

#Using the math modules sqrt function, print the square root of 90.
import math
print(math.sqrt(90))

#Using the os module, print the environment variables of the HOME directory
import os
print(os.getenv("HOME"))