from pygame import *

init()
# розміри вікна
W = 860
H = 680

window = display.set_mode((W, H))# створюємо вікно


display.set_caption("Labyrinth")
display.set_icon(image.load('scarb3.png'))

back = transform.scale(image.load('back1.png'), (W, H))# вписуємо картинку у вікно
clock = time.Clock()# створюємо лічильник кадрів
# підключення звуків
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.4)
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')


class GameSprite(sprite.Sprite):# базовий клас для спрайтів
    def __init__(self, player_img, player_x, player_y, speed):
        super().__init__()# викликаємо конструктор суперкласу
        self.image = transform.scale(image.load(player_img), (65, 65))# створюємо картинку
        self.rect = self.image.get_rect()# повертаємо прямокутник під картинкою
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
        
    def reset(self):# метод відображення картинки
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - 65:
            self.rect.y += self.speed
            
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < W - 65:
            self.rect.x += self.speed


class Enemy(GameSprite):
    direction = "right"
    
    def update(self, start, end):
        if self.rect.x >= end:
            self.direction = 'left'
            self.image = transform.scale(image.load('1.png'), (65, 65))
        if self.rect.x <= start:
            self.direction = 'right'
            self.image = transform.scale(image.load('1.png'), (65, 65))
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed
        
class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_w,wall_h,wall_x,wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width,self.height))
        self.image.fill((self.color1,self.color2,self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

hero = Player('hero2.png', 445, 5, 4)
enemy1 = Enemy('1.png', 480, 570, 2)
gold = GameSprite('scarb3.png', 475, 630, 0)

wall1 = Wall(43,0,255,400,20,20,20)
wall2 = Wall(43,0,255,20,640,20,20)
wall3 = Wall(43,0,255, 300,20, 540,20)
wall4 = Wall(43,0,255,20,640,830,20)
wall5 = Wall(43,0,255,270,20,560,640)
wall6 = Wall(43,0,255,420,20,20,640)
wall7 = Wall(43,0,255,480,20,280,118)
wall8 = Wall(43,0,255,20,230,160,40)
wall9 = Wall(43,0,255,20,250,280,120)
wall10 = Wall(43,0,255,450,20,381,220)
wall11 = Wall(43,0,255,20,100,470,220)
wall12= Wall(43,0,255,20,155,470,220)
wall13= Wall(43,0,255,550,20,200,450)
wall14= Wall(43,0,255,20,200,192,350)
wall15= Wall(43,0,255,200,20,192,540)
wall16= Wall(43,0,255,20,100,380,370)
wall17= Wall(43,0,255,50,20,160,130)
wall18= Wall(43,0,255,100,20,110,350)

game= True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back, (0, 0))
    hero.reset()
    hero.update()
    enemy1.reset()
    enemy1.update(300, 570)
    gold.reset()
    wall1.reset()
    wall2.reset()
    wall3.reset()
    wall4.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    wall8.reset()
    wall9.reset()
    wall10.reset()
    wall11.reset()
    wall12.reset()
    wall13.reset()
    wall14.reset()
    wall15.reset()
    wall16.reset()
    wall17.reset()
    wall18.reset()
    if sprite.collide_rect(hero,wall1) or sprite.collide_rect(hero,wall2) or sprite.collide_rect(hero,wall3) or sprite.collide_rect(hero,wall4) or sprite.collide_rect(hero,wall5) or sprite.collide_rect(hero,wall6) or sprite.collide_rect(hero,wall7) or sprite.collide_rect(hero,wall8) or sprite.collide_rect(hero,wall9) or sprite.collide_rect(hero,wall10) or sprite.collide_rect(hero,wall11) or sprite.collide_rect(hero,wall12) or sprite.collide_rect(hero,wall13) or sprite.collide_rect(hero,wall14) or sprite.collide_rect(hero,wall15) or sprite.collide_rect(hero,wall16) or sprite.collide_rect(hero,wall17) or sprite.collide_rect(hero,wall18) or sprite.collide_rect(hero,enemy1):
        hero.rect.x = 445
        hero.rect.y = 5
    if sprite.collide_rect(hero,gold):
       game = False
        
    display.update()
    clock.tick(60)

    