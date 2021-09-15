import pygame as pg
import math


class Game:
    # Рахунок, шрифти і лічильник для кількості ворогів
    pg.init()
    score = 0
    fonts = pg.font.Font('freesansbold.ttf', 30)
    gameOver = pg.font.Font('freesansbold.ttf', 50)
    counter_enemy = 0

    def showScore(self, scoreXcoord, scoreYcoord, window):
        totalScore = self.fonts.render("Score: " + str(self.score), True, (255, 255, 255))
        window.blit(totalScore, (scoreXcoord, scoreYcoord))


    # Функція яка перевіряє чи доторкались вороги та пулі
    def collision(self, enemyXcoord, enemyYcoord, bulletXcoord, bulletYcoord):
        isCollision = math.sqrt((math.pow(enemyXcoord - bulletXcoord, 2)) + (math.pow(enemyYcoord - bulletYcoord, 2)))
        if isCollision < 30:
            return True
        else:
            return False

    def asteroidCollision(self, enemyXcoord, enemyYcoord, bulletXcoord, bulletYcoord):
        isCollision = math.sqrt((math.pow(enemyXcoord - bulletXcoord, 2)) + (math.pow(enemyYcoord - bulletYcoord, 2)))
        if isCollision < 55:
            return True
        else:
            return False



    def set_score(self, change):
        self.score += change

    def set_counterEnemy(self, change):
        self.counter_enemy += change

    def get_counterEnemy(self):
        return self.counter_enemy

    def end_game_win(self, window):
        gameOverTitle = self.gameOver.render("YOU WIN! CONGRATULATIONS", True, (255, 255, 255))
        window.blit(gameOverTitle, (10, 250))

    # Функція яка виводить повідомлення про програш на екран
    def end_game_lose(self, window):
        gameOvertitle = self.gameOver.render("YOU LOSE! TRY NEXT TIME!", True, (255, 255, 255))
        window.blit(gameOvertitle, (50, 250))

