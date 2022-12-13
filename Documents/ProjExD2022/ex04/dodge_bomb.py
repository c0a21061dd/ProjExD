import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    pgbg_sfc = pg.image.load("fig/pg_bg.png")
    pgbg_sfc = pg.transform.rotozoom(pgbg_sfc, 0, 2.0)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()