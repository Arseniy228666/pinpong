from pygame import *

class GameSprite(sprite.Sprite):#класс
    def __init__(self, image_sprite, img_x, img_y, speed, hight, width):#ввод значений 
        super().__init__()##указывает на себя всё из класса родителя
        self.image = transform.scale(image.load(image_sprite), (65,65))#указывает на себя картинку
        self.speed = speed#указывает на себя скорость
        self.rect = self.image.get_rect()#указывает на себя
        self.rect.x = img_x#указывает на себя х
        self.rect.y = img_y#указывает на себя у

    def show_s(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left_player(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<win_hight-80:
            self.rect.y+=self.speed
    def update_right_player(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<win_hight-80:
            self.rect.y+=self.speed

back=(200,255,155)
win_hight=600
win_widht=650
window=display.set_mode((win_widht, win_hight))
window.fill(back)

player1=Player('dosk.png',30,200,4,50,150)
player2=Player('dosk.png', 520,200,4,50,150)

ball=GameSprite('boll.png', 200,200,4,50,50)

font.init()
font=font.Font(None, 35)
lose1=font.render('PLAYER 1 LOSE', True, (180,0,0))
lose2=font.render('PLAYER 2 LOSE', True, (180,0,0))

speed_x=3
speed_y=3

game=True
finish=False
clock=time.Clock()

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
        
    if finish !=True:
        window.fill(back)
        player1.update_left_player()
        player2.update_right_player()

        ball.rect.x+=speed_x
        ball.rect.y+=speed_y

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x*=-1
            speed_y*=1

        if ball.rect.y>win_hight-50 or ball.rect.y<0:
            speed_y *=-1

        if ball.rect.x<0:
            finish=True
            window.blit(lose1,(200,200))
            game_over=True

        if ball.rect.x>win_widht:
            finish=True
            window.blit(lose2,(200,200))
            game_over=True

        player1.show_s()
        player2.show_s()
        ball.show_s()




    display.update()
    clock.tick(60)