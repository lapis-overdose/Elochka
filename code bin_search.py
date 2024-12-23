import sys
import pygame
from pygame.examples.aliens import SCORE

from button import Button


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



FONT = pygame.font.SysFont("arial", 70)
text = FONT.render("Guessing Game", True, (0, 0, 0))
text_rect = text.get_rect(center=(WIDTH/2, 150))


CLOCK = pygame.time.Clock()

BG = pygame.image.load("Sprites/welcome.png")
INGAMEBG = pygame.image.load("Sprites/in_game.png")
GAMEOVER = pygame.image.load("Sprites/end.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Fonts/filicudi.otf", size)



def game_over():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        SCREEN.blit(GAMEOVER, (0, 0))

        GUESSING_TEXT = get_font(45).render("1337", True, "White")
        GUESSING_RECT = GUESSING_TEXT.get_rect(center=(630, 299))
        SCREEN.blit(GUESSING_TEXT, GUESSING_RECT)

        STEPS_TEXT = get_font(45).render("1337", True, "White")
        STEPS_RECT = STEPS_TEXT.get_rect(center=(630, 407))
        SCREEN.blit(STEPS_TEXT, STEPS_RECT)

        LIES_TEXT = get_font(45).render("234", True, "White")
        LIES_RECT = LIES_TEXT.get_rect(center=(310, 407))
        SCREEN.blit(LIES_TEXT, LIES_RECT)




        PLAY_BACK = Button(image=None, pos=(640, 520),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def game_process():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        SCREEN.blit(INGAMEBG, (0, 0))

        PLAY_TEXT = get_font(45).render("213", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(198, 140))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        HIGHER_BUTTON = Button(image=pygame.image.load("Sprites/higher_button.png"), pos=(198, 369),
                            text_input=None, font=get_font(75), base_color="White", hovering_color="Green")

        HIGHER_BUTTON.changeColor(PLAY_MOUSE_POS)
        HIGHER_BUTTON.update(SCREEN)

        LOWER_BUTTON = Button(image=pygame.image.load("Sprites/lower_button.png"), pos=(602, 369),
                             text_input=None, font=get_font(63), base_color="White", hovering_color="Black")

        LOWER_BUTTON.changeColor(PLAY_MOUSE_POS)
        LOWER_BUTTON.update(SCREEN)

        HIGHER_BUTTON.changeColor(PLAY_MOUSE_POS)
        HIGHER_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HIGHER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        START_BUTTON = Button(image=pygame.image.load("Sprites/start_button.png"), pos=(620, 339),
                             text_input="Start", font=get_font(65), base_color="White", hovering_color="Black")


        for button in [START_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_process()

        pygame.display.update()


main_menu()