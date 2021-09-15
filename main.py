import pygame as pg
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Settings import Game
from Asteroid import Asteroid
from algoritms import bfs, dfs
from graph import graph

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
algoCounter = 0
enemy.enemyCreation()
path = []
enemyCoords = []
#asteroid.asteroidCreation()


isClose = True
while isClose:
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isClose = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                player.set_playerSpeedChange(0.5)
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                player.set_playerSpeedChange(-0.5)
            if event.key == pg.K_SPACE:
                if bullet.get_bulletIsReady() == "Ready":
                    bullet.set_bulletXcoord(player.get_playerXcoord())
                    bullet.bullet(bullet.get_bulletXcoord(), bullet.get_bulletYcoord(), window)
                    bullet.changeYcoord(-bullet.get_bulletHightChange())
            if event.key == pg.K_z:
                algoCounter+=1
                if algoCounter == 1:
                    path = bfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy())
                    print(path)
                algoCounter = 0
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_d or event.key == pg.K_a:
                player.set_playerSpeedChange(0)

    player.set_playerXcoord(player.get_playerSpeedChange())
    if bullet.get_bulletIsReady() == "Not ready":
        bullet.bullet(bullet.get_bulletXcoord(), bullet.get_bulletYcoord(), window)
        bullet.changeYcoord(-bullet.get_bulletHightChange())
    player.outOfBounds()
    if bullet.get_bulletYcoord() <= 0:
        bullet.set_bulletIsReady("Ready")
        bullet.set_bulletYcoord(470)
    enemy.enemyMove(game, bullet, window)
    #asteroid.lifeCicleAsteroid(bullet, game, window)
    #enemy.get_positionEnemy()
    for i in range(enemy.get_numOfEnemy()):
        path.append(bfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(i)))





    player.player(player.get_playerXcoord(), player.get_playerYcoord(), window)
    game.showScore(10, 10, window)
    pg.display.update()

