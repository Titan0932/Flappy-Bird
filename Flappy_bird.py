
import pygame
from settings import Settings
from bird import Bird
import game_functions as gf
import pipes

pygame.init()
clock=pygame.time.Clock()
def main():
    settings=Settings()
    screen=pygame.display.set_mode((settings.width,settings.height))
    screen.fill((settings.bgcolor))
    bird=Bird(screen,settings)
    
    

    
    gf.disp_score(bird,screen,settings)
    pipe=[ [pipes.top_pipe(screen,settings.center_pos),pipes.bottom_pipe(screen,settings.center_pos)]]
    
    gf.update_screen(screen,settings,bird,pipe)
    gf.start_message(screen,bird)
    while True:
        gf.check_events(bird,screen,settings,pipe)
        if bird.started==True:
            gf.check_events(bird,screen,settings,pipe)
            gf.update_screen(screen,settings,bird,pipe)
            if bird.collision==True:          
                bird.started=False
                gf.update_screen(screen,settings,bird,pipe)
                gf.lose_message(screen,bird)
                if bird.score>int(bird.highscore): 
                    bird.highscore=bird.score
                    with open('highscore.txt','w') as file_val:
                        file_val.write(str(bird.score))
                gf.start_message(screen,bird)

        clock.tick(300)     
            


main()

