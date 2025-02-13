# 📝 Word Guessing Game

A simple **word guessing game** built using **Pygame**. Players attempt to guess a secret word within a limited number of attempts. The game provides feedback on guessed letters, indicating correct placements and incorrect choices.

### 🕹️ Gameplay
<div align="center">
    <img src="https://s3.gifyu.com/images/b2A1T.gif" width="300" height="300">
</div>

---

## 🎮 Features

- _Difficulty Levels:_ Choose between Easy (6 attempts), Medium (4 attempts), and Hard (3 attempts).

- _Keyboard Input:_ On-screen virtual keyboard for entering guesses.

- _Win/Lose Screens:_ Displays appropriate feedback when the game ends and shows the secret word.

- _Word Validation:_ Ensures only valid words from the word list are accepted.

<br>

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/juliaduken/guess-the-word.git
   ```
2. **Create a virtual environment** (optional but recommended):
   <br>_For Windows_
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   _For Mac_
   ```bash
   python -m venv venv
   venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the game**:
   ```bash
   python app.py
   ```

<br>

## 🎨 How to Play

1. **Launch the game** by running `python app.py`

2. **Select a difficulty**
    - 6 tries --> Easy
    - 4 tries --> Medium
    - 3 tries --> Hard
   
3. **Guess the word**
    - Click letters on the on-screen keyboard.
    - Letters turn _green_ (correct & in right position), _yellow_ (in the word but wrong position), or _gray_ (not in the word).
    - Press **Enter** to submit your guess, or **Del** if you need to backspace.
  
4. **Win or Lose**
    - Guess the word within the allowed attempts to win! 🎉
    - If you run out of attempts, the correct word is revealed. 

<br>

## 📂 Project Structure

```bash
word-guessing-game/
│── game/               # Main game logic and assets
│   ├── assets.py       # Loads game assets (images, buttons)
│   ├── config.py       # Stores configuration values (colors, screen size)
│   ├── draw.py         # Handles game rendering and drawing
│   ├── settings.py     # Initializes fonts and Pygame settings
│   ├── states.py       # Manages game states and logic
│   ├── ui.py           # Button handling and UI elements
│   ├── wordlist.py     # Loads and selects words for the game
│   ├── assets/         # Contains images and UI assets
│── .gitignore          # Specifies files to ignore in Git
│── app.py              # Main entry point to start the game
│── words.txt           # List of words for the game
│── requirements.txt    # Required dependencies (Pygame)
│── README.md           # Documentation
```
