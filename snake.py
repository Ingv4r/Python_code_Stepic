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


def render_now_score(score):
    value = score_font.render('Your score: ' + str(score), True, yellow)
    dis.blit(value, [0, 0])

def draw_snake(snake_list, color):
    for element in snake_list:
        pygame.draw.circle(dis, color, (element[0], element[1]), 10)

def render_text_and_position(text, color, height): 
    message = font_style.render(text, True, color)
    position_on_center = message.get_rect(center = (dis_width / 2, dis_height / height))
    dis.blit(message, position_on_center)

def gameloop(): 
    pixel = 1
    snake_speed = 180
 
    x1 = dis_width / 2 
    y1 = dis_height / 2 
 
    x1_change = 0 
    y1_change = 0 

    snake_list = []
    length_of_snake = 1
 
    foodx = round(random.randrange(8, dis_width - 8)) 
    foody = round(random.randrange(8, dis_height - 8)) 

    game = True
    game_close = False 
    while game: 
 
        while game_close == True: 
            dis.fill(black) 
            render_text_and_position("Your score: " + str(length_of_snake // 10), white, 3)
            render_text_and_position("Press 'Q' to Quit or 'P' to Play Again", red, 2)
             
            pygame.display.update()        
         
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                        game = False 
                        game_close = False
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q: 
                        game = False 
                        game_close = False
                    if event.key == pygame.K_p: 
                        dis.fill(black) 
                        game_func()


        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game = False 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_a:
                    if len(snake_list) == 1 or snake_list[-1][0] != (snake_list[-2][0] + 1):
                        x1_change = -pixel 
                        y1_change = 0 
                elif event.key == pygame.K_w:
                    if len(snake_list) == 1 or snake_list[-1][1] != (snake_list[-2][1] + 1):
                        x1_change = 0 
                        y1_change = -pixel 
                elif event.key == pygame.K_s:
                    if len(snake_list) == 1 or snake_list[-1][1] != (snake_list[-2][1] - 1):
                        x1_change = 0 
                        y1_change = pixel 
                elif event.key == pygame.K_d: 
                    if len(snake_list) == 1 or snake_list[-1][0] != (snake_list[-2][0] - 1):
                        x1_change = pixel 
                        y1_change = 0 
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: 
            game_close = True  
 
        x1 += x1_change 
        y1 += y1_change 
        
        dis.fill(black)

        pygame.draw.circle(dis, green, (foodx, foody), 8)

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1:1]:
            if x == snake_head:
                game_close = True
        
        draw_snake(snake_list, white)
        render_now_score(length_of_snake // 10)
 
        pygame.display.update() 
 
        if (foodx - 11) <= x1 <= (foodx + 11) and (foody - 11) <= y1 <= (foody + 11):
            foodx = round(random.randrange(8, dis_width - 8)) 
            foody = round(random.randrange(8, dis_height - 8))
            length_of_snake += 10
        
        clock.tick(snake_speed) 
 
    pygame.quit() 
    quit() 
 
def game_func():
    while True:
        gameloop()


if __name__ == '__main__':
    game_func()    
