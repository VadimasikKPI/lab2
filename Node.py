
class Node:
    def __init__(self, player, invaders, bulls, move, bunkers):
        self.player = player.copy_object()
        self.invaders = [invader.copy_object() for invader in invaders]
        self.bulls = [bull.copy_object() for bull in bulls]
        self.bunkers = [bunker.copy_object() for bunker in bunkers]
        self.move = move
        self.is_terminal = False