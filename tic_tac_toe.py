import random


class TicTacToe:

    def __init__(self):
        self.board = []
        self.win = None

    def draw_board(self):
        # creates the board for playing the game
        # loops through the row
        for i in range(3):
            row = []
            # loops through the column
            for j in range(3):
                row.append('_')
            self.board.append(row)

    def get_random_first_player(self):
        # randomly picks between two players
        return random.randint(0, 1)

    def cell(self, row: int, column: int, player):
        # identifies a cell with the row number and column number and then
        # replaces it with the player currently playing
        self.board[row][column] = player

    def player_win(self, player):
        # gets the number of rows in the board
        rows = len(self.board)

        # checks each cell in the row
        for i in range(rows):
            self.win = True
            for j in range(rows):
                # check if cell in the row is equal to a particular
                # if True, the player wins else the player looses
                if self.board[i][j] != player:
                    self.win = False
                    break
            if self.win:
                return self.win

        # check each sell in the column
        for i in range(rows):
            self.win = True
            for j in range(rows):
                # check if cell in the column is equal to a particular
                # if True, the player wins else the player looses
                if self.board[j][i] != player:
                    self.win = False
                    break
            if self.win:
                return self.win

        # check each cell diagonally
        for i in range(rows):
            self.win = True
            # check if cell is equal to a particular
            # if True, the player wins else the player looses
            if self.board[i][i] != player:
                self.win = False
                break
        if self.win:
            return self.win

        for i in range(rows):
            self.win = True
            if self.board[i][rows - 1 - i] != player:
                self.win = False
                break
        if self.win:
            return self.win
        return False

    def is_board_filled(self):
        # check to see if all the cells are filled or empty
        for row in self.board:
            for item in row:
                if item == '_':
                    return False

        return True

    def swap_player(self, player):
        if player == 'O':
            player = 'X'
        else:
            player = 'O'

        return player

    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def play(self):
        self.draw_board()
        p = self.get_random_first_player()
        if p == 1:
            player = 'X'
        else:
            player = 'O'

        while True:
            print(f"Player {player} turn")

            self.print_board()

            # take the user input
            row, column = list(map(int, input("Enter the row and column number: ").split()))

            # enters the user input to the particular cell
            self.cell(row, column, player)

            # check if the current player won or not
            if self.player_win(player):
                print(f"Player {player} wins the game")
                break

            # check if the game is a draw
            if self.is_board_filled():
                print('Draw')
                break

            # swap player turn
            player = self.swap_player(player)

        # show the final view of the board
        self.print_board()
