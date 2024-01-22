# Write a Program to extract each digit from an integer in the reverse order.

# pseudocode

# ask user to enter a number
number = int(input("Enter a number: "))

# print the entered number
print(number)

# reverse the number
while number > 0:
    # extract the last digit
    reversed_number = number % 10
    # remove the last digit
    number = number // 10

    # print the reversed number with spaces between each digit
    print(reversed_number, end=" ")
