import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")

    tori = pg.image.load("fig/3.png")
    tori=pg.transform.flip(tori, True, False)
    bg_img2=pg.transform.flip(bg_img, True, False)


    tori_move1=pg.transform.rotozoom(tori,2,1.0)
    tori_move2=pg.transform.rotozoom(tori,4,1.0)
    tori_move3=pg.transform.rotozoom(tori,6,1.0)
    tori_move4=pg.transform.rotozoom(tori,8,1.0)
    tori_move5=pg.transform.rotozoom(tori,10,1.0)
    tori_move6=pg.transform.rotozoom(tori,8,1.0)
    tori_move7=pg.transform.rotozoom(tori,6,1.0)
    tori_move8=pg.transform.rotozoom(tori,4,1.0)
    tori_move9=pg.transform.rotozoom(tori,2,1.0)
    tori_move10=pg.transform.rotozoom(tori,0,1.0)

    tories=[tori,tori_move1,tori_move2,tori_move3,tori_move4,tori_move5,tori_move6,tori_move7,tori_move8,tori_move9,tori_move10]
    
    tmr = 0
    cut=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [-cut, 0])
        screen.blit(bg_img, [3200-cut, 0])
        screen.blit(bg_img2,[1600-cut,0])
        screen.blit(tories[tmr%11],[300,200])
        pg.display.update()
        tmr += 1
        cut+=1

        if cut%3200 ==0:
            cut=0
     
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()