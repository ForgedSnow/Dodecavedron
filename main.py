import random

from data import cave_map


class HuntTheWumpus:
    def __init__(self):
        # pick 6 random starting locations for the 2 pits, 2 bats, wumpus, and player
        random_locations = random.sample(sorted(cave_map.keys()), 6)

        self.wumpus_location = random_locations[0]
        self.player_location = random_locations[1]
        self.super_bats = random_locations[2:4]
        self.bottomless_pits = random_locations[4:6]

        self.start_game()

    def start_game(self):
        while True:
            print("HUNT THE WUMPUS")
            if self.game_loop():
                print("CONGRATULATIONS YOU WON")
                break
            else:
                print("Game Over")
                replay = handle_input("SAME SET-UP? (Y-N)?", ['y', 'n'])
                if replay == 'n':
                    break

    def game_loop(self) -> bool:
        while True:
            # lookup which caves are adjacent to the hunter
            caves_near_player = cave_map.get(self.player_location)
            # is the wumpus nearby
            if self.wumpus_location in caves_near_player:
                print('I SMELL A WUMPUS!')
            # is there a pit nearby
            if self.bottomless_pits[0] in caves_near_player or self.bottomless_pits[1] in caves_near_player:
                print('I FEEL A DRAFT')
            # is there a bat nearby
            if self.super_bats[0] in caves_near_player or self.super_bats[1] in caves_near_player:
                print('BATS NEARBY!')

            print(f'YOU ARE IN ROOM {self.player_location}')
            print(f'TUNNELS LEAD TO {caves_near_player[0]}    {caves_near_player[1]}    {caves_near_player[2]}')

            next_action = handle_input("SHOOT OR MOVE (S-M)?", ['s', 'm'])
            if next_action == 'm':
                # move
                self.player_location = int(handle_input("Where to?", [str(cave_num) for cave_num in caves_near_player]))
                if self.player_location in self.bottomless_pits:
                    print("YYYIIIIEEEE . . . FELL IN PIT")
                    print("HA HA HA - YOU LOSE!")
                    return False
                elif self.player_location in self.super_bats:
                    print("ZAP--SUPER BAT SNATCH! ELSEWHEREVILLE FOR YOU!")
                    self.player_location = random.choice(cave_map.keys())
                elif self.player_location == self.wumpus_location:
                    # roll the dice. 25% chance to get eaten
                    if roll_dice(4) == 4:
                        # failed the 25% dice roll. you ded
                        print("tsk tsk tsk- Wumpus got you!")
                        return False
                    else:
                        print("... oops! Bumped a wumpus!")
                        # move the wumpus to a nearby room
                        self.wumpus_location = random.choice(cave_map.get(self.wumpus_location))
            else:
                # arrow
                arrow_distance = handle_input("No. of rooms(1-5)?", [str(num + 1) for num in range(5)])
                arrow_location = self.player_location
                for _ in range(int(arrow_distance)):
                    next_cave = handle_input("Room #?", [str(cave_num) for cave_num in cave_map.keys()])
                    adjacent_caves = cave_map.get(arrow_location)
                    if next_cave in adjacent_caves:
                        # if location is adjacent, move arrow there
                        arrow_location = next_cave
                    else:
                        # choose at random if it cant
                        arrow_location = random.choice(adjacent_caves)
                    if self.player_location == arrow_location:
                        print("Ouch! Arrow got you!")
                        return False
                    elif self.wumpus_location == arrow_location:
                        print("Aha! You got the Wumpus!")
                        return True


def roll_dice(sides: int) -> int:
    return random.randint(1, sides)


def handle_input(prompt: str, valid: list[str]) -> str:
    while True:
        maybe_valid_input = input(prompt)
        if maybe_valid_input.lower() in valid:
            return maybe_valid_input


if __name__ == '__main__':
    HuntTheWumpus()
