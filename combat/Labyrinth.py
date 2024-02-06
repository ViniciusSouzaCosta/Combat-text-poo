from game import CombatGame
import Bullet
import Tank

class CombatGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Tank(player1_name, 0, 4)
        self.player2 = Tank(player2_name, 9, 4)
        self.board = [["." for _ in range(10)] for _ in range(10)]

    def draw_board(self):
        for row in self.board:
            print(" ".join(row))

    def update_board(self):
        self.board = [["." for _ in range(10)] for _ in range(10)]
        self.board[self.player1.x][self.player1.y] = "P1"
        self.board[self.player2.x][self.player2.y] = "P2"
