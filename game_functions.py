import pygame
import sys
import pipes
import random


pygame.init()
CREATEPIPE=pygame.USEREVENT
pygame.mixer.pre_init(frequency=44100,size=16,channels=1,buffer=512)
pygame.time.set_timer(CREATEPIPE,2000)


score_sound=pygame.mixer.Sound('score (2).wav')
dead_sound=pygame.mixer.Sound('died.wav')

def create_pipes(pipe,screen):
    

    center_pos=random.randint(110,600)
    top=pipes.top_pipe(screen,center_pos)
    bottom=pipes.bottom_pipe(screen,center_pos)
    pipe.append([top,bottom])


def check_events(bird,screen,settings,pipe):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type==CREATEPIPE:
            create_pipes(pipe,screen)

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                bird.started=True
                pipe.clear()
                bird.rect.centery=bird.screen_rect.centery
                bird.rect.centerx=bird.screen_rect.centerx
                bird.score=0
                bird.collision=False
                pipe=[[pipes.top_pipe(screen,settings.center_pos),pipes.bottom_pipe(screen,settings.center_pos)]]
                
            elif event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_UP:
                bird.up=True
            

def start_message(screen,bird):
    start=pygame.font.SysFont('AlternateGothic2 BT',50)
    ins=pygame.font.SysFont('AlternateGothic2 BT',30)
    text1=start.render("PRESS 'S' TO START.....",True,(232,50,200))
    text2=ins.render("Press up key to move",True,(232,50,250))
    h_score=pygame.font.SysFont('AlternateGothic2 BT',50)
    text3=h_score.render(f"Highscore: {bird.highscore}",True,(255,255,250))
    pos=screen.get_rect()
    screen.blit(text1,(pos.centerx-150,pos.centery+250))
    screen.blit(text2,(pos.centerx-100,pos.centery+290))
    screen.blit(text3,(pos.centerx-70,pos.centery-110))


    pygame.display.flip()




def pipe_operations(pipe,bird,settings,screen):
    for count in pipe:
        top=count[0]
        bot=count[1]
        
        pipes.pipe_move(top,bot,settings)
        calc_score(bird,top)
        disp_score(bird,screen,settings)
        detect_collision(top,bot,bird,settings)
        
        pipes.display_pipes(top,bot)
        pipes.remove_extra(top,bot,pipe)

    
def detect_collision(top,bot,bird,settings):
    if pygame.sprite.spritecollideany(bird, [top,bot]) or bird.rect.centery==settings.height:
        bird.collision=True
        dead_sound.play()

def lose_message(screen,bird):
    pygame.font.init()
    msg=pygame.font.SysFont('AlternateGothic2 BT',70)
    lose=msg.render("You DIED!!!",True,(252,0,0))
    screen.blit(lose,(bird.screen_rect.centerx-100,bird.screen_rect.centery-50))
    pygame.display.flip()

def calc_score(bird,top):
    if bird.rect.x==top.rect.right:
        bird.score+=1     
        score_sound.play() 
        
def disp_score(bird,screen,settings):
    pygame.font.init()
    text=pygame.font.SysFont('AlternateGothic2 BT',50)
    msg=text.render(f'Score:{bird.score}',False,(252,0,0))
    screen.blit(msg,(0,settings.height-50))

def update_screen(screen,settings,bird,pipe):
    screen.fill(settings.bgcolor)
    bird.movement(settings)
    bird.blitme()
    pipe_operations(pipe,bird,settings,screen)
    
        
        
       
    pygame.display.flip()
