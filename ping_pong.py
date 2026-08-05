from pygame import *
mixer.init()
font.init()
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
        #draw.rect(window, (255,255,255), self.rect, 3)

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
class Mach(Igroc):
    def __init__(self, x, y, width, height, skorost, filename):
        super().__init__(x, y, width, height, skorost, filename)
        self.skorost_x = self.skorost
        self.skorost_y = self.skorost
    def update(self):
        self.rect.y += self.skorost_y
        self.rect.x += self.skorost_x
        if self.rect.bottom >= win_h:
            self.skorost_y = (-1) * abs(self.skorost_y)
        elif self.rect.y <= 0:
            self.skorost_y = abs(self.skorost_y)
win_w = 1200
win_h = 800
window = display.set_mode((win_w, win_h))#создание окна игры
background = transform.scale(image.load(poisk_kart("galaxy.jpg")), (win_w, win_h))

raketka = Raketa(100, 310, 104, 154, 4, "image.png")
raketka2 = Raketa(900, 310, 104, 154, 4, "image.png")
mach  = Mach(510, 370, 120, 80, 3, "ufo.png")

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
        mach.update()
        if sprite.collide_rect(mach, raketka):
            mach.skorost_x = +1 * abs(mach.skorost_x)
        if sprite.collide_rect(mach, raketka2):
            mach.skorost_x = -1 * abs(mach.skorost_x)
        window.blit(background, (0, 0))
        raketka.reset(window)
        raketka2.reset(window)
        mach.reset(window)
        
        if mach.rect.left < 0:
            stop = True
            text_lose = font.SysFont('verdana', 70).render('выигрыш правого', True, (200, 50, 50))
            window.blit(text_lose, (140, 150))
        elif mach.rect.right > win_w:
            stop = True
            text_lose = font.SysFont('verdana', 70).render('выигрыш левого', True, (50, 200, 50))
            window.blit(text_lose, (140, 150))
#------------
    display.update()
    clock.tick(FPS)
quit()
