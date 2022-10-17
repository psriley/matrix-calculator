def print_matrix(numList):
    row = []
    for cell in numList:
        if cell is not ';':
            row.append(cell)
        if cell is ';' or numList.index(cell) is len(numList) - 1:
            print(row)
            row.clear()


if __name__ == '__main__':
    print_matrix(['4', '3', ';', '2', '1'])
