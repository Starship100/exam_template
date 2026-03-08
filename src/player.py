class Player:
    marker = "@"  # Symbolen för spelaren på kartan

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.inventory = []  # Lista på upplockade frukter/föremål

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy, grid):
        """Flyttar spelaren och kollar efter föremål"""
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy
        item = grid.get(new_x, new_y)

        # Om rutan inte är tom eller en vägg är det ett föremål
        if item != grid.empty and item != grid.wall:
            self.inventory.append(item.name)
            grid.clear(new_x, new_y)

        # Uppdatera spelarens position
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        #
        move_to_x = self.pos_x + dx
        move_to_y = self.pos_y + dy
        #
        tile = grid.get(move_to_x, move_to_y)

        # Om rutan är en vägg stoppas spelaren
        if tile == grid.wall:
            return False

        return True
        #TODO: returnera True om det inte står något i vägen


