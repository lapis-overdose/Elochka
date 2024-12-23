'''
def to_lower_case(s):
    # Convert the input string to lowercase
    return s.lower()

def recurs(left, right, guessing_num, steps):
    # Base case: if the range is invalid, the number is outside the range
    if left > right:
        print("Your number is outside the range!")
        return -1

    # Increment the step count
    steps += 1
    # Calculate the middle point of the current range
    mid = left + (right - left) // 2
    # Ask the user if the guessed number is correct, higher, or lower
    response = input(f"Your number {mid}? (enter 'yes', 'higher', or 'lower'): ")
    # Convert the response to lowercase
    response = to_lower_case(response)

    if response == "yes":
        # If the guessed number is correct, check for honesty
        if mid == guessing_num:
            return mid
        else:
            print("You're lying! I caught you!")
            return -1
    elif response == "higher":
        # If the guessed number is higher, check for honesty
        if mid >= guessing_num:
            print(f"You're lying! Your number can't be higher than {mid}!")
            return -1
        # Recursively guess in the higher half of the range
        return recurs(mid + 1, right, guessing_num, steps)
    elif response == "lower":
        # If the guessed number is lower, check for honesty
        if mid <= guessing_num:
            print(f"You're lying! Your number can't be lower than {mid}!")
            return -1
        # Recursively guess in the lower half of the range
        return recurs(left, mid - 1, guessing_num, steps)
    else:
        # Handle invalid input
        print("Invalid input. Please answer 'yes', 'higher', or 'lower'.")
        return recurs(left, right, guessing_num, steps)

# Example usage
left = 0
right = 100
steps = 0
# Ask the user to enter their number
guessing_num = int(input("Please enter your number: "))

# Check if the number is within the valid range
if guessing_num < 0 or guessing_num > 100:
    print("Invalid number as you")
else:
    # Start the guessing game
    result = recurs(left, right, guessing_num, steps)

    if result != -1:
        # If the number is guessed correctly, print the result
        print(f"I guessed your number! It's {result}!")
        print(f"It took only {steps} steps to guess your number.")
    else:
        # If the game ends without guessing the number, print the game over message
        print("Game over, YOU LOST!")
'''

