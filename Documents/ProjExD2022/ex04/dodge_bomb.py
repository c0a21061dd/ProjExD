import pygame as pg
import random
import sys
import tkinter as tk
import tkinter.messagebox as tkm

def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.png")
    pgbg_rct = pgbg_sfc.get_rect()
    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 
    # 練習５
    bomb_sfc = pg.Surface((30, 30)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (15, 15), 15)
    pg.draw.circle(bomb_sfc, (191, 0, 0), (15, 15), 12)
    pg.draw.circle(bomb_sfc, (127, 0, 0), (15, 15), 9)
    pg.draw.circle(bomb_sfc, (63, 0, 0), (15, 15), 6)
    pg.draw.circle(bomb_sfc, (0, 0, 0), (15, 15), 3)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0+1, scrn_rct.width-1)
    bomb_rct.centery = random.randint(0+1, scrn_rct.height-1)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 

    bomb_sfc_1 = pg.Surface((30, 30)) # 正方形の空のSurface
    bomb_sfc_1.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc_1, (255, 0, 0), (15, 15), 15)
    pg.draw.circle(bomb_sfc_1, (191, 0, 0), (15, 15), 12)
    pg.draw.circle(bomb_sfc_1, (127, 0, 0), (15, 15), 9)
    pg.draw.circle(bomb_sfc_1, (63, 0, 0), (15, 15), 6)
    pg.draw.circle(bomb_sfc_1, (0, 0, 0), (15, 15), 3)
    bomb_rct_1 = bomb_sfc_1.get_rect()
    bomb_rct_1.centerx = random.randint(0+30, scrn_rct.width-30)
    bomb_rct_1.centery = random.randint(0+30, scrn_rct.height-30)
    scrn_sfc.blit(bomb_sfc_1, bomb_rct_1) 

    vx, vy = +1, +1
    vx_1, vy_1 = +1.7, +2
    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        elif key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        elif key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        elif key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1

        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            elif key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            elif key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            elif key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) 
        # 練習６
        bomb_rct_1.move_ip(vx_1, vy_1)
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        scrn_sfc.blit(bomb_sfc_1, bomb_rct_1)
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        yoko, tate = check_bound(bomb_rct_1, scrn_rct)
        vx_1 *= yoko
        vy_1 *= tate

        # 練習８
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb_rct_1):
            root = tk.Tk()
            root.withdraw()
            tkm.showinfo("失敗", "GAME OVER")
            return    

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()