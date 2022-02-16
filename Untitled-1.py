import pygame as pg


def m():
    screen = pg.display.set_mode((600, 400))
    font = pg.font.Font(None, 30)
    clock = pg.time.Clock()
    input_box = pg.Rect(330, 140, 200, 30)
    input_box2 = pg.Rect(330, 230, 200, 30)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    color2 = color_inactive
    active = False
    active2 = False
    text = '600*400'
    text2 = 'easy'
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    active2 = False
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active2 = not active2
                    active = False
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                color2 = color_active if active2 else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                        import snake
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
        txt_surface = font.render(text, True, color)
        txt_surface2 = font.render(text2, True, color2)
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        pg.draw.rect(screen, color2, input_box2, 2)

        pg.display.flip()
        clock.tick(30)


pg.init()
m()
pg.quit()