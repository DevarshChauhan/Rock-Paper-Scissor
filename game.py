import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        # Create label to display game result
        self.result_label = tk.Label(master, text="", wraplength=200)
        self.result_label.pack()

        # Create buttons for rock, paper, and scissors
        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT)
        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT)
        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT)

        # Create play again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again)
        self.play_again_button.pack()

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        if (user_choice == "rock" and computer_choice == "scissors") or \
           (user_choice == "paper" and computer_choice == "rock") or \
           (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        return "Computer wins!"

    def play_again(self):
        self.result_label.config(text="")

root = tk.Tk()
my_game = RockPaperScissors(root)
root.mainloop()
