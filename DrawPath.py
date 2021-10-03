#from algoritms import bfs, ucs, dfs
from A_star import a_star_search, reconstruct_path, findWayToEnemy
import pygame as pg

def drawPath_Astar(window, enemy, graph, player, bullet):
    lastpath = []
    for i in range(enemy.numOfEnemiesforalgo):
        yPlayer, xPlayer = player.get_positionPlayer()
        yEemy, xEnemy = enemy.get_positionEnemy(i)
        path1 = a_star_search(graph, (yPlayer, xPlayer), (yEemy, xEnemy))
        path = reconstruct_path(path1, (yPlayer, xPlayer), (yEemy, xEnemy))
        lastpath.append(path)
    cost = lastpath
    index = findWayToEnemy(cost)
    # for i in range(len(cost[index])):
    #     (y, x) = cost[index][i]
    #     x = x * 64
    #     y = y * 64
    #     pg.draw.rect(window, (0, 0, 255), pg.Rect(x, y, 48, 48))
    player.moveplayerToEnemy(enemy, index, bullet, window)






# def drawPath_dfs(window, enemy, graph, player, asteroidcoords):
#     path = []
#     lastPath = []
#     for i in range(enemy.get_numOfEnemy()):
#         path.append(dfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(i), asteroidcoords))
#     if lastPath != path:
#         for i in range(len(lastPath)):
#             lastPath.pop(i)
#         lastPath = path
#
#     if len(path) == 1:
#         for j in range(len(lastPath[0]) - 1):
#             (y, x) = lastPath[0][j]
#             x = x * 64
#             y = y * 64
#             pg.draw.rect(window, (0, 0, 255), pg.Rect(x, y, 48, 48))
#
#     else:
#         for i in range(len(path)):
#             for j in range(len(path[i]) - 1):
#                 (y, x) = lastPath[i][j]
#                 x = x * 64
#                 y = y * 64
#                 pg.draw.rect(window, (0, 0, 255), pg.Rect(x, y, 48, 48))


# def drawPath_bfs(window, enemy, graph, player, asteroidcoords):
#     path = []
#     lastPath = []
#
#     if enemy.get_numOfEnemy == 1:
#         path.append(bfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(), asteroidcoords))
#     else:
#         for i in range(enemy.get_numOfEnemy()):
#             path.append(bfs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(i), asteroidcoords))
#     if lastPath != path:
#         for i in range(len(lastPath)):
#             lastPath.pop(i)
#         lastPath = path
#
#
#     if len(path) == 1:
#         for j in range(len(lastPath[0])-1):
#             (y, x) = lastPath[0][j]
#             x = x * 64
#             y = y * 64
#             pg.draw.rect(window, (0, 200, 64), pg.Rect(x, y, 48, 48))
#
#     else:
#         for i in range(len(path)):
#             for j in range(len(path[i]) - 1):
#                 (y, x) = lastPath[i][j]
#                 x = x * 64
#                 y = y * 64
#                 pg.draw.rect(window, (0, 200, 64), pg.Rect(x, y, 48, 48))
#
#
# def drawPath_ucs(window, enemy, graph, player, asteroidcoords):
#     path = []
#     lastPath = []
#
#     if enemy.get_numOfEnemy == 1:
#         path.append(ucs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(), asteroidcoords))
#     else:
#         for i in range(enemy.get_numOfEnemy()):
#             path.append(ucs(graph, player.get_positionPlayer(), enemy.get_positionEnemy(i), asteroidcoords))
#     if lastPath != path:
#         for i in range(len(lastPath)):
#             lastPath.pop(i)
#         lastPath = path
#
#     if len(path) == 1:
#         for j in range(len(lastPath[0]) - 1):
#             (y, x) = lastPath[0][j]
#             x = x * 64
#             y = y * 64
#             pg.draw.rect(window, (200, 0, 64), pg.Rect(x, y, 48, 48))
#
#     else:
#         for i in range(len(path)):
#             for j in range(len(path[i]) - 1):
#                 (y, x) = lastPath[i][j]
#                 x = x * 64
#                 y = y * 64
#                 pg.draw.rect(window, (200, 0, 64), pg.Rect(x, y, 48, 48))
