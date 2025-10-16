import pygame
import random
from pygame import mixer
mixer.init()


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My game")
bg=pygame.image.load("Game_Background_190.png")
bg=pygame.transform.scale(bg,(500,500))
pygame. init()

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect() 
    def moveRight(self, pixels):
        self.rect.x+= pixels
    def moveLeft(self, pixels):
        self.rect.x-= pixels
    def moveForward(self, speed):
        self.rect.y-= speed*speed/10
    def moveBackward(self, speed):
        self.rect.y+=speed*speed/10

    
    



all_sprites_list = pygame.sprite.Group()
sp1 = Sprite("red", 50, 50)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,480)

all_sprites_list.add(sp1)

sp2 = Sprite("purple",50,50)
sp2.rect.x = random.randint(0,480)
sp2.rect.y = random.randint(0,480)
all_sprites_list.add(sp2)

rad = 20
exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        sp1.moveRight(5)
    if keys[pygame.K_UP]:
        sp1.moveForward(5)
    if keys[pygame.K_DOWN]:
        sp1.moveBackward(5)


    all_sprites_list.update()
    screen.blit(bg,(0,0))

    all_sprites_list.draw(screen)
    pygame.display.flip()

    if sp1.rect.colliderect(sp2.rect):
        all_sprites_list.remove(sp2)
        text = "Great Job"

        font = pygame.font.Font('freesansbold.ttf',32)
        text = font.render(text,True,"red")
        screen.blit(text,(200 - text.get_width() // 2, 140 - text.get_height() // 2))
    pygame.display.update()
    clock.tick(60)
pygame.quit()