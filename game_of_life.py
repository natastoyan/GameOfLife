def get_next_generation(cells: list[list[int]]) -> list[list[int]]:
    new_gen = [[0 for _ in cells[0]] for _ in cells]
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            next_i = i + 1 if i < len(cells) - 1 else 0
            next_j = j + 1 if j < len(row) - 1 else 0
            prev_i = i - 1
            prev_j = j - 1
            neighbours = (cells[prev_i][prev_j], cells[prev_i][j], cells[prev_i][next_j],
                          cells[i][prev_j], cells[i][next_j],
                          cells[next_i][prev_j], cells[next_i][j], cells[next_i][next_j])
            if cells[i][j] == 0 and sum(neighbours) == 3:
                new_gen[i][j] = 1
            elif cells[i][j] == 1 and (sum(neighbours) == 2 or sum(neighbours) == 3):
                new_gen[i][j] = 1
            else:
                new_gen[i][j] = 0
    return new_gen


