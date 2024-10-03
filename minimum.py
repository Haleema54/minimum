'''
6) Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
program:

# Input: Read the number of elements
n = int(input())

# Input: Create a tuple by reading n elements from the user
elements = tuple(int(input()) for _ in range(n))

# Calculate the minimum value in the tuple
min_value = min(elements)

# Output: Print the minimum value
print(min_value)
'''
