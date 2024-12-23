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

BACKGROUND = pygame.image.load("Sprites/welcome.png")


FONT = pygame.font.SysFont("arial", 70)
text = FONT.render("Guessing Game", True, (0, 0, 0))
text_rect = text.get_rect(center=(WIDTH/2, 150))


CLOCK = pygame.time.Clock()

'''
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
'''

def game_init():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Код отображения

        SCREEN.fill(("white"))
        SCREEN.blit(text, text_rect)
        SCREEN.blit(BACKGROUND, (0, 0))

        pygame.display.update()

        CLOCK.tick(30)

game_init()