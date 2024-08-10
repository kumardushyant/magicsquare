from typing import Dict, Any, List


def _get_squares(data: dict) -> list[dict[int, int]]:
    row = data["size"][0]
    col = data["size"][1]
    if row < 3 or col < 3:
        return []
    squares = []
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if i+2 <= row and j+2 <= col:
                square = {1: int(data[i, j]), 2: int(data[i, j + 1]), 3: int(data[i, j + 2]), 4: int(data[i + 1, j]), 5: int(data[i + 1, j + 1]),
                          6: int(data[i + 1, j + 2]), 7: int(data[i + 2, j]), 8: int(data[i + 2, j + 1]), 9: int(data[i + 2, j + 2])}
                squares.append(square)
    return squares


def _is_magic_square(data: dict) -> bool:
    n = 3
    row_sum = [0, 0, 0]
    col_sum = [0, 0, 0]
    diag_sum = [0, 0]
    for key, value in data.items():
        if key == 1 or key == 5 or key == 9:
            diag_sum[0] += value
        if key == 3 or key == 5 or key == 7:
            diag_sum[1] += value
        row_sum[(key - 1) // n] += value
        col_sum[(key - 1) % n] += value
    if row_sum[0] == row_sum[1] == row_sum[2] == col_sum[0] == col_sum[1] == col_sum[2] == diag_sum[0] == diag_sum[1]:
        return True
    return False


class MagicSquares:

    def __init__(self, data_file: str):
        self.file = data_file

    def _read_file(self) -> dict[int, dict[int, int]]:
        data: dict = {}
        with open(self.file, 'r') as file:
            row = 0
            for line in file.read().splitlines():
                row = row + 1
                col = 0
                for elem in line.split(","):
                    col += 1
                    data[row, col] = int(elem)
        data["size"] = [row, col]
        return data

    def create_magic_square(self) -> list:
        inp_data = self._read_file()
        squares = _get_squares(inp_data)
        magic_squares = []
        for square in squares:
            if _is_magic_square(square):
                magic_squares.append(square)
        return magic_squares
