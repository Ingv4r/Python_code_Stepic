import pygame as pg
import snake

pg.init()
pg.display.set_caption("Igor's first snake game v1.5")

class SnakeMenu():
    def __init__(self):
        self.text_width = '600'
        self.text_height = '400'
        self.screen = pg.display.set_mode((int(text), int(text2)))
        self.font = pg.font.Font(None, 30)
        self.clock = pg.time.Clock()
        self.resolution_width = pg.Rect(330, 120, 58, 30)
        self.resolution_height = pg.Rect(430, 120, 58, 30)
        self.difficulty_box_easy = pg.Rect(300, 180, 55, 30)
        self.difficulty_box_med = pg.Rect(380, 180, 85, 30)
        self.difficulty_box_hard = pg.Rect(485, 180, 57, 30)
        self.Start_box = pg.Rect(200, 290, 75, 30)
        self.Quit_box = pg.Rect(330, 290, 75, 30)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.active_width = False
        self.active_height= False
        self.active_easy = False
        self.active_med = False
        self.active_hard = False
        self.done = False


    def start_game(self):
        self.done = True
        if self.active_easy == True:
            dificulty = 'easy'
        elif self.active_med == True:
            dificulty = 'medium'
        elif self.active_hard == True:
            dificulty = 'hard'
        snake.game_settings(int(self.text_width), int(self.text_height), dificulty)
        snake.gameloop()

    def mouse_click(self, event):
        if self.resolution_width.collidepoint(event.pos):
            self.active_width = True
            self.active_height = False
        elif self.resolution_height.collidepoint(event.pos):
            self.active_width = False
            self.active_height = True
        elif self.difficulty_box_easy.collidepoint(event.pos):
            self.active_easy = True
            self.active_med = False
            self.active_hard = False
            self.active_width = False
            self.active_height = False
        elif self.difficulty_box_med.collidepoint(event.pos):
            self.active_easy = False
            self.active_med = True
            self.active_hard = False
            self.active_width = False
            self.active_height = False
        elif self.difficulty_box_hard.collidepoint(event.pos):
            self.active_easy = False
            self.active_med = False
            self.active_hard = True
            self.active_width = False
            self.active_height = False
        elif self.Start_box.collidepoint(event.pos):
            self.start_game()
        elif self.Quit_box.collidepoint(event.pos):
            self.done = True
        else:
            self.active_width = False
            self.active_height = False


    def menu(self):
        while not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    self.mouse_click(event)
                  
                        
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    color2 = color_active if active2 else color_inactive
                    color3 = color_active if active3 else color_inactive
                    color4 = color_active if active4 else color_inactive
                    color5 = color_active if active5 else color_inactive
        
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            print(text)
                            text = ''
                            
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pg.K_RETURN:
                            print(text2)
                            text2 = ''
                        elif event.key == pg.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                

            screen.fill((30, 30, 30))
            # Render the current text.
            txt_resX = font.render(text, True, color)
            txt_resY = font.render(text2, True, color2)
            txt_easy = font.render('easy', True, color_inactive)
            txt_med = font.render('medium', True, color_inactive)
            txt_hard = font.render('hard', True, color_inactive)
            txt_Start = font.render('START', True, color_inactive)
            txt_Quit = font.render(' QUIT', True, color_inactive)
            # Blit the text.
            screen.blit(txt_resX, (res_boxX.x+5, res_boxX.y+5))
            screen.blit(txt_resY, (res_boxY.x+5, res_boxY.y+5))
            screen.blit(txt_easy, (diff_box_easy.x+5, diff_box_easy.y+5))
            screen.blit(txt_med, (diff_box_med.x+5, diff_box_med.y+5))
            screen.blit(txt_hard, (diff_box_hard.x+5, diff_box_hard.y+5))
            screen.blit(txt_Start, (Start_box.x+5, Start_box.y+5))
            screen.blit(txt_Quit, (Quit_box.x+5, Quit_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(screen, color, res_boxX, 2)
            pg.draw.rect(screen, color2, res_boxY, 2)
            pg.draw.rect(screen, color3, diff_box_easy, 2)
            pg.draw.rect(screen, color4, diff_box_med, 2)
            pg.draw.rect(screen, color5, diff_box_hard, 2)
            pg.draw.rect(screen, color_inactive, Start_box, 2)
            pg.draw.rect(screen, color_inactive, Quit_box, 2)

            snake.render_text_and_position('Hello world!', font, (255, 255, 255), screen, 300, 20)
            snake.render_text_and_position('Choose resolution:', font, (255, 255, 255), screen, 150, 135)
            snake.render_text_and_position('x', font, color_inactive, screen, 408, 135)
            snake.render_text_and_position('Choose difficulty:', font, (255, 255, 255), screen, 150, 200)
            snake.render_text_and_position('Hello world!', font, (255, 255, 255), screen, 300, 20)
            

            pg.display.flip()
            clock.tick(30)


if __name__ == '__main__':
    m = SnakeMenu()
    m.menu()
