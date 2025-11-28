# Word Guess (Stickman-style) Game

A simple terminal-based Python word-guessing game inspired by stickman/hangman.  
The game reveals the vowels of a secret word and the player guesses consonants. The player has 5 chances for incorrect guesses. Words are grouped into three categories: **Cars**, **Animals**, and **Places**.

---

## Features
- CLI / terminal gameplay — no GUI needed.
- 3 categories to choose from: **Cars**, **Animals**, **Places**.
- Vowels are revealed at start; player fills in consonants (spaces are preserved).
- Allows single-letter guesses and guessing the full word.
- Input validation and clear user prompts.
- No external dependencies — pure Python.

---

## Prerequisites
- Python 3.8+ installed.
- Terminal / command prompt or VS Code integrated terminal.

---

## Installation / Setup
1. Save the game script as `game.py`.
2. In your terminal, run:
```bash
python game.py
