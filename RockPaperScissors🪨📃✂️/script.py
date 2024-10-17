import tkinter as tk
import random

def play_game():
    choice = user_choice.get()

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    lbl_user_choice['text'] = f'User choice is: {choice_name}'
    lbl_status['text'] = 'Now it’s the computer’s turn...'

    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    lbl_computer_choice['text'] = f'Computer choice is: {comp_choice_name}'
    lbl_result['text'] = f'{choice_name} vs {comp_choice_name}'

    if choice == comp_choice:
        result = "It's a Draw!"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Paper wins!'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'Rock wins!'
    else:
        result = 'Scissors wins!'

    if result.split()[0] == choice_name:
        lbl_winner['text'] = "User wins!"
    else:
        lbl_winner['text'] = "Computer wins!"

def reset_game():
    user_choice.set(1)
    lbl_user_choice['text'] = ''
    lbl_computer_choice['text'] = ''
    lbl_result['text'] = ''
    lbl_winner['text'] = ''
    lbl_status['text'] = ''

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# User choice variable
user_choice = tk.IntVar(value=1)

# Radio buttons for user to choose Rock, Paper, or Scissors
tk.Label(window, text="Choose your option:").grid(row=0, column=0, padx=10, pady=10)
tk.Radiobutton(window, text="Rock", variable=user_choice, value=1).grid(row=1, column=0)
tk.Radiobutton(window, text="Paper", variable=user_choice, value=2).grid(row=1, column=1)
tk.Radiobutton(window, text="Scissors", variable=user_choice, value=3).grid(row=1, column=2)

# Play button
btn_play = tk.Button(window, text="Play", command=play_game)
btn_play.grid(row=2, column=0, columnspan=3, pady=10)

# Labels to display user choice, computer choice, and result
lbl_user_choice = tk.Label(window, text="")
lbl_user_choice.grid(row=3, column=0, columnspan=3)
lbl_computer_choice = tk.Label(window, text="")
lbl_computer_choice.grid(row=4, column=0, columnspan=3)
lbl_result = tk.Label(window, text="")
lbl_result.grid(row=5, column=0, columnspan=3)
lbl_winner = tk.Label(window, text="", font=('Helvetica', 12, 'bold'))
lbl_winner.grid(row=6, column=0, columnspan=3)

# Status label
lbl_status = tk.Label(window, text="")
lbl_status.grid(row=7, column=0, columnspan=3)

# Reset button
btn_reset = tk.Button(window, text="Reset", command=reset_game)
btn_reset.grid(row=8, column=0, columnspan=3, pady=10)

# Quit button
btn_quit = tk.Button(window, text="Quit", command=window.quit)
btn_quit.grid(row=9, column=0, columnspan=3, pady=10)

window.mainloop()