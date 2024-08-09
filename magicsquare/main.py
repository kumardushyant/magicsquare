class MagicSquares:

    def __init__(self, data_file: str):
        self.file = data_file

    def read_file(self) -> dict:
        data: dict = {}
        with open(self.file, 'r') as file:
            row = 0
            for line in file.read().splitlines():
                row = row + 1
                col = 0
                for elem in line.split(","):
                    col += 1
                    data[int(elem)] = (row, col)
        return data
