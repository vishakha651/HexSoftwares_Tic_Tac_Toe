import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Puzzle Game")
        
        self.cards = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.time_limit = 60  # Time limit in seconds
        self.start_time = None
        
        self.create_cards()
        self.create_widgets()
        
    def create_cards(self):
        # Create a list of pairs of cards
        card_values = list(range(1, 9)) * 2  # 8 pairs
        random.shuffle(card_values)
        self.cards = card_values
        
    def create_widgets(self):
        self.buttons = []
        for i in range(4):  # 4 rows
            row = []
            for j in range(4):  # 4 columns
                button = tk.Button(self.master, text='', width=10, height=5,
                                   command=lambda i=i, j=j: self.flip_card(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        
        self.timer_label = tk.Label(self.master, text=f'Time left: {self.time_limit} seconds')
        self.timer_label.grid(row=4, column=0, columnspan=4)
        
        self.start_button = tk.Button(self.master, text='Start Game', command=self.start_game)
        self.start_button.grid(row=5, column=0, columnspan=4)
        
    def start_game(self):
        self.matched_pairs = 0
        self.flipped_cards = []
        self.start_time = time.time()
        self.update_timer()
        for row in self.buttons:
            for button in row:
                button.config(state=tk.NORMAL, text='', bg='SystemButtonFace')
        
    def flip_card(self, i, j):
        if len(self.flipped_cards) < 2 and self.buttons[i][j]['text'] == '':
            self.buttons[i][j].config(text=self.cards[i * 4 + j], bg='lightblue')
            self.flipped_cards.append((i, j))
            
            if len(self.flipped_cards) == 2:
                self.master.after(1000, self.check_match)
                
    def check_match(self):
        i1, j1 = self.flipped_cards[0]
        i2, j2 = self.flipped_cards[1]
        
        if self.cards[i1 * 4 + j1] == self.cards[i2 * 4 + j2]:
            self.matched_pairs += 1
            if self.matched_pairs == 8:
                self.end_game("You win!")
        else:
            self.buttons[i1][j1].config(text='', bg='SystemButtonFace')
            self.buttons[i2][j2].config(text='', bg='SystemButtonFace')
        
        self.flipped_cards = []
        
    def update_timer(self):
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            time_left = self.time_limit - elapsed_time
            
            if time_left <= 0:
                self.end_game("Time's up! You lose!")
            else:
                self.timer_label.config(text=f'Time left: {time_left} seconds')
                self.master.after(1000, self.update_timer)
                
    def end_game(self, message):
        self.start_time = None
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
        self.timer_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()