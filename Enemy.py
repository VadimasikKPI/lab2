import pygame as pg
import random
import math


class Enemy:
    enemyIcon = []
    enemyNumber = []
    enemyXcoord = []
    enemyYcoord = []
    enemySpeedChange = []
    enemyHightChange = []
    numOfEnemies = 4
    numOfEnemiesforalgo = 4

    def enemyCreation(self):
        number = random.choice([1, 2, 3])
        for i in range(self.numOfEnemies):
            self.enemyNumber.append(i)
            if (i % 2 == 0):
                self.enemyIcon.append(pg.image.load('images/enemy1.png'))
            else:
                self.enemyIcon.append(pg.image.load('images/enemy2.png'))
                print(number)
            if number ==1:
                self.firstCreation(i)
            elif number == 2:
                self.secondCreation(i)
            elif number == 3:
                self.thirdCreation(i)

            # random.choice([self.firstCreation(i), self.secondCreation(i), self.thirdCreation(i)])
            # self.enemyXcoord.append(random.randint(90, 700))
            # self.enemyYcoord.append(random.randint(0, 100))

            self.enemySpeedChange.append(0)
            self.enemyHightChange.append(0.02)

    def enemy(self, enemyX, enemyY, i, window):
        window.blit(self.enemyIcon[i], (enemyX, enemyY))

    def get_positionEnemy(self, i):
        if self.enemyXcoord[i] <= 800 and self.enemyYcoord[i] <= 512:
            widthPlace = int(self.enemyXcoord[i] / 64)
            heightPlace = int(self.enemyYcoord[i] / 64)
        else:
            widthPlace = 0
            heightPlace = 0
        return (heightPlace, widthPlace)

    def positionLastEnemy(self):
        for i in range(self.numOfEnemies):
            if self.enemyYcoord[i] <= 600:
                return i
            else:
                continue

    def enemyMove(self, game, bullet, window, asteroid):

        for i in range(self.numOfEnemies):
            self.enemyXcoord[i] += self.enemySpeedChange[i]
            if self.enemyXcoord[i] <= 0:
                self.enemySpeedChange[i] = 0.5
                self.enemyYcoord[i] += self.enemyHightChange[i]
            elif self.enemyXcoord[i] >= 740:
                self.enemySpeedChange[i] = -0.5
                self.enemyYcoord[i] += self.enemyHightChange[i]
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)


            isCollision = game.collision(self.enemyXcoord[i], self.enemyYcoord[i], bullet.get_bulletXcoord(),
                                         bullet.get_bulletYcoord())
            if isCollision:
                bullet.set_bulletYcoord(470)
                bullet.set_bulletIsReady("Ready")
                game.set_score(10)
                self.enemyYcoord[i] = 2000
                self.enemySpeedChange[i] = 0
                self.enemyHightChange[i] = 0
                game.countofEnemies += 1
                self.numOfEnemiesforalgo -=1
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)
            if self.numOfEnemies == game.countofEnemies:
                game.end_game_win(window)
                for i in range(asteroid.numOfAsteroids):
                    asteroid.asteroidYcoord[i] = 1500
                break
            if self.enemyYcoord[i] > 400 and self.enemyYcoord[i] < 1900:
                for j in range(self.numOfEnemies):
                    self.enemyYcoord[j] = 1500
                    self.enemySpeedChange[i] = 0
                for i in range(asteroid.numOfAsteroids):
                    asteroid.asteroidYcoord[i] = 1500
                game.end_game_lose(window)
                break

    def newEnemyMove(self, game, bullet, window, asteroid):
        for i in range(self.numOfEnemies):
            if self.enemyXcoord[i] <= 0:
                self.enemyXcoord[i] = 0
            elif self.enemyXcoord[i] >= 740:
                self.enemyXcoord[i] = 740
            self.enemyYcoord[i] += self.enemyHightChange[i]
            self.enemyXcoord[i] += self.enemySpeedChange[i]
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)

            isCollision = game.collision(self.enemyXcoord[i], self.enemyYcoord[i], bullet.get_bulletXcoord(),
                                         bullet.get_bulletYcoord())
            if isCollision:
                bullet.set_bulletYcoord(470)
                bullet.set_bulletIsReady("Ready")
                game.set_score(10)
                self.enemyYcoord[i] = 2000
                self.enemySpeedChange[i] = 0
                game.countofEnemies += 1
                self.numOfEnemiesforalgo -= 1
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)
            if self.numOfEnemies == game.countofEnemies:
                game.end_game_win(window)
                for i in range(asteroid.numOfAsteroids):
                    asteroid.asteroidYcoord[i] = 1500
                break
            if self.enemyYcoord[i] > 400 and self.enemyYcoord[i] < 1900:
                self.enemyYcoord[i] = 1500
                self.enemySpeedChange[i] = 0
                for i in range(asteroid.numOfAsteroids):
                    asteroid.asteroidYcoord[i] = 1500
                game.end_game_lose(window)
                break

    def thirdEnemyMove(self, game, bullet, window, asteroid, player):
        for i in range(self.numOfEnemies):
            if self.enemyXcoord[i] <= 0:
                self.enemyXcoord[i] = 0
            elif self.enemyXcoord[i] >= 740:
                self.enemyXcoord[i] = 740
            self.enemyYcoord[i] += self.enemyHightChange[i]
            self.enemyXcoord[i] += self.enemySpeedChange[i]
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)

            if i == 0 or i == 2:

                if self.enemyXcoord[i] - player.playerXcoord <-10:
                    self.enemySpeedChange[i] = 0.05
                elif self.enemyXcoord[i] - player.playerXcoord>10:
                    self.enemySpeedChange[i] = -0.05
                else:
                    self.enemySpeedChange[i] = 0

            isCollision = game.collision(self.enemyXcoord[i], self.enemyYcoord[i], bullet.get_bulletXcoord(),
                                         bullet.get_bulletYcoord())
            if isCollision:
                bullet.set_bulletYcoord(470)
                bullet.set_bulletIsReady("Ready")
                game.set_score(10)
                self.enemyYcoord[i] = 2000
                self.enemySpeedChange[i] = 0
                game.countofEnemies += 1
                self.numOfEnemiesforalgo -= 1
            self.enemy(self.enemyXcoord[i], self.enemyYcoord[i], i, window)
            if self.numOfEnemies == game.countofEnemies:
                game.end_game_win(window)
                for i in range(asteroid.numOfAsteroids):
                    asteroid.asteroidYcoord[i] = 1500
                break
            if self.enemyYcoord[i] > 400 and self.enemyYcoord[i] < 1900:
                self.enemyYcoord[i] = 1500
                self.enemySpeedChange[i] = 0
                for i in range(asteroid.numOfAsteroids):
                    asteroid.asteroidYcoord[i] = 1500
                game.end_game_lose(window)
                break

    def get_numOfEnemy(self):
        return self.numOfEnemiesforalgo


    def enemyMoveRight(self, i):
        self.enemySpeedChange[i] = 0.3

    def enemyMoveLeft(self, i):
        self.enemySpeedChange[i] = -0.3

    def ranMove(self, i, way):
        if self.enemyXcoord[i]> way:
            self.enemySpeedChange[i] = -0.3
        elif self.enemyXcoord[i]<way:
            self.enemySpeedChange[i] = 0.3
        else:
            self.enemySpeedChange[i] = 0

    def firstCreation(self, i):
        if i == 0:
            self.enemyXcoord.append(118)
            self.enemyYcoord.append(96)
        elif i == 1:
            self.enemyXcoord.append(270)
            self.enemyYcoord.append(160)
        elif i == 2:
            self.enemyXcoord.append(478)
            self.enemyYcoord.append(96)
        elif i == 3:
            self.enemyXcoord.append(560)
            self.enemyYcoord.append(160)

    def secondCreation(self, i):
        if i == 0:
            self.enemyXcoord.append(118)
            self.enemyYcoord.append(160)
        elif i == 1:
            self.enemyXcoord.append(270)
            self.enemyYcoord.append(96)
        elif i == 2:
            self.enemyXcoord.append(478)
            self.enemyYcoord.append(160)
        elif i == 3:
            self.enemyXcoord.append(560)
            self.enemyYcoord.append(96)

    def thirdCreation(self, i):
        if i == 0:
            self.enemyXcoord.append(128)
            self.enemyYcoord.append(96)
        elif i == 1:
            self.enemyXcoord.append(320)
            self.enemyYcoord.append(160)
        elif i == 2:
            self.enemyXcoord.append(428)
            self.enemyYcoord.append(160)
        elif i == 3:
            self.enemyXcoord.append(560)
            self.enemyYcoord.append(96)
