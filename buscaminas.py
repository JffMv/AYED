def typing (matrix, rows):
    cont = 0
    while cont != rows:
        matrix[cont] = input().split(",")
        cont +=1
    return matrix

def calculate (change,row):
    posi_row =change.index(row)
    posi = None
    for row in change:
        for column in row:
            if column == "*":
                posi = row.index(column)
                if posi == 0:
                    column[1]= column + 1
                else:
                    column[posi + 1], column[posi - 1] = column + 1, column +1 
        if posi_row == 0 and row > 1:
            row[1]= column[posi] + 1
        elif posi_row != 0 and row > 1:
            row [posi_row-1], row [posi_row + 1] = column[posi] + 1, column[posi] + 1
            row [posi_row], row [posi_row] = column[posi] + 1, column[posi] + 1
    return change

def run ():
    row = int((input ("how many are rows? ")))
    column = int((input("how many are columns? ")))

    matrix = [[ () for _ in range (row)] for _ in range(column)]

    change = typing(matrix, row)

    print_beatiful = calculate (change, row)


    for fila in print_beatiful:
        for columna in fila:
            print("{}\t".format(columna),end="")
        print("\n", end= "")
    


if __name__ == "__main__":
    run()