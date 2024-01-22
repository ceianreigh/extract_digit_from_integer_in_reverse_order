# Write a Program to extract each digit from an integer in the reverse order.

# pseudocode

# ask user to enter a number
number = int(input("Enter a number: "))

# print the entered number
print(number)

# reverse the number
reversed_number = 0
while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

print(reversed_number)
# print the reversed number with spaces between each digit
