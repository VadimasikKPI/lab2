import pygame as pg
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Settings import Game
from Asteroid import Asteroid

pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption("Space Invaders")
icon = pg.image.load('images/Caption.png')
pg.display.set_icon(icon)
background = pg.image.load('images/space2.png')
player = Player()
enemy = Enemy()
bullet = Bullet()
game = Game()
asteroid = Asteroid()

enemy.enemyCreation()
asteroid.asteroidCreation()

isClose = True
while isClose:
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isClose = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                player.set_playerSpeedChange(0.7)
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                player.set_playerSpeedChange(-0.7)
            if event.key == pg.K_SPACE:
                if bullet.get_bulletIsReady() == "Ready":
                    bullet.set_bulletXcoord(player.get_playerXcoord())
                    bullet.bullet(bullet.get_bulletXcoord(), bullet.get_bulletYcoord(), window)
                    bullet.changeYcoord(-bullet.get_bulletHightChange())
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_d or event.key == pg.K_a:

                player.set_playerSpeedChange(0)

    player.set_playerXcoord(player.get_playerSpeedChange())
    if bullet.get_bulletIsReady() == "Not ready":
        bullet.bullet(bullet.get_bulletXcoord(), bullet.get_bulletYcoord(), window)
        bullet.changeYcoord(-bullet.get_bulletHightChange())

    if bullet.get_bulletYcoord() <= 0:
        bullet.set_bulletIsReady("Ready")
        bullet.set_bulletYcoord(470)
    enemy.enemyMove(game, bullet, window)
    asteroid.lifeCicleAsteroid(bullet, game, window)
    #enemy.get_positionEnemy()



    player.player(player.get_playerXcoord(), player.get_playerYcoord(), window)
    game.showScore(10, 10, window)
    pg.display.update()

