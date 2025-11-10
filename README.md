# Pong - Python (Pygame) — Multi-file Repo

Simple two-player Pong implemented with Pygame, split into modules with assets, tests and a README.

## Structure
- `src/` — game source files
- `assets/` — placeholders for sounds/images
- `tests/` — unit tests for pure-Python logic
- `requirements.txt` — dependencies

## Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the game:
   ```
   python -m pong_game.main
   ```

## Notes
- Game loop and rendering use `pygame`. Tests are focused on logic functions that do not require display.
- This repo is ready to be expanded with art and sounds in `assets/`.
