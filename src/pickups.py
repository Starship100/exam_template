import random

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):
        self.name = name    # Föremålens namn t.ex "apple"
        self.value = value   # Hur många poäng det ger
        self.symbol = symbol  # Tecknet för föremålen på spelplanen

    def __str__(self):
        return self.symbol

# Listan med alla föremål i spelet
pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

def spawn_one(grid):
    """Slumpar en frukt ut på spelplanen"""
    item = random.choice(pickups)
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, item)
            break # Avsluta när föremålet har placerats
