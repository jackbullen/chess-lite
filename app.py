from board import *
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from io import BytesIO
import traceback

app = FastAPI()
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MoveModel(BaseModel):
    move: str

@app.get("/start-new-game")
async def start_new_game():
    global board
    board = chess.Board()
    draw_board_and_save(board, 'board.png')

@app.post("/move")
async def make_move(move_data: MoveModel):
    global board
    move = move_data.move
    try:
        print(move_data)
        chess_move = chess.Move.from_uci(move)
        print(move)
        if chess_move in board.legal_moves:
            board.push(chess_move)
            draw_board_and_save(board, 'board.png')
            return {"message": f"Move {move} was made"}
        else:
            return {"message": f"Move {move} is illegal"}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="Invalid move")

# This might be better frontend for getting board image.
# I think the current way (saving image) is not the best.
# Probably having the image for board is bad idea altogether, 
# but it's easy to implement.
# @app.get("/board-image")
# async def get_board_image():
#     return FileResponse("board.png")

@app.get("/legal-moves")
async def get_legal_moves():
    global board
    moves = [move.uci() for move in board.legal_moves]
    return {"moves": moves}