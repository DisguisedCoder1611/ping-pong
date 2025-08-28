from pygame import *

w = 600
h = 500

win = display.set_mode((w, h))
display.set_caption('sepak bola tapi gak pake kaki dan pake tongkat')

background_color = (255, 0, 0)
win.fill(background_color)
game = True

class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # every sprite must have the rect property that represents the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # method drawing the character on the window
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


# main player class
class Player(GameSprite):
    # method to control the sprite with arrow keys
    def move_p1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < h - 80:
            self.rect.y += self.speed
    
    def move_p2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < h - 80:
            self.rect.y += self.speed

p1 = Player('racket.png', 30, 200, 30, 100, 5)
p2 = Player('racket.png', 520, 200, 30, 100, 5)
ball = GameSprite('tenis_ball.png', 250, 300, 50, 50, 5)
clock = time.Clock()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.fill(background_color)
    p1.move_p1()
    p2.move_p2()
    p1.reset()
    p2.reset()
    ball.reset()
    display.update()
    clock.tick(60)
