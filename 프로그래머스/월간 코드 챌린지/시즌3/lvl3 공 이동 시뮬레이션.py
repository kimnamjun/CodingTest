def solution(n, m, x, y, queries):
    row_m1, col_m1, target_row, target_col = n - 1, m - 1, x, y

    left, right, top, bottom = target_col, target_col, target_row, target_row
    for direction, distance in reversed(queries):
        if direction == 0:
            right += distance
            if left != 0:
                if left + distance > col_m1:
                    return 0
                left += distance
        elif direction == 1:
            left -= distance
            if right != col_m1:
                if right - distance < 0:
                    return 0
                right -= distance
        elif direction == 2:
            bottom += distance
            if top != 0:
                if top + distance > row_m1:
                    return 0
                top += distance
        elif direction == 3:
            top -= distance
            if bottom != row_m1:
                if bottom - distance < 0:
                    return 0
                bottom -= distance

        left = min(max(left, 0), col_m1)
        right = min(max(right, 0), col_m1)
        top = min(max(top, 0), row_m1)
        bottom = min(max(bottom, 0), row_m1)

    return (right - left + 1) * (bottom - top + 1)