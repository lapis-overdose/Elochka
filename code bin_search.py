def to_lower_case(s):

    return s.lower()

def recurs(left, right, guessing_num, steps):

    if left > right:
        print("Your number is outside the range!")
        return -1


    steps += 1

    mid = left + (right - left) // 2

    response = input(f"Your number {mid}? (enter 'yes', 'higher', or 'lower'): ")

    response = to_lower_case(response)

    if response == "yes":

        if mid == guessing_num:
            return mid
        else:
            print("You're lying! I caught you!")
            return -1
    elif response == "higher":

        if mid >= guessing_num:
            print(f"You're lying! Your number can't be higher than {mid}!")
            return -1

        return recurs(mid + 1, right, guessing_num, steps)
    elif response == "lower":

        if mid <= guessing_num:
            print(f"You're lying! Your number can't be lower than {mid}!")
            return -1

        return recurs(left, mid - 1, guessing_num, steps)
    else:

        print("Invalid input. Please answer 'yes', 'higher', or 'lower'.")
        return recurs(left, right, guessing_num, steps)


left = 0
right = 100
steps = 0

guessing_num = int(input("Please enter your number: "))


if guessing_num < 0 or guessing_num > 100:
    print("Invalid number as you")
else:

    result = recurs(left, right, guessing_num, steps)

    if result != -1:

        print(f"I guessed your number! It's {result}!")
        print(f"It took only {steps} steps to guess your number.")
    else:

        print("Game over, YOU LOST!")