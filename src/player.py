class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.inventory = []

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def pick_up(self, item):
        """Sparar frukterna i listan"""
        self.inventory.append(item)

    def can_move(self, dx, dy, grid):
        #
        move_to_x = self.pos_x + dx
        move_to_y = self.pos_y + dy
        #
        tile = grid.get(move_to_x, move_to_y)
        if tile == grid.wall:
            return False

        return True
        #TODO: returnera True om det inte står något i vägen


