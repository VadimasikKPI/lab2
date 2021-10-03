import pygame as pg

class Bullet:
    bulletIcon = pg.image.load('images/star_bullet.png')
    bulletXcoord = 360
    bulletYcoord = 470
    bulletHightChange = 0.25
    bulletIsReady = "Ready"

    def bullet(self, bulletX, bulletY, window):
        self.bulletIsReady = "Not ready"
        window.blit(self.bulletIcon, (bulletX + 32, bulletY + 10))


    def set_bulletXcoord(self, coord):
        self.bulletXcoord = coord

    def get_bulletIsReady(self):
        return self.bulletIsReady

    def get_bulletXcoord(self):
        return self.bulletXcoord

    def get_bulletYcoord(self):
        return self.bulletYcoord

    def bulletYchange(self):
        self.bulletYcoord -= self.bulletHightChange

    def set_bulletYcoord(self, change):
        self.bulletYcoord = change

    def set_bulletIsReady(self, change):
        self.bulletIsReady = change


    def changeYcoord(self, change):
        self.bulletYcoord += change

    def get_bulletHightChange(self):
        return self.bulletHightChange