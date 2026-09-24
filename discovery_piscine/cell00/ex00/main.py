from checkmate import checkmate


def main():
    board = """\
R...
...K
..P.
....\
"""

#     board = """\
# .K
# .B\
# """
    checkmate(board)


if __name__ == "__main__":
    main()