import pygame as pg
import random

class Enemy:
    enemyIcon = []
    enemyXcoord = []
    enemyYcoord = []
    enemySpeedChange = []
    enemyHightChange = []
    numOfEnemies = 6

    def enemyCreation(self):
        for i in range(self.numOfEnemies):
            if (i % 2 == 0):
                self.enemyIcon.append(pg.image.load('images/enemy1.png'))
            else:
                self.enemyIcon.append(pg.image.load('images/enemy2.png'))
            self.enemyXcoord.append(random.randint(0, 800))
            self.enemyYcoord.append(random.randint(50, 100))
            self.enemySpeedChange.append(0.3)
            self.enemyHightChange.append(40)

    def enemy(self, enemyX, enemyY, i, window):
        window.blit(self.enemyIcon[i], (enemyX, enemyY))

    def enemyMove(self, game, bullet, window):

        for i in range(self.numOfEnemies):
            self.enemyXcoord[i] += self.enemySpeedChange[i]
            if self.enemyXcoord[i] <= 0:
                self.enemySpeedChange[i] = 0.3
                self.enemyYcoord[i] += self.enemyHightChange[i]
            elif self.enemyXcoord[i] >= 740:
                self.enemySpeedChange[i] = -0.3
                self.enemyYcoord[i] += self.enemyHightChange[i]
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)

            isCollision = game.collision(self.enemyXcoord[i], self.enemyYcoord[i], bullet.get_bulletXcoord(),
                                         bullet.get_bulletYcoord())
            if isCollision:
                bullet.set_bulletYcoord(470)
                bullet.set_bulletIsReady("Ready")
                game.set_score(10)
                self.enemyYcoord[i] = 2000
                game.set_counterEnemy(1)
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)
            if game.get_counterEnemy() == self.numOfEnemies:
                game.end_game_win(window)
                break
            if self.enemyYcoord[i] > 400 and self.enemyYcoord[i] < 1900:
                for j in range(self.numOfEnemies):
                    self.enemyYcoord[j] = 1500
                game.end_game_lose(window)
                break
