from pygame import *

w = 600
h = 500

win = display.set_mode((w, h))
display.set_caption('sepak bola tapi gak pake kaki dan pake tongkat')

background_color = (255, 0, 0)
win.fill(background_color)
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game == False
    win.fill(background_color)
    display.update()
