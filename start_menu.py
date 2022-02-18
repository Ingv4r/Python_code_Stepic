from turtle import Screen
import pygame as pg


text = '600'
text2 = '400'
screen = pg.display.set_mode((int(text), int(text2)))


def render_text_and_position(text, font, color, width = 0, height = 0): 
    message = font.render(text, True, color)
    position = [0, 0]
    if width != 0 and height != 0:
        position = message.get_rect(center = (width, height))
    screen.blit(message, position)

def m():
    global text, text2, screen
    font = pg.font.Font(None, 30)
    clock = pg.time.Clock()
    res_boxX = pg.Rect(330, 120, 58, 30)
    res_boxY = pg.Rect(430, 120, 58, 30)
    diff_box_easy = pg.Rect(300, 180, 55, 30)
    diff_box_med = pg.Rect(380, 180, 85, 30)
    diff_box_hard = pg.Rect(485, 180, 57, 30)
    Start_box = pg.Rect(200, 290, 75, 30)
    Quit_box = pg.Rect(330, 290, 75, 30)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    color4 = color_inactive
    color5 = color_inactive
    color6 = color_inactive
    color7 = color_inactive
    active = False
    active2 = False
    active3 = False
    active4 = False
    active5 = False
    active6 = False
    active7 = False

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if res_boxX.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    active2 = False
                elif res_boxY.collidepoint(event.pos):
                    # Toggle the active variable.
                    active2 = not active2
                    active = False
                elif diff_box_easy.collidepoint(event.pos):
                    active3 = True
                    active4 = False
                    active5 = False
                elif diff_box_med.collidepoint(event.pos):
                    active4 = True
                    active3 = False
                    active5 = False
                elif diff_box_hard.collidepoint(event.pos):
                    active5 = True
                    active3 = False
                    active4 = False
                elif Start_box.collidepoint(event.pos):
                    import snake
                    
                    done = True
                elif Quit_box.collidepoint(event.pos):
                    done = True
                else:
                    active = False
                    active2 = False
                    
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

        render_text_and_position('Hello world!', font, (255, 255, 255), 300, 20)
        render_text_and_position('Choose resolution:', font, (255, 255, 255), 150, 135)
        render_text_and_position('x', font, color_inactive, 408, 135)
        render_text_and_position('Choose difficulty:', font, (255, 255, 255), 150, 200)
        render_text_and_position('Hello world!', font, (255, 255, 255), 300, 20)
        

        pg.display.flip()
        clock.tick(30)


pg.init()
m()
pg.quit()
