from smtplib import SMTPConnectError

import pygame
import sys


def to_lower_case(s):
    return s.lower()

def recurs(left, right, guessing_num, steps):
    if left > right:
        print("Your number is outside the range!")
        return -1


    mid = left + (right - left) // 2


    response = input(f"Is your number {mid}? (enter 'yes', 'higher', or 'lower'): ")
    response = to_lower_case(response)


    steps += 1

    if response == "yes":
        if mid == guessing_num:
            print(f"I guessed your number! It's {mid}!")
            print(f"It took me {steps} steps to guess your number.")
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

# Example usage
def guessing_game():
    left = 0
    right = 100
    steps = 0

    try:
        guessing_num = int(input("Please enter your number (between 0 and 100): "))

        if guessing_num < 0 or guessing_num > 100:
            print("Invalid number. Please choose a number between 0 and 100.")

        else:
            result = recurs(left, right, guessing_num, steps)

            if result == -1:
                print("Game over! I couldn't guess your number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guessing Game")

#ICON = pygame.image.load("icon.png")
#pygame.display.set_icon(pygame.image.load(ICON)

#BACKGROUND = pygame.image.load("images/background.jpg")

FONT = pygame.font.SysFont("arial", 70)
text = FONT.render("Guessing Game", True, (0, 0, 0))
text_rect = text.get_rect(center=(WIDTH/2, 150))


CLOCK = pygame.time.Clock()



def game_init():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Код отображения

        SCREEN.fill(("white"))
        SCREEN.blit(text, text_rect)

        pygame.display.update()

        CLOCK.tick(30)

game_init()