# PyPy3

def print_board():
    for idx, val in enumerate(board):
        print(val, end=' ')
        if idx % 9 == 8:
            print()


def possible_set(index):
    set1 = {board[i] for i in range(index // 9 * 9, index // 9 * 9 + 9)}
    set2 = {board[i] for i in range(index % 9, 81, 9)}
    set3 = {board[i] for i in box[inv_box[index]]}
    return {1, 2, 3, 4, 5, 6, 7, 8, 9} - set1 - set2 - set3


def search(b_idx):
    global printed

    if printed:
        return

    if b_idx == blank_length:
        if not printed:
            printed = True
            print_board()
        return

    ps = possible_set(blank_index[b_idx])
    for s in ps:
        board[blank_index[b_idx]] = s
        search(b_idx + 1)

    board[blank_index[b_idx]] = 0
    return


box = {i: tuple([j for j in range(i // 3 * 27, i // 3 * 27 + 27) if i % 3 * 3 <= j % 9 < i % 3 * 3 + 3]) for i in range(9)}
inv_box = dict()
for key, value in box.items():
    for num in value:
        inv_box[num] = key

board = list()
for _ in range(9):
    board.extend(map(int, input().split()))

blank_index = [idx for idx, val in enumerate(board) if not val]
blank_length = len(blank_index)

printed = False
search(0)