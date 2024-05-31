import tkinter as tk

class TicTacToe:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = [['-' for _ in range(n)] for _ in range(n)]
        self.player1 = True
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry(f"{n*100}x{n*100}")
        self.buttons = []
        for i in range(n):
            row = []
            for j in range(n):
                button = tk.Button(self.root, text="-", command=lambda i=i, j=j: self.make_move(i, j), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = 'X' if self.player1 else 'O'
            self.buttons[row][col].config(text=self.board[row][col])
            self.player1 = not self.player1
            if self.check_win():
                self.game_over()

    def check_win(self):
        # Check rows
        for row in self.board:
            for i in range(self.n - self.m + 1):
                if all(cell == row[i] and cell != '-' for cell in row[i:i + self.m]):
                    return True

        # Check columns
        for col in range(self.n):
            for i in range(self.n - self.m + 1):
                if all(self.board[i + j][col] == self.board[i][col] and self.board[i][col] != '-' for j in range(self.m)):
                    return True

        # Check diagonals
        for i in range(self.n - self.m + 1):
            if all(self.board[i + j][i + j] == self.board[i][i] and self.board[i][i] != '-' for j in range(self.m)):
                return True
            if all(self.board[i + j][self.n - i - 1 - j] == self.board[i][self.n - i - 1] and self.board[i][self.n - i - 1] != '-' for j in range(self.m)):
                return True

        return False

    def game_over(self):
        self.root.title("Game Over!")
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def play_game(self):
        self.root.mainloop()

if __name__ == "__main__":
    n = int(input("Enter grid size (n): "))
    while n < 3 or n > 10:
        n = int(input("Invalid input. Enter grid size (n) between 3 and 10: "))

    m = int(input("Enter win streak (m): "))
    while m < 3 or m > n:
        m = int(input(f"Invalid input. Enter win streak (m) between 3 and {n}: "))

    game = TicTacToe(n, m)
    game.play_game()