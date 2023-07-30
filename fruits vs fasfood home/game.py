from pygame import *

windows = display.set_mod(700,500)
display.set_captoin('ftuits vs fasfood')
background = trasform.scale(image.load('kitchen.png'),(700,500))


class GameSprite():
    def __init__ (self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        #self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_A] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_D] and self.rect.y < 450:
            self.rect.y += 10
player = Player('man.jpg',0,500)
#fruits = GameSprite('banane.jpg',700,0)
#fasfood = GameSprite('fasfood.jpg',700,0)
game = True
while game:
    windows.blit(background,(0,0))

    for e in event:
        if e.type == QUIT
            game = False


    display.update()