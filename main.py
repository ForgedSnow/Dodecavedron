import random

cave_map = {
    1: (2, 5, 8),
    2: (1, 3, 10),
    3: (2, 4, 12),
    4: (3, 5, 14),
    5: (1, 4, 6),
    6: (5, 7, 15),
    7: (6, 8, 17),
    8: (1, 7, 9),
    9: (8, 10, 18),
    10: (2, 9, 11),
    11: (10, 12, 19),
    12: (3, 11, 13),
    13: (12, 14, 20),
    14: (4, 13, 15),
    15: (6, 14, 16),
    16: (15, 17, 20),
    17: (7, 16, 18),
    18: (9, 17, 19),
    19: (11, 18, 20),
    20: (13, 16, 19),
}


class Game:
    def __init__(self):
        # pick 6 random starting locations for the 2 pits, 2 bats, wumpus, and player
        random_locations = random.sample(sorted(cave_map.keys()), 6)

        self.wumpus = random_locations[0]
        self.player = random_locations[1]
        self.super_bats = random_locations[2:4]
        self.bottomless_pits = random_locations[4:6]

    def take_turn(self):
        # lookup which caves are adjacent to the cave the player is in
        caves_near_player = cave_map.get(self.player)
        # is the wumpus nearby
        if self.wumpus in caves_near_player:
            print('I smell a wumpus!')
        # is there a pit nearby
        if self.bottomless_pits[0] in caves_near_player or self.bottomless_pits[1] in caves_near_player:
            print('I feel a draft')
        # is there a bat nearby
        if self.super_bats[0] in caves_near_player or self.super_bats[1] in caves_near_player:
            print('Bats nearby!')


if __name__ == '__main__':
    hunt_the_wumpus = Game()
    hunt_the_wumpus.take_turn()
