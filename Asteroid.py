import pygame as pg

class Asteroid:
    asteroidIcon = []
    asteroidXcoord = []
    asteroidYcoord = []
    asteroidLives = []
    numOfAsteroids = 3

    def asteroidCreation(self):
        counter = 1
        for i in range(self.numOfAsteroids):
            self.asteroidIcon.append(pg.image.load('images/asteroid.png'))
            if(counter == 1):
                self.asteroidXcoord.append(50)
            if (counter == 2):
                self.asteroidXcoord.append(330)
            if (counter == 3):
                self.asteroidXcoord.append(640)
            self.asteroidYcoord.append(350)
            self.asteroidLives.append(2)
            counter +=1

    def asteroids(self, window, i, asteroidX, asteroidY):
        window.blit(self.asteroidIcon[i], (asteroidX, asteroidY))

    def lifeCicleAsteroid(self, bullet, game, window):
        for i in range(self.numOfAsteroids):
            self.asteroids(window, i, self.asteroidXcoord[i], self.asteroidYcoord[i])

            isCollision = game.asteroidCollision(self.asteroidXcoord[i], self.asteroidYcoord[i], bullet.get_bulletXcoord(),
                                         bullet.get_bulletYcoord())
            if isCollision:
                bullet.set_bulletYcoord(470)
                bullet.set_bulletIsReady("Ready")
                self.asteroidIcon[i] = pg.image.load('images/asteroid_broken.png')
                self.asteroidLives[i] -= 1

            if self.asteroidLives[i] == 0:
                self.asteroidYcoord[i] = 2700
            self.asteroids(window, i, self.asteroidXcoord[i], self.asteroidYcoord[i])