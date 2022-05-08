import random as rand
import pygame
import hello_menu

class GameVariables():
    '''docstring'''
    def __init__(self, dis_width, dis_height,
                 food_radius, snake_speed) -> None:
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.dis = pygame.display.set_mode((dis_width, dis_height))
        self.white = (255, 255, 255)
        self.black = (30, 30, 50)
        self.yellow = (255, 255, 102)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont('bahnschrift', 30)
        self.score_font = pygame.font.SysFont('comicsansms', 35)
        self.snake_speed = snake_speed
        self.food_radius = food_radius
        self.food_coords = []
        self.area = []
        self.snake_rad = 10
        self.x = dis_width / 2
        self.y = dis_height / 2
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.length_of_snake = 1
        self.game = True
        self.endgame = False

pygame.init()
pygame.display.set_caption("Igor's first snake game v1.5")

def menu_button():
    '''docstring'''
    menu_box = pygame.Rect(snake.dis_width / 2.27,
                           snake.dis_height / 1.3 , 85, 40)
    font = pygame.font.Font(None, 40)
    color = (255, 255, 255)
    text = font.render('Menu', True, color)
    snake.dis.blit(text, (menu_box.x+5, menu_box.y+7))
    pygame.draw.rect(snake.dis, color, menu_box, 2)
    return menu_box

def game_settings(width, height, dificulty):
    '''docstring'''
    global snake
    if dificulty == 'easy':
        food_radius = 10
        snake_speed = 150
    elif dificulty == 'medium':
        food_radius = 7
        snake_speed = 190
    elif dificulty == 'hard':
        food_radius = 5
        snake_speed = 220
    snake = GameVariables(width, height, food_radius, snake_speed)
    return snake

def quit_game():
    '''docstring'''
    pygame.quit()
    quit()

def restart_game():
    '''docstring'''
    snake.dis.fill(snake.black)
    snake.x = snake.dis_width / 2
    snake.y = snake.dis_height / 2
    snake.x_change = 0
    snake.y_change = 0
    snake.snake_list = []
    snake.length_of_snake = 1
    food_coord()
    snake.game = True
    snake.endgame = False

def endgame_keypress(event):
    '''docstring'''
    if event.key == pygame.K_q:
        quit_game()
    elif event.key == pygame.K_p:
        snake.dis.fill(snake.black)
        restart_game()

def endgame_dis(score):
    '''docstring'''
    height_of_score = snake.dis_height / 3
    height_of_message = snake.dis_height / 2
    width_of_score = snake.dis_width /  2
    width_of_message = snake.dis_width / 2
    snake.dis.fill(snake.black)
    render_text_and_position("Your score: " + str(score),
                             snake.score_font, snake.white,
                             snake.dis, width_of_score,
                             height_of_score)
    render_text_and_position("Press 'Q' to Quit or 'P' to Play Again",
                             snake.font_style, snake.red, snake.dis,
                             width_of_message, height_of_message)
    menu = menu_button()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            return endgame_keypress(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu.collidepoint(event.pos):
                snake.endgame = False
                snake.game = False
                hello_menu.menu_from_snake()

def move_keypress(event) -> tuple:
    '''docstring'''
    step_size = 1
    if event.key == pygame.K_w and check_direction('w'):
        delta_x = 0
        delta_y = -step_size
        return delta_x, delta_y
    if event.key == pygame.K_a and check_direction('a'):
        delta_x = -step_size
        delta_y = 0
        return delta_x, delta_y
    if event.key == pygame.K_s and check_direction('s'):
        delta_x = 0
        delta_y = step_size
        return delta_x, delta_y
    if event.key == pygame.K_d and check_direction('d'):
        delta_x = step_size
        delta_y = 0
        return delta_x, delta_y

def check_direction(key) -> bool:
    '''docstring'''
    if key == 'a':
        return (True if len(snake.snake_list) == 1 or
                snake.snake_list[-1][0] !=
                (snake.snake_list[-2][0] + 1) else False)
    if key == 'w':
        return (True if len(snake.snake_list) == 1 or
                snake.snake_list[-1][1] !=
                (snake.snake_list[-2][1] + 1) else False)
    if key == 's':
        return (True if len(snake.snake_list) == 1 or
                snake.snake_list[-1][1] !=
                (snake.snake_list[-2][1] - 1) else False)
    if key == 'd':
        return (True if len(snake.snake_list) == 1 or
                snake.snake_list[-1][0] !=
                (snake.snake_list[-2][0] - 1) else False)

def draw_snake(snake_list):
    '''docstring'''
    color_body = snake.white
    color_head = snake.yellow
    for element in snake_list:
        if element == snake_list[-1]:
            pygame.draw.circle(snake.dis, color_head,
                           (element[0], element[1]),
                            snake.snake_rad)
        else:
            pygame.draw.circle(snake.dis, color_body,
                           (element[0], element[1]),
                           snake.snake_rad)

def render_text_and_position(text, font, color,
                             display, width = 0,
                             height = 0):
    '''docstring'''
    message = font.render(text, True, color)
    position = [0, 0]
    if width != 0 and height != 0:
        position = message.get_rect(center = (width, height))
    display.blit(message, position)

def draw_food(food):
    '''docstring'''
    pygame.draw.circle(
        snake.dis, snake.green,
        food,
        snake.food_radius
        )

def check_borders():
    '''docstring'''
    if (
            snake.x >= snake.dis_width or snake.x < 0 or
            snake.y >= snake.dis_height or snake.y < 0):
        snake.endgame = True

def snake_form():
    '''docstring'''
    snake_head = (snake.x, snake.y)
    snake.snake_list.append(snake_head)
    if len(snake.snake_list) > snake.length_of_snake:
        del snake.snake_list[0]
    if len(snake.snake_list) > 1:
        if snake.snake_list[-1] == snake.snake_list[-2]:
            snake.snake_list.pop()
    return snake_head

def snake_eat_self(snake_head):
    '''docstring'''
    for elem in snake.snake_list[:-1:1]:
        if elem == snake_head:
            snake.endgame = True

def food_coord():
    '''docstring'''
    k = snake.food_radius
    snake.food_coords = [
        rand.randrange(k, snake.dis_width-k),
        rand.randrange(k, snake.dis_height-k)
        ]

def snake_eat(food):
    '''docstring'''
    k = snake.food_radius + snake.snake_rad - 1
    if (
        (food[0]-k) <= snake.x <= (food[0]+k)
        and
        (food[1]-k) <= snake.y <= (food[1]+k)
    ):
        food_coord()
        snake.length_of_snake += 10

def gameloop():
    '''docstring'''
    snake.dis.fill(snake.black)

    while snake.game:
        # event block
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                keypress = move_keypress(event)
                if keypress is not None:
                    snake.x_change = keypress[0]
                    snake.y_change = keypress[1]

        # game objects form block
        score = snake.length_of_snake // 10
        snake.x += snake.x_change
        snake.y += snake.y_change
        head = snake_form()
        if not snake.food_coords:
            food_coord()
        # collision block
        snake_eat_self(head)
        while snake.endgame:
            endgame_dis(score)
        check_borders()
        snake_eat(snake.food_coords)
        # draw block
        snake.dis.fill(snake.black)
        draw_food(snake.food_coords)
        draw_snake(snake.snake_list)
        render_text_and_position(
            'Your score: ' + str(score),
            snake.score_font, snake.yellow, snake.dis
            )
        pygame.display.update()

        snake.clock.tick(snake.snake_speed)

    quit_game()

if __name__ == '__main__':
    snake = game_settings(600, 400, 'hard')
    gameloop()
