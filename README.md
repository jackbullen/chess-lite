# chess-lite

A simple chess app written in JavaScript and Python using FastAPI and python-chess.

Matplotlib draws the chess board on a figure and writes the pieces with the text function and unicode chess characters.

<img width="749" alt="demo image" src="https://github.com/jackbullen/chess-lite/assets/37254717/c32cf700-797d-4500-b254-69a65b86b76d">

## Usage

Start a virtual environtment, install the dependencies, and start the fastapi app. Then run a server for frontend that will reload on changes (backend saves game state to board.png)

## Todo

- [x] Reset board
- [x] Move pieces with buttons
- Move pieces with drag and drop (Perhaps make frontend a react app and use library)
- Add a chess engine: display evaluations of position and moves, play game against engine, etc
- Loading pgn and viewing multiple games, writing pgn, exporting, etc
- Board UI: theme, size, orientation, etc
- Database: store games, users, leaderboard, chat, matchmaking, ratings, etc
- Game analysis, history, review, report, export, import system
- Enable user to annotate games easily

## Contribution

Feel free to contribute to this project.
