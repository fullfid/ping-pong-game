from pygame import *

back = (200,200,200)
win_width = 600
win_height = 500
display.set_caption("Ping - Pong")
window = display.set_mode((win_width, win_height))

font.init()
font = font.Font(None,35)
lose1 = font.render('1 Player LOSE',True, (200,0,0))
lose2 = font.render('2 Player LOSE', True, (200,0,0))

r_img = 'racket.png'
speed = 5
weight = 50
hight = 150
speed_x = 3
speed_y = 3
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - hight:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - hight:
            self.rect.y += self.speed
            



run = True 
finish = False
clock = time.Clock()
FPS = 60
racket1 = Player(r_img,30,200,weight,hight,speed)
racket2 = Player(r_img,520,200,weight,hight,speed)
ball = GameSprite("tenis_ball.png",200,200,50,50,speed)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.fill(back)
    racket1.update_l()
    racket2.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    racket1.reset()
    racket2.reset()
    ball.reset()
    
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1

    if ball.rect.x <0 :
        window.blit(lose1,(200,200))
        

    if ball.rect.x > win_width:
        window.blit(lose2,(200,200))



    display.update()
    clock.tick(FPS)
