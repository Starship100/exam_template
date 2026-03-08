from .grid import Grid
from .player import Player
from . import pickups



player = Player(18, 5) # Skapar spelaren på denna position
score = 0                    # Total poäng
steps_taken = 0              # Räknare för att veta när nya frukter ska dyka upp

g = Grid()
g.set_player(player)  # Placerar spelaren i spelplanens system
g.make_walls()        # Skapar spelets ytterväggar
g.make_inside_walls() # Skapar nya väggar och hinder på inuti spelplanen
pickups.randomize(g)  # Slumpar ut de första föremålen


def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, i for Inventory or Q/X to quit. ")
    command = command.casefold()[:1]

    # Visar inventory om spelaren trycker på "i"
    if command == "i":
        print("Inventory: ")
        print(player.inventory)

    """Hanterar användarens w, a, s, d tryckningar"""
    if command == "w" and player.can_move(0, -1, g):  # move right
        score -= 1
        maybe_item = g.get(player.pos_x, player.pos_y - 1)
        player.move(0, -1, g)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

        steps_taken += 1
        if steps_taken == 25:
            pickups.spawn_one(g)
            steps_taken = 0

    if command == "a" and player.can_move(-1, 0, g):  # move right
        score -= 1
        maybe_item = g.get(player.pos_x - 1, player.pos_y)
        player.move(-1, 0, g)
        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

        steps_taken += 1
        if steps_taken == 25:
            pickups.spawn_one(g)
            steps_taken = 0

    if command == "s" and player.can_move(0, 1, g):  # move right
        score -= 1
        maybe_item = g.get(player.pos_x, player.pos_y + 1)
        player.move(0, 1, g)
        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

        steps_taken += 1
        if steps_taken == 25:
            pickups.spawn_one(g)
            steps_taken = 0

    if command == "d" and player.can_move(1, 0, g):  # move right
        score -= 1
        maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0, g)
        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

        steps_taken += 1
        if steps_taken == 25:
            pickups.spawn_one(g)
            steps_taken = 0

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

