# 📝 Word Guessing Game

A simple **word guessing game** built using **Pygame**. Players attempt to guess a secret word within a limited number of attempts. The game provides feedback on guessed letters, indicating correct placements and incorrect choices.

### 🕹️ Gameplay
<div align="center">
    <img src="https://s3.gifyu.com/images/b2A1T.gif" width="300" height="300">
</div>

---

<br>
<h2>🎮 Features</h2>

- _Difficulty Levels:_ Choose between Easy (6 attempts), Medium (4 attempts), and Hard (3 attempts).

- _Keyboard Input:_ On-screen virtual keyboard for entering guesses.

- _Win/Lose Screens:_ Displays appropriate feedback when the game ends and shows the secret word.

- _Word Validation:_ Ensures only valid words from the word list are accepted.

<br>
<h2> 🛠️ Installation</h2>

1. **Clone the repository**:
   ```bash
   git clone https://github.com/juliaduken/guess-the-word.git
   cd word-guessing-game
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
