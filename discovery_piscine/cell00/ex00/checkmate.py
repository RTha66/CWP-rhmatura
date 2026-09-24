def pawn(p_row, p_col, k_row, k_col):
    if k_row == p_row - 1 and k_col == p_col - 1:
        return True

    if k_row == p_row - 1 and k_col == p_col + 1:
        return True

    return False


def bishop(board, b_row, b_col, k_row, k_col):
    max_row = len(board)
    max_col = len(board[0])

    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:
        row = b_row + dr
        col = b_col + dc

        while 0 <= row < max_row and 0 <= col < max_col:

            if row == k_row and col == k_col:
                return True

            if board[row][col] != ".":
                break

            row += dr
            col += dc

    return False


def rook(board, r_row, r_col, k_row, k_col):
    max_row = len(board)
    max_col = len(board[0])

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:
        row = r_row + dr
        col = r_col + dc

        while 0 <= row < max_row and 0 <= col < max_col:

            if row == k_row and col == k_col:
                return True

            if board[row][col] != ".":
                break

            row += dr
            col += dc

    return False


def queen(board, q_row, q_col, k_row, k_col):
    max_row = len(board)
    max_col = len(board[0])

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:
        row = q_row + dr
        col = q_col + dc

        while 0 <= row < max_row and 0 <= col < max_col:

            if row == k_row and col == k_col:
                return True

            if board[row][col] != ".":
                break

            row += dr
            col += dc

    return False


def checkmate(board):

    rows = board.split("\n")

    if len(rows) == 0:
        return

    max_row = len(rows)
    max_col = len(rows[0])

    if max_row != max_col:
        return

    for row in rows:
        if len(row) != max_col:
            return

    king_row = -1
    king_col = -1

    for r in range(max_row):
        for c in range(max_col):
            if rows[r][c] == "K":
                king_row = r
                king_col = c

    if king_row == -1:
        return

    for r in range(max_row):
        for c in range(max_col):

            piece = rows[r][c]

            if piece == "P":
                if pawn(r, c, king_row, king_col):
                    print("Success")
                    return

            elif piece == "B":
                if bishop(rows, r, c, king_row, king_col):
                    print("Success")
                    return

            elif piece == "R":
                if rook(rows, r, c, king_row, king_col):
                    print("Success")
                    return

            elif piece == "Q":
                if queen(rows, r, c, king_row, king_col):
                    print("Success")
                    return

    print("Fail")














































# def pawn(p_row, p_col, k_row, k_col):
#     if k_row == p_row - 1 and k_col == p_col - 1:
#         return True

#     if k_row == p_row - 1 and k_col == p_col + 1:
#         return True

#     return False


# def bishop(board, b_row, b_col, k_row, k_col):
#     max_row = len(board)
#     max_col = len(board[0])
#     #max_col = max_row

#     directions = [
#         (-1, -1),  # up-left
#         (-1, 1),   # up-right
#         (1, -1),   # down-left
#         (1, 1)     # down-right
#     ]

#     for dr, dc in directions:
#         row = b_row + dr
#         col = b_col + dc

#         while 0 <= row < max_row and 0 <= col < max_col:

#             # Found the King
#             if row == k_row and col == k_col:
#                 return True

#             # Found another piece before reaching King
#             if board[row][col] != ".":
#                 break

#             row += dr
#             col += dc

#     return False


# def rook(board, r_row, r_col, k_row, k_col):
#     max_row = len(board)
#     max_col = len(board[0])
#     #max_col = max_row

#     directions = [
#         (-1, 0),  # up
#         (1, 0),   # down
#         (0, -1),  # left
#         (0, 1)    # right
#     ]

#     for dr, dc in directions:
#         row = r_row + dr
#         col = r_col + dc

#         while 0 <= row < max_row and 0 <= col < max_col:

#             # Found the King
#             if row == k_row and col == k_col:
#                 return True

#             # Found another piece before reaching King
#             if board[row][col] != ".":
#                 break

#             row += dr
#             col += dc

#     return False


# def queen(board, q_row, q_col, k_row, k_col):
#     max_row = len(board)
#     max_col = len(board[0])
#     #max_col = max_row

#     directions = [
#         (-1, 0),   # up
#         (1, 0),    # down
#         (0, -1),   # left
#         (0, 1),    # right
#         (-1, -1),  # up-left
#         (-1, 1),   # up-right
#         (1, -1),   # down-left
#         (1, 1)     # down-right
#     ]

#     for dr, dc in directions:
#         row = q_row + dr
#         col = q_col + dc

#         while 0 <= row < max_row and 0 <= col < max_col:

#             # Found the King
#             if row == k_row and col == k_col:
#                 return True

#             # Found another piece before reaching King
#             if board[row][col] != ".":
#                 break

#             row += dr
#             col += dc

#     return False


# def checkmate(board):

#     # Convert the board string into rows
#     rows = board.split("\n")

#     # Check that the board is not empty
#     if len(rows) == 0:
#         return

#     # Check that the board is square
#     max_row = len(board)
#     max_col = len(board[0])
#     #max_col = max_row

#     if max_row != max_col:
#         # return print(f"Error this is not a square board")
#         return

#     # Check that every row has the same length
#     for row in rows:
#         if len(row) != max_col:
#             # return print(f"Error row not equal to column")
#             return

#     # Find the King
#     king_row = -1
#     king_col = -1

#     for r in range(max_row):
#         for c in range(max_col):
#             if rows[r][c] == "K":
#                 king_row = r
#                 king_col = c

#     # If there is no King, stop
#     if king_row == -1:
#         # return print(f"Error no King found")
#         return

#     # Check every piece on the board
#     for r in range(max_row):
#         for c in range(max_col):

#             piece = rows[r][c]

#             if piece == "P":
#                 if pawn(r, c, king_row, king_col):
#                     print("Success")
#                     return

#             elif piece == "B":
#                 if bishop(rows, r, c, king_row, king_col):
#                     print("Success")
#                     return

#             elif piece == "R":
#                 if rook(rows, r, c, king_row, king_col):
#                     print("Success")
#                     return

#             elif piece == "Q":
#                 if queen(rows, r, c, king_row, king_col):
#                     print("Success")
#                     return

#     print("Fail")