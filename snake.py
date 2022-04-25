import random as rand
import pygame 
import hello_menu

class GameVariables():

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
        self.food_coords = list()
        self.area = dict()
        self.snake_rad = 10
        self.x1 = dis_width / 2
        self.y1 = dis_height / 2
        self.x1_change = 0 
        self.y1_change = 0 
        self.snake_list = list()
        self.length_of_snake = 1
        self.game = True
        self.endgame = False


pygame.init()
pygame.display.set_caption("Igor's first snake game v1.5")

def menu_button():
    menu_box = pygame.Rect(snake.dis_width / 2.27, 
                           snake.dis_height / 1.3 , 85, 40)
    font = pygame.font.Font(None, 40)
    color = (255, 255, 255)
    text = font.render('Menu', True, color)
    snake.dis.blit(text, (menu_box.x+5, menu_box.y+7))
    pygame.draw.rect(snake.dis, color, menu_box, 2)
    return menu_box

def game_settings(width, height, dificulty):
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

def quit_game():
    pygame.quit()
    quit()

def restart_game():
    snake.dis.fill(snake.black)
    snake.x1 = snake.dis_width / 2
    snake.y1 = snake.dis_height / 2
    snake.x1_change = 0 
    snake.y1_change = 0 
    snake.snake_list = []
    snake.length_of_snake = 1
    food_coords()
    food_in_snake()
    snake.game = True
    snake.endgame = False

def endgame_keypress(event):
    if event.key == pygame.K_q:
        quit_game()
    elif event.key == pygame.K_p:  
        snake.dis.fill(snake.black)
        restart_game()

def endgame_dis(score): 
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
    stepSize = 1
    if event.key == pygame.K_w and check_direction('w'):
        deltaX = 0
        deltaY = -stepSize
        return deltaX, deltaY
    elif event.key == pygame.K_a and check_direction('a'):
        deltaX = -stepSize
        deltaY = 0
        return deltaX, deltaY
    elif event.key == pygame.K_s and check_direction('s'):
        deltaX = 0
        deltaY = stepSize
        return deltaX, deltaY
    elif event.key == pygame.K_d and check_direction('d'):
        deltaX = stepSize
        deltaY = 0
        return deltaX, deltaY

def check_direction(key) -> bool: 
    if key == 'a':
        return (True if len(snake.snake_list) == 1 or
                snake.snake_list[-1][0] != 
                (snake.snake_list[-2][0] + 1) else False)
    elif key == 'w':
        return (True if len(snake.snake_list) == 1 or 
                snake.snake_list[-1][1] != 
                (snake.snake_list[-2][1] + 1) else False)
    elif key == 's':
        return (True if len(snake.snake_list) == 1 or 
                snake.snake_list[-1][1] != 
                (snake.snake_list[-2][1] - 1) else False)
    elif key == 'd': 
        return (True if len(snake.snake_list) == 1 or
                snake.snake_list[-1][0] != 
                (snake.snake_list[-2][0] - 1) else False)

def draw_snake(snake_list):
    color_body = snake.white
    color_head = snake.red
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
    message = font.render(text, True, color)
    position = [0, 0]
    if width != 0 and height != 0:
        position = message.get_rect(center = (width, height))
    display.blit(message, position)

def draw_food(food):
    pygame.draw.circle(
        snake.dis, snake.green, 
        food, 
        snake.food_radius
        )

def check_borders():
    if (
            snake.x1 >= snake.dis_width or snake.x1 < 0 or
            snake.y1 >= snake.dis_height or snake.y1 < 0): 
        snake.endgame = True 

def snake_form():
    snake_head = []
    snake_head.append(snake.x1)
    snake_head.append(snake.y1)
    snake.snake_list.append(snake_head)
    if len(snake.snake_list) > snake.length_of_snake:
        del snake.snake_list[0]
    if len(snake.snake_list) > 1:
        if snake.snake_list[-1] == snake.snake_list[-2]:
            snake.snake_list.pop()
    return snake_head

def snake_eat_self(snake_head):
    for x in snake.snake_list[:-1:1]:
            if x == snake_head:
                snake.endgame = True

def area():
    # form playing field by cells of food size
    k = snake.food_radius
    y = snake.dis_height
    x = snake.dis_width 
    for col in range(0, x, k):
        for line in range(0, y, k):
            snake.area[(col, line)] = True
        
def avaible_food_cell():
    # make 'False' cells where is snake now
    k = snake.food_radius
    game = snake.area
    for cell in game.keys():
        for elem in snake.snake_list:
            if (
                cell[0] <= elem[0] <= (cell[0]+k) 
                and   
                cell[1] <= elem[1] <= (cell[1]+k)
                ):
                snake.area[cell] = False

def food_coord():
    # choice cell from 'True' cells
    k = snake.food_radius // 2
    coords = list()
    for i in snake.area.keys():
        if snake.area[i]:
            coords.append(list(i))
    food = rand.choice(coords)
    food[0] += k
    food[1] += k
    snake.food_coords = list(food)


'''def food_in_snake():
    food = snake.food_coords
    k = snake.snake_rad + snake.food_radius
    for i in snake.snake_list:
        if((food[0]-k) <= i[0] <= (food[0]+k) and
        (food[1]-1) <= i[1] <= (food[1]+k)):
            snake.list.append(food)
            food_coords()
            if snake.food_coords not in snake.list:
                food_in_snake()
            else:
                food_coords()
        else:
            snake.list = []'''

def snake_eat(food):
    k = snake.food_radius*2
    if ((food[0]-k) <= snake.x1 <= (food[0]+k) and 
    (food[1]-k) <= snake.y1 <= (food[1]+k)):
        food_coord()
        snake.length_of_snake += 10
        

def gameloop(): 
    snake.dis.fill(snake.black)

    while snake.game: 
        # event block
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                quit_game()
            elif event.type == pygame.KEYDOWN:
                keypress = move_keypress(event)
                if keypress != None:
                    snake.x1_change = keypress[0]
                    snake.y1_change = keypress[1]

        # game objects form block  
        snake.x1 += snake.x1_change
        snake.y1 += snake.y1_change
        head = snake_form()
        area()
        avaible_food_cell()
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
        score = snake.length_of_snake // 10
        render_text_and_position(
            'Your score: ' + str(score), 
            snake.score_font, snake.yellow, snake.dis
            )
        pygame.display.update() 

        snake.clock.tick(snake.snake_speed) 

    quit_game()

if __name__ == '__main__':
    snake = GameVariables(800, 600, 5, 220)
    gameloop()
