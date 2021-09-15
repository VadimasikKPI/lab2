import pygame as pg


class Player:
    playerIcon = pg.image.load('images/player.png')
    playerXcoord = 384
    playerYcoord = 470
    playerSpeedChange = 0

    def player(self, playerX, playerY, window):
        window.blit(self.playerIcon, (playerX, playerY))

    def set_playerSpeedChange(self, change):
        self.playerSpeedChange = change

    def get_playerXcoord(self):
        return self.playerXcoord

    def set_playerXcoord(self, coord):
        self.playerXcoord += coord

    def get_playerSpeedChange(self):
        return self.playerSpeedChange

    def get_playerYcoord(self):
        return self.playerYcoord

    def get_positionPlayer(self):
        widthPlace = int(self.playerXcoord / 64)
        heightPlace = int(self.playerYcoord / 64)
        return (heightPlace, widthPlace)

    def outOfBounds(self):
        if self.playerXcoord <= 0:
            self.playerXcoord = 0
        elif self.playerXcoord >= 740:
            self.playerXcoord = 740

