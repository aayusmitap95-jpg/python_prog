
# Create a list named numbers with the numbers 4, 5, and 6
# Given a list named hidden, add 5, remove 2, and then sort.
numbers = [4,5,6]
hidden = [2,3,4,5]
hidden.append(5)
hidden.remove(2)
hidden.sort()
print(numbers)
print(hidden)

#Given a sequence numbers print the median of the sequence. Note: your solution should work if the sequence is a list or tuple.
numbers = [1, 2, 3, 4]
numbers.sort()
n = len(numbers)

if n % 2 == 0:
    mid1 = n // 2
    mid2 = mid1 - 1
    median = (numbers[mid1] + numbers[mid2]) / 2
else:
    mid = n // 2
    median = numbers[mid]
print(median)

#Given a list to_remove create a new set called numbers that contains the all numbers 1 through 10 that are not in to_remove.
to_remove = [3, 4, 5]
all_numbers = set(range(1, 11))
numbers = all_numbers - set(to_remove)
print(sorted(numbers))

#Given a list numbers create a dictionary called counts that contains the number of times each number appears in the list.
numbers = {1, 2, 3}
counts = {1: "one", 2: "two", 3: "three"}
print(numbers)
counts = {}