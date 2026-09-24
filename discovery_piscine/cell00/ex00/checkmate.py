#function ที่เก็บ pattern การเดินของหมาก pawn 
def pawn(p_row, p_col, k_row, k_col): #รับค่ามา 4 ค่า คือ ตำแหน่ง row-col ของ pawn row-col ของ king

    #ถ้าแถวของ king เท่ากับแถวของ P-1 และ คอลลัมของ king เท่ากับ คอลัมของ pawn-1 จะ return true  
    if k_row == p_row - 1 and k_col == p_col - 1:
        return True

    #ถ้าแถวของ king เท่ากับแถวของ P-1 และ คอลลัมของ king เท่ากับ คอลัมของ pawn+1 จะ return true  
    if k_row == p_row - 1 and k_col == p_col + 1:
        return True

    #other case return false
    return False

#function ที่เก็บ pattern การเดินของหมาก bishop
def bishop(board, b_row, b_col, k_row, k_col):
    #หาแถวที่มาที่สุดที่เป็นไปได้ด้วยการใช้ len นับ board
    max_row = len(board)

    #เนื่องจากเป็นตารางจัตุรัสอยู่แล้ว max col= max row 
    max_col = max_row

    #สร้าง direction มาเก็บทิศการเดินในแนวทแยง
    directions = [
        (-1, -1),  # up-left
        (-1, 1),   # up-right
        (1, -1),   # down-left
        (1, 1)     # down-right
    ]

    #loop การเดินของ bishop
    for dr, dc in directions:
        row = b_row + dr
        col = b_col + dc

        #เดินไปเรื่อย ๆ จนกว่าจะออกนอก board หรือเจอหมากตัวอื่น
        while 0 <= row < max_row and 0 <= col < max_col:

            #Found King
            if row == k_row and col == k_col:
                return True

            #Found another piece before reaching King
            if board[row][col] in "PQR":
                break

            #เดินต่อในทิศเดิม
            row += dr
            col += dc

    #กิน king ไม่ได้ return flase
    return False

#function ที่เก็บ pattern การเดินของหมาก rook
def rook(board, r_row, r_col, k_row, k_col):
    #หาแถวที่มาที่สุดที่เป็นไปได้ด้วยการใช้ len นับ board
    max_row = len(board)

    #เนื่องจากเป็นตารางจัตุรัสอยู่แล้ว max col= max row 
    max_col = max_row

    #สร้าง direction มาเก็บทิศการเดินในแนวตรงและแนวนอน
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    #loop การเดินของ rook
    for dr, dc in directions:
        row = r_row + dr
        col = r_col + dc

        # เดินไปเรื่อย ๆ จนกว่าจะออกนอก board หรือเจอหมากตัวอื่น
        while 0 <= row < max_row and 0 <= col < max_col:

            # Found King
            if row == k_row and col == k_col:
                return True

            # Found another piece before reaching King
            if board[row][col] in "PQB":
                break

            #เดินต่อในทิศเดิม
            row += dr
            col += dc

    #rook กิน king ไม่ได้
    return False

#function ที่เก็บ pattern การเดินของหมาก queen
def queen(board, q_row, q_col, k_row, k_col):
    #หาแถวที่มาที่สุดที่เป็นไปได้ด้วยการใช้ len นับ board
    max_row = len(board)

    #เนื่องจากเป็นตารางจัตุรัสอยู่แล้ว max col= max row 
    max_col = max_row


    #สร้าง direction มาเก็บทิศการเดินแบบเอาการเดินของ bishop และ rook มารวมกัน
    directions = [
        (-1, 0),   # up
        (1, 0),    # down
        (0, -1),   # left
        (0, 1),    # right
        (-1, -1),  # up-left
        (-1, 1),   # up-right
        (1, -1),   # down-left
        (1, 1)     # down-right
    ]

    #loop การเดินของ queen
    for dr, dc in directions:
        row = q_row + dr
        col = q_col + dc

        # เดินไปเรื่อย ๆ จนกว่าจะออกนอก board หรือเจอหมากตัวอื่น
        while 0 <= row < max_row and 0 <= col < max_col:

            #Found King
            if row == k_row and col == k_col:
                return True

            #Found another piece before reaching King
            if board[row][col] in "PBR":
                break

            #เดินต่อในทิศเดิม
            row += dr
            col += dc

    #queen กิน king ไม่ได้
    return False


def checkmate(board):

    #แปลง board จาก string ให้เป็น list ของแต่ละแถว
    rows = board.split("\n")

    max_row = len(rows)
    max_col = max_row

    #จะได้ไม่ต้องเรียกซ้ำ
    #ตรวจว่า board ว่างมั้ย ถ้าว่างก็จบการทำงาน
    if len(rows) == 0:
        return

    #เช็คว่าบอร์ดเป็นจัตุรัส
    

    #เช็คว่าแต่ละแถวมีจำนวนช่องเท่ากัน
    for r in rows:
        if len(r) != max_row:
            return

    #กำหนดตำแหน่งเริ่มต้นของ king
    king_row = -1
    king_col = -1

    #loop to find king's position
    king_amount = 0
    for r in range(max_row):
        for c in range(max_col):
            if rows[r][c] == "K":
                king_row = r
                king_col = c
                king_amount += 1

    #If there is no King, stop
    if king_row == -1:
        return

    if king_amount != 1:
        return

    #ถ้ามี king เยอะกว่า 1 ตัว


    #วนตรวจสอบหมากทุกตัวบน board
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
    print(f"Fail")