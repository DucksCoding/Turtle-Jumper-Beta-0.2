#game options.
TITLE = "Turtle Jump"
WIDTH = 600
HEIGHT = 800
FPS = 60
FONT_NAME = 'Impact'
HS_FILE = "highscore.txt"

#player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 80, WIDTH, 80),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 400, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]



#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
