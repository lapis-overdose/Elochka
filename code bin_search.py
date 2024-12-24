import sys
import pygame
import pygame_gui
from button import Button


def to_lower_case(s):
    return s.lower()


def recurs(left, right, guessing_num, steps, lies):
    if left > right:
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


def guessing_game(guessing_num):
    left = 0
    right = 100
    steps = 0

    result = recurs(left, right, guessing_num, steps)
    return result


pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guessing Game")

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((56, 299), (443, 81)), manager=MANAGER, object_id="#main_text_entry"
)

BG = pygame.image.load("Sprites/welcome.png")
INGAMEBG = pygame.image.load("Sprites/in_game.png")
GAMEOVER = pygame.image.load("Sprites/end.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Fonts/filicudi.otf", size)


def game_over(final_guess, steps):
    while True:
        SCREEN.blit(GAMEOVER, (0, 0))

        GUESSING_TEXT = get_font(45).render(str(final_guess), True, "White")
        GUESSING_RECT = GUESSING_TEXT.get_rect(center=(630, 299))
        SCREEN.blit(GUESSING_TEXT, GUESSING_RECT)

        STEPS_TEXT = get_font(45).render(str(steps), True, "White")
        STEPS_RECT = STEPS_TEXT.get_rect(center=(630, 407))
        SCREEN.blit(STEPS_TEXT, STEPS_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def game_process(guessing_num):
    left = 0
    right = 100
    steps = 0
    lies = 0
    guessed = False
    final_guess = None

    while not guessed:
        mid = left + (right - left) // 2

        SCREEN.blit(INGAMEBG, (0, 0))
        PLAY_TEXT = get_font(45).render(str(mid), True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(198, 140))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        HIGHER_BUTTON = Button(
            image=pygame.image.load("Sprites/higher_button.png"),
            pos=(198, 369),
            text_input=None,
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )
        LOWER_BUTTON = Button(
            image=pygame.image.load("Sprites/lower_button.png"),
            pos=(602, 369),
            text_input=None,
            font=get_font(63),
            base_color="White",
            hovering_color="Black",
        )

        HIGHER_BUTTON.update(SCREEN)
        LOWER_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if HIGHER_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    if mid >= guessing_num:
                        game_over(guessing_num, steps)
                        return
                    left = mid + 1
                    steps += 1
                if LOWER_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    if mid <= guessing_num:
                        game_over(guessing_num, steps)
                        return
                    right = mid - 1
                    steps += 1

                if left > right:
                    game_over(-1, steps)
                    return

                if mid == guessing_num:
                    guessed = True
                    final_guess = mid

        pygame.display.update()

    game_over(final_guess, steps)


def main_menu():
    guessing_num = ""

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(
            image=pygame.image.load("Sprites/start_button.png"),
            pos=(620, 339),
            text_input="Start",
            font=get_font(65),
            base_color="White",
            hovering_color="Black",
        )

        for button in [START_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Process UI Manager events
            MANAGER.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == "#main_text_entry":
                guessing_num = event.text  # Capture the current text

            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                    try:
                        # Convert text to an integer before starting the game
                        guessing_num_int = int(guessing_num)
                        if 0 <= guessing_num_int <= 100:
                            game_process(guessing_num_int)
                        else:
                            print("Please enter a number between 0 and 100!")
                    except ValueError:
                        print("Invalid input. Please enter a valid number!")

        MANAGER.update(CLOCK.tick(30) / 1000)
        MANAGER.draw_ui(SCREEN)
        pygame.display.update()



main_menu()
