import pygame


with open('highscore.txt','r') as file_val:
    h_score= file_val.readline()




class Bird():
    def __init__(self,screen,settings):
        self.screen=screen
        self.settings=settings
        self.image=pygame.image.load('images\smol_bird.bmp').convert_alpha()
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centery=self.screen_rect.centery
        self.rect.centerx=self.screen_rect.centerx
        self.up=False
        self.center=float(self.rect.centery)
        self.collision=False
        self.score=0
        self.started=False
        self.highscore=h_score

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def movement(self,settings):
        if self.rect.centery<self.screen_rect.bottom:
            self.center+=settings.gravity
        if self.up==True and self.rect.centery>0:
            self.center-=settings.lift
        self.rect.centery=self.center
        self.up=False
