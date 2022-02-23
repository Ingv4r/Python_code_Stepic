import pygame
import random

pygame.init() 

# display variables 
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height)) 
# colors
white = (255, 255, 255) 
black = (30, 30, 50)
yellow = (255, 255, 102) 
red = (213, 50, 80) 
green = (0, 255, 0) 
# display update variable
clock = pygame.time.Clock() 
# font variables
font_style = pygame.font.SysFont('bahnschrift', 30)
score_font = pygame.font.SysFont('comicsansms', 35) 
#snake variables
x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0 
y1_change = 0 
snake_list = []
length_of_snake = 1
snake_speed = 180
# food variables
food_radius = 8
foodx = round(random.randrange(food_radius, dis_width - food_radius)) 
foody = round(random.randrange(food_radius, dis_height - food_radius)) 
# game bool variables
game = True
endgame = False

pygame.display.set_caption("Igor's first snake game v1.01")
dis.fill(black)

def game_settings(width, height, dificulty):
    global dis_width, dis_height, food_radius, snake_speed
    if dificulty == 'easy':
        food_radius = 10
        snake_speed = 150
    elif dificulty == 'medium':
        food_radius = 7
        snake_speed = 190
    elif dificulty == 'hard':
        food_radius = 5
        snake_speed = 220
    dis_width = width
    dis_height = height

def quit_game():
    pygame.quit()
    quit()

def restart_game():
    global x1, y1, x1_change, y1_change, snake_list, length_of_snake, foodx, foody, game, endgame
    dis.fill(black)
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0 
    y1_change = 0 
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(food_radius, dis_width - food_radius)) 
    foody = round(random.randrange(food_radius, dis_height - food_radius)) 
    game = True
    endgame = False

def endgame_keypress(event):
    if event.key == pygame.K_q:
        quit_game()
    elif event.key == pygame.K_p:  
        dis.fill(black)
        restart_game()

def endgame_dis(score):
    height_of_score = dis_height / 3
    height_of_message = dis_height / 2
    width_of_score = dis_width / 2
    width_of_message = dis_width / 2
    dis.fill(black) 
    render_text_and_position("Your score: " + str(score), score_font, white, dis, width_of_score, height_of_score)
    render_text_and_position("Press 'Q' to Quit or 'P' to Play Again", font_style, red, dis, width_of_message, height_of_message)
             
    pygame.display.update()        
         
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            return endgame_keypress(event)

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
        return True if len(snake_list) == 1 or snake_list[-1][0] != (snake_list[-2][0] + 1) else False
    elif key == 'w':
        return True if len(snake_list) == 1 or snake_list[-1][1] != (snake_list[-2][1] + 1) else False
    elif key == 's':
        return True if len(snake_list) == 1 or snake_list[-1][1] != (snake_list[-2][1] - 1) else False
    elif key == 'd': 
        return True if len(snake_list) == 1 or snake_list[-1][0] != (snake_list[-2][0] - 1) else False

def draw_snake(snake_list, color = white, circle_rad = 10):
    for element in snake_list:
        pygame.draw.circle(dis, color, (element[0], element[1]), circle_rad)

def render_text_and_position(text, font, color, display, width = 0, height = 0): 
    message = font.render(text, True, color)
    position = [0, 0]
    if width != 0 and height != 0:
        position = message.get_rect(center = (width, height))
    display.blit(message, position)
    
def draw_food():
    pygame.draw.circle(dis, green, (foodx, foody), food_radius)

def check_borders():
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: 
        global endgame
        endgame = True 

def snake_form():
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
            del snake_list[0]
    if len(snake_list) > 1:
        if snake_list[-1] == snake_list[-2]:
            snake_list.pop()
    return snake_head

def Ouroboros(snake_head):
    # snake eat self
    for x in snake_list[:-1:1]:
            if x == snake_head:
                global endgame
                endgame = True

def snake_eat():
    global foodx, foody, length_of_snake
    if (foodx - 11) <= x1 <= (foodx + 11) and (foody - 11) <= y1 <= (foody + 11):
            foodx = round(random.randrange(food_radius, dis_width - food_radius)) 
            foody = round(random.randrange(food_radius, dis_height - food_radius)) 
            length_of_snake += 10

def gameloop(): 
    global x1, y1, x1_change, y1_change, snake_list, length_of_snake, foodx, foody, game, endgame

    while game: 
        # get event block
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                quit_game()
            elif event.type == pygame.KEYDOWN:
                keypress = move_keypress(event)
                if keypress != None:
                    x1_change = keypress[0]
                    y1_change = keypress[1]

        # snake form block        
        x1 += x1_change
        y1 += y1_change
        head = snake_form()

        # collision block
        Ouroboros(head)
        while endgame == True: 
            endgame_dis(score)
        check_borders()
        snake_eat()
        
        # draw block
        dis.fill(black)
        draw_food()
        draw_snake(snake_list)
        score = length_of_snake // 10
        render_text_and_position('Your score: ' + str(score), score_font, yellow, dis)
        pygame.display.update() 

        clock.tick(snake_speed) 
 
    quit_game()
    
if __name__ == '__main__': 
    gameloop()
