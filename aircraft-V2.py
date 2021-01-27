import pygame
from sys import exit   #向sys模块借一个exit函数用来退出程序
import os
import sys
import random

#pyinstaller打包路径获取
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

backjpg = resource_path(os.path.join("res","back.jpg"))


planepng = resource_path(os.path.join("res","plane.png"))
bulletpng = resource_path(os.path.join("res","bullet.png"))
enemypng = resource_path(os.path.join("res","enemy.png"))


pygame.init()  #初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((450, 700), 0, 32) #创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Hello world")   #设置窗口标题
#背景加载background
background=pygame.image.load(backjpg)


#封装子弹相关内容
class Bullet:
    def __init__(self):
        #初始化变量,x,y,image
        self.x=-1
        self.y=-1
        self.image=pygame.image.load(bulletpng).convert_alpha()
        self.active=False
    def move(self):
        if self.active:
            self.y -= 0.3           #子弹速度
        if self.y < 0:
            self.active=False
    def restart(self):
        mouse_x,mouse_y=pygame.mouse.get_pos()
        self.x=mouse_x-self.image.get_width()/2
        self.y=mouse_y-self.image.get_height()/2
        self.active=True
bullet=[]
#子弹总数
count_b=5
#创建子弹
for i in range(count_b):
    bullet.append(Bullet())
#即将激活子弹序号
index_b=0
#发射子弹间隔
in_b=500                 #发射子弹间隔
interval_b=0

#封装敌机
class Enemy:
    def __init__(self):
        self.image=pygame.image.load(enemypng).convert_alpha()
        self.restart()
    def move(self):
        if self.y<700:
            self.y += self.speed
        else:
            self.restart()
    def restart(self):
        self.x=random.randint(50,400)
        self.y=random.randint(-200,-50)
        self.speed=random.randrange(0,1)+0.1
enemy=[]
for i in range(5):
    enemy.append(Enemy())

#封装主机
class Plane():
    def __init__(self):
        self.restart()
        self.image=pygame.image.load(planepng)
    def restart(self):
        self.x=200
        self.y=600
    def move(self):
        x,y=pygame.mouse.get_pos()
        self.x = x - self.image.get_width() / 2
        self.y = y - self.image.get_height() / 2
plane=Plane()



#命中目标
def checkhit(en,bu):
    if (bu.x > en.x and bu.x < en.x+en.image.get_width()) and (bu.y > en.y and bu.y < en.y+en.image.get_height()):
        en.restart()
        bu.active = False
        return True
    return False

#GameOver判断
def checkcrash(en,pl):
    if ((pl.x + pl.image.get_width() * 0.3) > en.x and (pl.x + pl.image.get_width() * 0.7) < (en.x +en.image.get_width())) and ((pl.y + pl.image.get_height() * 0.3) > en.y and (pl.y + pl.image.get_height() * 0.7) < (en.y + en.image.get_height())):
        return True
    return False
gameover=False


#分数记录与绘制
score=0
font=pygame.font.SysFont('elephant',32)
overfont=pygame.font.SysFont('elephant',50)



while True:    #游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            exit()
        if gameover and event.type == pygame.MOUSEBUTTONUP:   #重置游戏
            gameover = False
            score=0
            plane.restart()
            for i in enemy:
                i.restart()
            for i in bullet:
                i.restart()
    screen.blit(background, (0, 0))  # 将背景图画上去

    if not gameover:
        #画子弹
        interval_b-=1
        if interval_b<0:
            bullet[index_b].restart()
            interval_b=in_b
            index_b=(index_b+1)%count_b
        for b in bullet:
            if b.active:
                for e in enemy:
                    if checkhit(e,b):
                        score += 100
                b.move()
                screen.blit(b.image,(b.x,b.y))

        # 画敌机
        for e in enemy:
            if checkcrash(e, plane):
                gameover = True
            e.move()
            screen.blit(e.image, (e.x, e.y))

        #画飞机
        plane.move()
        screen.blit(plane.image,(plane.x,plane.y))

        #画分数
        text=font.render("Score: %d" % score, 1, (0,0,0))
        screen.blit(text,(0,0))


    else:
        text1=overfont.render("GAME OVER",1,(0,0,0))
        text2=overfont.render("Score: %d" %score,1,(0,0,0))
        screen.blit(text1,(50,300))
        screen.blit(text2, (80, 360))
        pass

    # 刷新一下画面
    pygame.display.update()





