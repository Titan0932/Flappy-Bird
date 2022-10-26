
import pygame



class top_pipe():
    def __init__(self,screen,center_pos):
        self.image=pygame.image.load('top_pipe.bmp').convert()
        self.screen=screen
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.bottom=center_pos-90
        self.rect.left=self.screen_rect.right
        self.center=float(self.rect.centerx)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)

class bottom_pipe():
    def __init__(self,screen,center_pos):
        self.image=pygame.image.load('bottom_pipe.bmp').convert()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect=self.image.get_rect()
        self.rect.top=center_pos+90
        self.rect.left=self.screen_rect.right
        self.center=float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image,self.rect)


def display_pipes(t_pipe,b_pipe):
    t_pipe.blitme()
    b_pipe.blitme()


def remove_extra(top,bot,pipe):
    if (top.rect.right==0 and bot.rect.right==0):
        pipe.remove([top,bot])
    


def pipe_move(top,bot,settings):
    if top.rect.right>0 and bot.rect.right>0:
        top.center-=settings.pipe_speed
        bot.center-=settings.pipe_speed
        top.rect.centerx=top.center
        bot.rect.centerx=bot.center
    
    



        