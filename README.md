# 🎲 Random Number Guessing Game

Welcome to the **Random Number Guessing Game** — a simple yet fun Python project where players try to guess a randomly generated number within a defined range and limited attempts.

## 🚀 How It Works

- The player sets a **lower** and **upper bound** to define the range.
- The game randomly selects a number within that range.
- The player has **7 chances** to guess the correct number.
- After each guess, the game provides feedback:
  - `"Your guess is too high!"`
  - `"Your guess is too low!"`
  - `"Congratulations! Your guess is correct!"`
- If the player fails to guess correctly within 7 tries, the game reveals the number.

## 🧠 Features

- Input validation to handle non-integer entries
- Friendly prompts and error messages
- Simple logic flow for beginners to understand
- Uses Python’s built-in `random` and `time` modules

## 📦 Requirements

- Python 3.x  
No external libraries required.

## ▶️ How to Run

```bash
python guessing_game.py
