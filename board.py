import chess
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects

board = chess.Board()

LIGHT_SQUARE_COLOR = "#F0D9B5"
DARK_SQUARE_COLOR = "#B58863"

WHITE_PIECE_COLOR = "#f8f8f8"
BLACK_PIECE_COLOR = "#0e0e0e"

def update_plot(ax, board):
    for i in range(64):
        piece = board.piece_at(i)
        if piece:
            symbol = piece.symbol()
            if symbol.islower():
                symbol = f"♙♘♗♖♕♔"[piece.piece_type - 1].lower()
            else:
                symbol = f"♙♘♗♖♕♔"[piece.piece_type - 1]
            piece_color = WHITE_PIECE_COLOR if piece.color else BLACK_PIECE_COLOR
            text = ax.text(i%8 + 0.5, i//8 + 0.42, symbol, size=33, ha="center", va="center", color=piece_color, weight="extra bold")
            text.set_path_effects([path_effects.withStroke(linewidth=1.2, foreground='black')])

def draw_board(board):
    fig, ax = plt.subplots()
    for i in range(8):
        for j in range(8):
            color = LIGHT_SQUARE_COLOR if (i + j) % 2 == 0 else DARK_SQUARE_COLOR
            ax.add_patch(patches.Rectangle((j,i), 1, 1, facecolor=color, edgecolor="black"))
    update_plot(ax, board)

    ax.set_xlim([0,8])
    ax.set_ylim([0,8])
    ax.set_aspect('equal')
    ax.axis('off')
    plt.draw()
    plt.pause(0.001)

def draw_board_and_save(board, filename):
    fig, ax = plt.subplots()
    for i in range(8):
        for j in range(8):
            color = LIGHT_SQUARE_COLOR if (i + j) % 2 == 0 else DARK_SQUARE_COLOR
            ax.add_patch(patches.Rectangle((j,i), 1, 1, facecolor=color, edgecolor="black"))
    update_plot(ax, board)
    ax.set_xlim([0,8])
    ax.set_ylim([0,8])
    ax.set_aspect('equal')
    ax.axis('off')
    plt.savefig(filename)
    plt.close(fig)

def make_move(board):
    move = input("Enter your move (e.g., e2e4): ")
    if chess.Move.from_uci(move) in board.legal_moves:
        board.push(chess.Move.from_uci(move))
    else:
        print("Illegal move")

def main():
    while not board.is_game_over():
        draw_board(board)
        make_move(board)

if __name__ == "__main__":
    main()