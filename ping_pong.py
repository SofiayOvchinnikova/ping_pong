from pygame import *
mixer.init()
import random
import os
import sys

def poisk_kart(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Igroc(sprite.Sprite):
    def __init__(self, x, y, width, height, skorost, filename):
        super().__init__()
        self.image = transform.scale(image.load(poisk_kart(filename)), (width, height))
        self.rect = self.image.get_rect()#Находится прямоугольник картинка
        self.skorost = skorost
        self.rect.x = x
        self.rect.y = y
    def reset(self, window):#отрисовывает игроя в точке
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (0,0,0), self.rect, 3)

class Raketa(Igroc):
    def update_r(self): # проверяет куда идти
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.skorost
        elif keys_pressed[K_DOWN] and self.rect.bottom < 800:
            self.rect.y += self.skorost 
    def update_l(self): # проверяет куда идти
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.skorost
        elif keys_pressed[K_s] and self.rect.bottom < 800:
            self.rect.y += self.skorost

win_w = 1200
win_h = 800
window = display.set_mode((win_w, win_h))#создание окна игры
background = transform.scale(image.load(poisk_kart("galaxy.jpg")), (win_w, win_h))

raketka = Raketa(100, 310, 150, 280, 4, "racketka.png")
raketka2 = Raketa(900, 310, 150, 280, 4, "racketka.png")
mach  = Raketa(510, 370, 120, 80, 4, "ufo.png")

vragi = sprite.Group()

mixer.music.load(poisk_kart("space.ogg"))
mixer.music.set_volume(0.1)
#mixer.music.play()
display.set_caption("Пинг-Понг")
clock = time.Clock()
FPS = 60
game = True
stop = False


#-------
while game:#игра идет

    for e in event.get():#все возм события
        if e.type == QUIT:#выход нажал на крест
            game = False
        
    if not stop:
        raketka.update_l()
        raketka2.update_r()
        window.blit(background, (0, 0))
        raketka.reset(window)
        raketka2.reset(window)
        mach.reset(window)
            #------------

    display.update()
    clock.tick(FPS)
quit()
