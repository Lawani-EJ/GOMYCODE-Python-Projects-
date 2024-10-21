![Assigned Project Task](./assets/Screenshot%20(154).png)

## Rock-Paper-Scissors Game with Tkinter 🪨📃✂️

This project implements a classic Rock-Paper-Scissors game using the Tkinter library in Python.

### Functionality

* Players choose their move (Rock, Paper, or Scissors) using radio buttons.
* Clicking the "Play" button generates a random choice for the computer.
* The game determines the winner and displays the user's choice, computer's choice, result (e.g., Rock vs Paper), and the winner (User or Computer).
* A "Reset" button allows players to start a new game.
* A "Quit" button closes the application.

### How it Works

1. **Imports:** The code imports `tkinter` for creating the graphical user interface (GUI) and `random` for generating the computer's choice.
2. **Functions:**
    * `play_game`: This function handles the game logic. It retrieves the user's choice from the radio buttons, generates the computer's choice, determines the winner based on the rules of Rock-Paper-Scissors, and displays the results on the labels.
    * `reset_game`: This function resets the game by setting the user's choice back to Rock, clearing all displayed text, and resetting the status label.
3. **GUI Creation:**
    * The code creates a main window titled "Rock-Paper-Scissors Game".
    * An `IntVar` named `user_choice` is used to store the user's selected option (1 for Rock, 2 for Paper, 3 for Scissors).
    * Radio buttons for Rock, Paper, and Scissors are created and linked to the `user_choice` variable.
    * A "Play" button triggers the `play_game` function when clicked.
    * Labels are created to display the user's choice, computer's choice, result, winner, and status messages.
    * A "Reset" button triggers the `reset_game` function to start a new game.
    * A "Quit" button closes the application.
4. **Running the Game:**
    * The `mainloop` function starts the main event loop of the Tkinter application, waiting for user interaction (clicks on buttons).
