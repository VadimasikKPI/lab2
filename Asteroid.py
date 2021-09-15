import pygame as pg

class Asteroid:
    asteroidIcon = []
    asteroidXcoord = []
    asteroidYcoord = []
    asteroidLives = []
    numOfAsteroids = 5

    def asteroidCreation(self):
        counter = 1
        for i in range(self.numOfAsteroids):
            self.asteroidIcon.append(pg.image.load('images/asteroid.png'))
            if counter == 1:
                self.asteroidXcoord.append(50)
                self.asteroidYcoord.append(350)
            if counter == 2:
                self.asteroidXcoord.append(330)
                self.asteroidYcoord.append(350)
            if counter == 3:
                self.asteroidXcoord.append(640)
                self.asteroidYcoord.append(350)
            if counter == 4:
                self.asteroidXcoord.append(170)
                self.asteroidYcoord.append(250)
            if counter == 5:
                self.asteroidXcoord.append(510)
                self.asteroidYcoord.append(250)

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

    def get_positionAsteroid(self):
        widthPlace = []
        heightPlace = []
        for i in range(self.numOfAsteroids):
            if self.asteroidXcoord[i]<800 and self.asteroidYcoord[i]<512:
                widthPlace.append(int(self.asteroidXcoord[i]/64))
                heightPlace.append(int(self.asteroidYcoord[i]/64))
            else:
                widthPlace.append(-1)
                heightPlace.append(-1)
