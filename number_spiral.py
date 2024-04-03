def number_spiral(row, column):
    if row == column:
        return row**2 - row + 1
    if row > column:
        if row % 2 == 0:
            return row**2 - column + 1
        else:
            return (row - 1)**2 + column
    else: 
        if column % 2 == 0:
            return (column - 1)**2 + row
        else:
            return column**2 + 1 - row
        

assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
assert number_spiral(1, 1) == 1, "Error en el caso de prueba"
assert number_spiral(3, 1) == 5, "Error en el caso de prueba"