import pygame as pg
from time import sleep
pg.init()
screen_size=[360,600]
screen=pg.display.set_mode(screen_size)
bg=pg.image.load('bg.png')
ss=pg.image.load('space-ship.png')
bullet=pg.image.load('bullet.png')
bullet_y=800
fired=False
planets=['p_one.png','p_two.png']
p_index=0
win=pg.image.load('win.png')
planet=pg.image.load(planets[p_index])
planet_x=280
direction='right'
keep_alive=True
clock=pg.time.Clock()
while keep_alive:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            quit()
        if event.type==pg.MOUSEMOTION:
            fired=True
    if fired is True:
        bullet_y=bullet_y-10
        if bullet_y==50:
            fired=False
            bullet_y=700
    if planet_x<=0:
        planet_x+=5
        direction='right'
    elif not(planet_x>540):
        if direction=='right':
            planet_x+=5
        elif direction=='left':
            planet_x-=5
    
    else:
        direction='left'
        if not(planet_x<0):
            planet_x-=5
        else:
            direction='right'
    screen.blit(bg,[0,0])
    screen.blit(bullet,[270,bullet_y])
    screen.blit(ss,[279,800])
    screen.blit(planet,[planet_x,50])
    if bullet_y<=120 and planet_x>=240 and planet_x<=300:
        bullet_y=700
        fired=False
        p_index+=1
        if p_index<len(planets):
            planet=pg.image.load(planets[p_index])
            planet_x=280
        else:
            screen.blit(win,[0,100])
            sleep(5)
            keep_alive=False
    pg.display.update()
    clock.tick(60)
pg.quit()
quit()