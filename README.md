# chess-lite

A simple chess app written in JavaScript and Python using FastAPI and python-chess.

Matplotlib draws the chess board on a figure and writes the pieces with the text function and unicode chess characters.

<img width="749" alt="Demo Image" src="https://github.com/jackbullen/chess-lite/assets/37254717/23adafa3-d66d-4629-9fd4-5c554637e3fd">

## Usage

1. Start a virtual environtment, install the dependencies, and start the fastapi app. Then run a server for frontend that will reload on changes (backend saves game state to board.png)

## Todo

- [x] Reset board
- [x] Move pieces with buttons
- Move pieces with drag and drop (Perhaps make frontend a react app and use library)
- ([]) Add a chess engine: display evaluations of position and moves, play game against engine, etc
([]) Loading pgn and viewing multiple games, writing pgn, exporting, etc
([x]) Board UI: theme, size, orientation, etc
- [] Database: store games, users, leaderboard, chat, matchmaking, ratings, etc
- [] Game analysis, history, review, report, export, import system
- [] Enable user to annotate games easily

## Contribution

Feel free to contribute to this project.
