import random

import pygame as pg
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Settings import Game
from Asteroid import Asteroid
from DrawPath import *
import time
from WriterCSV import csv_write
from A_star import *
#from algoritms import bfs, dfs
from graph import graph
game_end_count=0

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
tempBFS = False
tempDFS = False
tempUCS = False
lines = pg.image.load('line.png')
asteroid.asteroidCreation()

start_time = time.time()



isClose = True
while isClose:
    window.fill((0, 0, 0))
    window.blit(background, (0,0))
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
            #if event.key == pg.K_z:
                #tempBFS = True
                #tempDFS = False
                #tempUCS = False
            #if event.key == pg.K_x:
                #tempUCS = True
                #tempBFS = False
                #tempDFS = False
            #if event.key == pg.K_c:
                #tempDFS = True
                #tempBFS = False
                #tempUCS = False
           # if event.key == pg.K_f:
                #tempBFS = False
                #tempDFS = False
                #tempUCS = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_d or event.key == pg.K_a:
                player.set_playerSpeedChange(0)

    player.set_playerXcoord(player.get_playerSpeedChange())
    if bullet.get_bulletIsReady() == "Not ready":
        bullet.bullet(bullet.get_bulletXcoord(), bullet.get_bulletYcoord(), window)
        bullet.changeYcoord(-bullet.get_bulletHightChange())
    player.outOfBounds()
    if bullet.get_bulletYcoord() <= 10:
        bullet.set_bulletIsReady("Ready")
        bullet.set_bulletYcoord(470)
    enemy.thirdEnemyMove(game, bullet, window, asteroid, player)
    asteroid.lifeCicleAsteroid(bullet, game, window, enemy)
    if enemy.get_numOfEnemy() == 0:
        game.end_game_win(window)
        temp = False
    asteroid_coord = game.find_asteroid_coords(asteroid)
    #if tempBFS:
        #drawPath_bfs(window, enemy, graph, player, asteroid_coord)
    #if tempDFS:
        #drawPath_dfs(window, enemy, graph, player, asteroid_coord)
    #if tempUCS:
        #drawPath_ucs(window, enemy, graph, player, asteroid_coord)
    if enemy.get_numOfEnemy()>0:
        drawPath_Astar(window, enemy, graph, player, bullet)
    else:
        game_end_count +=1
        game.end_game_win(window)
        player.playerSpeedChange = 0
        if game_end_count == 1:
            last_time = time.time() - start_time
            rand = random.choice(['expectimax minimax', 'alpha-beta pruning'])
            print(rand)
            csv_write('data.csv', [str(game.score), str(last_time), str('True'), str(rand)])




    player.player(player.get_playerXcoord(), player.get_playerYcoord(), window)
    game.showScore(10, 10, window)
    pg.display.update()

