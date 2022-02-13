import pygame
import time 
import random 

pygame.init() 
 
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height)) 
pygame.display.set_caption("Igor's first snake game 1.0") 
 
white = (255, 255, 255) 
black = (30, 30, 50)
yellow = (255, 255, 102) 
red = (213, 50, 80) 
green = (0, 255, 0) 
 
dis.fill(black)
 
clock = pygame.time.Clock() 
 
font_style = pygame.font.SysFont('bahnschrift', 30)
score_font = pygame.font.SysFont('comicsansms', 35) 

snake_speed = 180
food_radius = 8

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


def quit_game():
    pygame.quit()
    quit()

def endgame_keypress(event):
    global x1, y1, x1_change, y1_change, snake_list, length_of_snake, foodx, foody, game, endgame
    if event.key == pygame.K_q:
        quit_game()
    elif event.key == pygame.K_p:  
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

def endgame_dis(score, height_of_score = 3,
    height_of_message = 2,
    width_of_score = 2,
    width_of_message = 2):
    dis.fill(black) 
    render_text_and_position("Your score: " + str(score), score_font, white, width_of_score, height_of_score)
    render_text_and_position("Press 'Q' to Quit or 'P' to Play Again", font_style, red, width_of_message, height_of_message)
             
    pygame.display.update()        
         
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            return endgame_keypress(event)


def move_keypress(event, snake_list):
    stepSize = 1
    if event.key == pygame.K_w:
        if check_collision(snake_list, 'w'):
            deltaX = 0
            deltaY = -stepSize
            return deltaX, deltaY
    elif event.key == pygame.K_a:
        if check_collision(snake_list, 'a'):
            deltaX = -stepSize
            deltaY = 0
            return deltaX, deltaY
    elif event.key == pygame.K_s:
        if check_collision(snake_list, 's'):
            deltaX = 0
            deltaY = stepSize
            return deltaX, deltaY
    elif event.key == pygame.K_d:
        if check_collision(snake_list, 'd'):
            deltaX = stepSize
            deltaY = 0
            return deltaX, deltaY

def check_collision(snake_list, key): # -> bool
    if key == 'a':
        if len(snake_list) == 1 or snake_list[-1][0] != (snake_list[-2][0] + 1): 
            return True 
        else:
            return False
    elif key == 'w':
        if len(snake_list) == 1 or snake_list[-1][1] != (snake_list[-2][1] + 1):
            return True
        else:
            return False
    elif key == 's':
        if len(snake_list) == 1 or snake_list[-1][1] != (snake_list[-2][1] - 1):
            return True
        else:
            return False
    elif key == 'd': 
        if len(snake_list) == 1 or snake_list[-1][0] != (snake_list[-2][0] - 1):
            return True
        else:
            return False

def draw_snake(snake_list, color = white, circle_rad = 10):
    for element in snake_list:
        pygame.draw.circle(dis, color, (element[0], element[1]), circle_rad)


def render_text_and_position(text, font, color, width = 0, height = 0): 
    message = font.render(text, True, color)
    position = [0, 0]
    if width != 0 and height != 0:
        position = message.get_rect(center = (dis_width / width, dis_height / height))
    dis.blit(message, position)
    

def gameloop(): 
    global x1, y1, x1_change, y1_change, snake_list, length_of_snake, foodx, foody, game, endgame

    while game: 
 
        while endgame == True: 
            endgame_dis(score)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                quit_game()
            elif event.type == pygame.KEYDOWN:
                keypress = move_keypress(event, snake_list)
                if keypress != None:
                    x1_change = keypress[0]
                    y1_change = keypress[1]

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: 
            endgame = True  
 
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(black)

        pygame.draw.circle(dis, green, (foodx, foody), food_radius)

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1:1]:
            if x == snake_head:
                endgame = True
        
        draw_snake(snake_list)

        score = length_of_snake // 10
        render_text_and_position('Your score: ' + str(score), score_font, yellow)
 
        pygame.display.update() 
 
        if (foodx - 11) <= x1 <= (foodx + 11) and (foody - 11) <= y1 <= (foody + 11):
            foodx = round(random.randrange(food_radius, dis_width - food_radius)) 
            foody = round(random.randrange(food_radius, dis_height - food_radius)) 
            length_of_snake += 10
        
        clock.tick(snake_speed) 
 
    quit_game()
 
 
gameloop()
