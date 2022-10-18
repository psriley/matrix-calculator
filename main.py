def print_matrix(num_list):
    num_semis = num_list.count(';')
    rows = get_num_rows(num_semis)
    cols = get_num_cols(num_list, num_semis)

    row = []
    print(f"Rows: {rows}")
    print(f"Columns: {cols}")
    for cell in num_list:
        if cell is not ';':
            row.append(cell)
        if cell is ';' or num_list.index(cell) is len(num_list) - 1:
            print(row)
            row.clear()


def get_num_rows(num_semis):
    # number of rows will be num_semis + 1 (no semicolon for last row)
    return num_semis + 1


def get_num_cols(num_list, num_semis):
    if num_semis > 0:
        # gets the index of the first semicolon, which is the number of columns
        return num_list.index(";")
    else:
        return 0


if __name__ == '__main__':
    print_matrix(['4', '3', '2', ';', '2', '1', '2'])
