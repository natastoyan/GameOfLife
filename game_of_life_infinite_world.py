hgcells = [
    [1, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1]
]

def crop_dead_cells(cells: list[list[int]]) -> list[list[int]]:
    i_indexes = []
    j_indexes = []
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            if cell:
                j_indexes.append(j)
                i_indexes.append(i)
    max_i = max(i_indexes)
    min_i = min(i_indexes)

    max_j = max(j_indexes)
    min_j = min(j_indexes)
    cells = cells[min_i:max_i+1]
    for i, row in enumerate(cells):
        cells[i] = row[min_j:max_j+1]
    return cells


def enlarge_cells(cells: list[list[int]]) -> list[list[int]]:
    cells.insert(0, [0 for i in cells[0]])
    cells.append([0 for i in cells[0]])
    for i, row in enumerate(cells):
        row.insert(0, 0)
        row.append(0)
    return cells


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    while generations > 0:
        cells = enlarge_cells(cells)
        cells = calculate_next_generation(cells)
        cells = crop_dead_cells(cells)
        generations -= 1
    return cells


def get_neighbours(cells: list[list[int]], i: int, j: int):
    max_ind_i = len(cells) - 1
    max_ind_j = len(cells[0]) - 1
    left_top = 0 if i == 0 or j == 0 else cells[i - 1][j - 1]
    middle_top = 0 if i == 0 else cells[i - 1][j]
    right_top = 0 if i == 0 or j == max_ind_j else cells[i - 1][j + 1]

    left_middle = 0 if j == 0 else cells[i][j - 1]
    right_middle = 0 if j == max_ind_j else cells[i][j + 1]

    left_bottom = 0 if i == max_ind_i or j == 0 else cells[i + 1][j - 1]
    middle_bottom = 0 if i == max_ind_i else cells[i + 1][j]
    right_bottom = 0 if i == max_ind_i or j == max_ind_j else cells[i + 1][j + 1]
    return left_top, middle_top, right_top, left_middle, right_middle, left_bottom, middle_bottom, right_bottom


def calculate_next_generation(cells: list[list[int]]) -> list[list[int]]:
    new_gen = [[0 for cell in cells[0]] for row in cells]
    for i, row in enumerate(cells):
        for j, cell in enumerate(cells[i]):
            neighbours = get_neighbours(cells, i, j)
            if cells[i][j] == 0 and sum(neighbours) == 3:
                new_gen[i][j] = 1
            elif cells[i][j] == 1 and (sum(neighbours) == 2 or sum(neighbours) == 3):
                new_gen[i][j] = 1
            else:
                new_gen[i][j] = 0
    return new_gen


bar = get_generation(hgcells, 16)
[print(row) for row in bar]

