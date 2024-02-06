import Bullet
import Labyrinth
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

def play(self):
    print("Combat Game")
    print("-----------")

    while True:
        self.update_board()
        self.draw_board()

        print(f"\n{self.player1.name}, choose your action (1-5): ")
        input()

        if self.shoot(self.player1, self.player2):
            print(f"{self.player1.name} hits {self.player2.name}!")
            print(f"{self.player2.name} is defeated!")
            break
        else:
            print(f"{self.player1.name} missed!")

        print(f"\n{self.player2.name}, choose your action (1-5): ")
        input()

        if self.shoot(self.player2, self.player1):
            print(f"{self.player2.name} hits {self.player1.name}!")
            print(f"{self.player1.name} is defeated!")
            break
        else:
            print(f"{self.player2.name} missed!")

if __name__ == "__main__":
    game = CombatGame("Player 1", "Player 2")
    game.play()