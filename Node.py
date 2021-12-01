
class Node:
    def __init__(self, player, invaders, bulls, move, bunkers):
        self.player = player.copy_object()
        self.invaders = [invader.copy_object() for invader in invaders]
        self.bulls = [bull.copy_object() for bull in bulls]
        self.bunkers = [bunker.copy_object() for bunker in bunkers]
        self.move = move
        self.is_terminal = False

    def generate_children(self, player):
        children = []
        for new_position, direction in [((-8, 0), '<'), ((8, 0), '>')]:
            node_position = (player.playerXcoord + new_position[0], player.playerYcoord + new_position[1])

            if node_position[0] > 800 - 1 or node_position[0] < 1 or node_position[1] > 576 - 1 or node_position[1] < 1:
                continue

            self.player.x += new_position[0]

            new_node = Node(self.player, self.invaders, self.bulls, direction, self.bunkers)

            children.append(new_node)
        return children

    def evaluation_function(self, enemy, player):
        centre_player = (
            player.playerXcoord + 32,
            player.playerYcoord + 32)
        distances = []
        for i in enemy.numOfEnemies:
            distances.append((centre_player, (enemy.enemyXcoord[i] + 32, enemy.enemyYcoord[i] + 32)))
        try:
            minvalue = min(distances)
        except ValueError:
            minvalue = 0
        return minvalue
