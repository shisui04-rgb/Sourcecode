import random

class LudoGame:
    def __init__(self):
        self.board = [' ' for _ in range(52)]  # 52 spaces on the board
        self.players = ['Player 1', 'Player 2']
        self.pieces = {'Player 1': ['A', 'B', 'C', 'D'], 'Player 2': ['E', 'F', 'G', 'H']}
        self.piece_positions = {'Player 1': {'A': 0, 'B': 0, 'C': 0, 'D': 0}, 'Player 2': {'E': 0, 'F': 0, 'G': 0, 'H': 0}}

    def roll_dice(self):
        return random.randint(1, 6)

    def move_piece(self, player, piece, spaces):
        current_position = self.piece_positions[player][piece]
        new_position = (current_position + spaces) % 52
        self.piece_positions[player][piece] = new_position
        self.board[current_position] = ' '
        self.board[new_position] = piece

    def capture_piece(self, player, piece, opponent_piece):
        opponent_position = self.piece_positions[self.get_opponent(player)][opponent_piece]
        self.piece_positions[self.get_opponent(player)][opponent_piece] = 0
        self.board[opponent_position] = ' '

    def get_opponent(self, player):
        return 'Player 2' if player == 'Player 1' else 'Player 1'

    def print_board(self):
        print('  ', end='')
        for i in range(52):
            print(self.board[i], end=' ')
            if (i + 1) % 13 == 0:
                print()

    def play_game(self):
        current_player = 'Player 1'
        while True:
            input(f"{current_player}'s turn. Press Enter to roll the dice.")
            roll = self.roll_dice()
            print(f"You rolled a {roll}.")
            piece_to_move = input("Which piece would you like to move? ")
            if piece_to_move not in self.pieces[current_player]:
                print("Invalid piece. Please try again.")
                continue
            self.move_piece(current_player, piece_to_move, roll)
            self.print_board()
            if self.piece_positions[current_player][piece_to_move] == 51:
                print(f"{current_player} wins!")
                break
            current_player = self.get_opponent(current_player)

game = LudoGame()
game.play_game()
