import pygame as pg
import snake
from snake import *

pg.init()
pg.display.set_caption("Igor's first snake game v1.5")

class Menu_var():
    def __init__(self) -> None:
        self.text_width = '600'
        self.text_height = '400'
        self.screen = pg.display.set_mode((int(self.text_width), int(self.text_height)))
        self.font = pg.font.Font(None, 30)
        self.clock = pg.time.Clock()
        self.done = False

class buttons_var():
    def __init__(self) -> None:
        # buttons position
        self.width_box = pg.Rect(330, 120, 58, 30)
        self.height_box = pg.Rect(430, 120, 58, 30)
        self.box_easy = pg.Rect(300, 180, 55, 30)
        self.box_med = pg.Rect(380, 180, 85, 30)
        self.box_hard = pg.Rect(485, 180, 57, 30)
        self.Start_box = pg.Rect(200, 290, 75, 30)
        self.Quit_box = pg.Rect(330, 290, 75, 30)
        # activation of color
        self.active_width = False
        self.active_height= False
        self.active_easy = False
        self.active_med = False
        self.active_hard = False
        # color of buttons
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.color_width = False
        self.color_height = False
        self.color_easy = False
        self.color_med = False
        self.color_hard = False

mn = Menu_var()
btn = buttons_var() 

def start_game():
    mn.done = True
    if btn.active_easy == True:
        dificulty = 'easy'
    elif btn.active_med == True:
        dificulty = 'medium'
    elif btn.active_hard == True:
        dificulty = 'hard'
    else:
        dificulty = 'medium'
    snake.game_settings(int(mn.text_width), int(mn.text_height), dificulty)
    snake.gameloop()

def mouse_click( event):
    if btn.width_box.collidepoint(event.pos):
        btn.active_width = True
        btn.active_height = False
    elif btn.height_box.collidepoint(event.pos):
        btn.active_width = False
        btn.active_height = True
    elif btn.box_easy.collidepoint(event.pos):
        btn.active_easy = True
        btn.active_med = False
        btn.active_hard = False
        btn.active_width = False
        btn.active_height = False
    elif btn.box_med.collidepoint(event.pos):
        btn.active_easy = False
        btn.active_med = True
        btn.active_hard = False
        btn.active_width = False
        btn.active_height = False
    elif btn.box_hard.collidepoint(event.pos):
        btn.active_easy = False
        btn.active_med = False
        btn.active_hard = True
        btn.active_width = False
        btn.active_height = False
    elif btn.Start_box.collidepoint(event.pos):
        mn.done = True
        pg.quit()
        start_game()
    elif btn.Quit_box.collidepoint(event.pos):
        mn.done = True
    else:
        btn.active_width = False
        btn.active_height = False

def buttons_text(event):
    if btn.active_width:
        if event.key == pg.K_RETURN:
            mn.text_width = ''    
        elif event.key == pg.K_BACKSPACE:
            mn.text_width = mn.text_width[:-1]
        else:
            mn.text_width += event.unicode
    if btn.active_height:
        if event.key == pg.K_RETURN:
            mn.text_height = ''
        elif event.key == pg.K_BACKSPACE:
            mn.text_height = mn.text_height[:-1]
        else:
            mn.text_height += event.unicode

def render_text():
    txt_width = mn.font.render(mn.text_width, True, btn.color_width)
    txt_height = mn.font.render(mn.text_height, True, btn.color_height)
    txt_easy = mn.font.render('easy', True, btn.color_inactive)
    txt_med = mn.font.render('medium', True, btn.color_inactive)
    txt_hard = mn.font.render('hard', True, btn.color_inactive)
    txt_Start = mn.font.render('START', True, btn.color_inactive)
    txt_Quit = mn.font.render(' QUIT', True, btn.color_inactive)
    # Blit the text.
    mn.screen.blit(txt_width, (btn.width_box.x+5, btn.width_box.y+5))
    mn.screen.blit(txt_height, (btn.height_box.x+5, btn.height_box.y+5))
    mn.screen.blit(txt_easy, (btn.box_easy.x+5, btn.box_easy.y+5))
    mn.screen.blit(txt_med, (btn.box_med.x+5, btn.box_med.y+5))
    mn.screen.blit(txt_hard, (btn.box_hard.x+5, btn.box_hard.y+5))
    mn.screen.blit(txt_Start, (btn.Start_box.x+5, btn.Start_box.y+5))
    mn.screen.blit(txt_Quit, (btn.Quit_box.x+5, btn.Quit_box.y+5))

def render_button():
    pg.draw.rect(mn.screen, btn.color_width, btn.width_box, 2)
    pg.draw.rect(mn.screen, btn.color_height, btn.height_box, 2)
    pg.draw.rect(mn.screen, btn.color_easy, btn.box_easy, 2)
    pg.draw.rect(mn.screen, btn.color_med, btn.box_med, 2)
    pg.draw.rect(mn.screen, btn.color_hard, btn.box_hard, 2)
    pg.draw.rect(mn.screen, btn.color_inactive, btn.Start_box, 2)
    pg.draw.rect(mn.screen, btn.color_inactive, btn.Quit_box, 2)

def render_info():
    snake.render_text_and_position('Hello world!', mn.font, (255, 255, 255), mn.screen, 300, 20)
    snake.render_text_and_position('Choose resolution:', mn.font, (255, 255, 255), mn.screen, 150, 135)
    snake.render_text_and_position('x', mn.font, btn.color_inactive, mn.screen, 408, 135)
    snake.render_text_and_position('Choose difficulty:', mn.font, (255, 255, 255), mn.screen, 150, 200)
    snake.render_text_and_position('Hello world!', mn.font, (255, 255, 255), mn.screen, 300, 20)

def main():
    while not mn.done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                mn.done = True
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                mouse_click(event)    
                # Change the current color of the input box.
                btn.color_width = btn.color_active if btn.active_width else btn.color_inactive
                btn.color_height = btn.color_active if btn.active_height else btn.color_inactive                
                btn.color_easy = btn.color_active if btn.active_easy else btn.color_inactive
                btn.color_med = btn.color_active if btn.active_med else btn.color_inactive
                btn.color_hard = btn.color_active if btn.active_hard else btn.color_inactive
            elif event.type == pg.KEYDOWN:
                buttons_text(event)
                
        mn.screen.fill((30, 30, 30))
        render_text()
        # Blit the input_box rect.
        render_button()
        render_info()

        pg.display.flip()
        mn.clock.tick(30)


if __name__ == '__main__':
    main()
    
