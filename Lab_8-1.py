# Author: Caleb Moura

# Function to find sum of all numbers up to and including user input, parameters, and return.
def find_sum(user_input):
    """
    Calculate the sum of all numbers up to and including the given input.

    - user_input (int): The user-provided integer.

    - int: The sum of all numbers up to and including the user input.
    """
    total = 0
    for number in range(1, user_input + 1):
        total += number
    return total

# Prompt user to input integer.
user_integer = int(input("Enter an integer: "))

# Call function and store output as variable.
sum_result = find_sum(user_integer)

# Print final sum.
print(f"The sum of numbers up to {user_integer} is: {sum_result}")