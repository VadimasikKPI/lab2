from algoritms import bfs, ucs, dfs
import pygame as pg


def drawPath_dfs(window, enemy, graph, player, asteroidcoords):
    path = []
    lastPath = []
    for i in range(enemy.get_numOfEnemy()):
        path.append(bfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(i), asteroidcoords))
    if lastPath != path:
        for i in range(len(lastPath)):
            lastPath.pop(i)
        lastPath = path

    if len(path) == 1:
        for j in range(len(lastPath[0]) - 1):
            (y, x) = lastPath[0][j]
            x = x * 64
            y = y * 64
            pg.draw.rect(window, (0, 0, 255), pg.Rect(x, y, 48, 48))

    else:
        for i in range(len(path)):
            for j in range(len(path[i]) - 1):
                (y, x) = lastPath[i][j]
                x = x * 64
                y = y * 64
                pg.draw.rect(window, (0, 0, 255), pg.Rect(x, y, 48, 48))


def drawPath_bfs(window, enemy, graph, player, asteroidcoords):
    path = []
    lastPath = []

    if enemy.get_numOfEnemy == 1:
        path.append(bfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(), asteroidcoords))
    else:
        for i in range(enemy.get_numOfEnemy()):
            path.append(bfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(i), asteroidcoords))
    if lastPath != path:
        for i in range(len(lastPath)):
            lastPath.pop(i)
        lastPath = path


    if len(path) == 1:
        for j in range(len(lastPath[0])-1):
            (y, x) = lastPath[0][j]
            x = x * 64
            y = y * 64
            pg.draw.rect(window, (0, 200, 64), pg.Rect(x, y, 48, 48))

    else:
        for i in range(len(path)):
            for j in range(len(path[i]) - 1):
                (y, x) = lastPath[i][j]
                x = x * 64
                y = y * 64
                pg.draw.rect(window, (0, 200, 64), pg.Rect(x, y, 48, 48))


def drawPath_ucs(window, enemy, graph, player, asteroidcoords):
    path = []
    lastPath = []

    if enemy.get_numOfEnemy == 1:
        path.append(ucs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(), asteroidcoords))
    else:
        for i in range(enemy.get_numOfEnemy()):
            path.append(ucs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(i), asteroidcoords))
    if lastPath != path:
        for i in range(len(lastPath)):
            lastPath.pop(i)
        lastPath = path

    if len(path) == 1:
        for j in range(len(lastPath[0]) - 1):
            (y, x) = lastPath[0][j]
            x = x * 64
            y = y * 64
            pg.draw.rect(window, (200, 0, 64), pg.Rect(x, y, 48, 48))

    else:
        for i in range(len(path)):
            for j in range(len(path[i]) - 1):
                (y, x) = lastPath[i][j]
                x = x * 64
                y = y * 64
                pg.draw.rect(window, (200, 0, 64), pg.Rect(x, y, 48, 48))
