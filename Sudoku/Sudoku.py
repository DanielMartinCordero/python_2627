
print("SUDOKU")
with open("Sudoku/sudoku_sin_resolver.txt", "r", encoding="utf-8") as sudoku_bruto:
    lineas_sudoku = sudoku_bruto.readlines()
    linea_limpia = []
    sudoku_limpio = []
    for lista in lineas_sudoku:
        linea_limpia = lista.strip().strip("|").split("|")
        sudoku_limpio.append([int(elemento) for elemento in linea_limpia])

"""if resolverSudoku(sudoku_limpio):
    print("Sudoku resuelto:")
else:
    print("Quedan casillas sin resolver:")
"""
for fila in sudoku_limpio:
    print(fila)

def resolverSudoku(sudoku_limpio):
   for lista in sudoku_limpio:
       for i in range(len(lista)):
           if lista[i] == 0:
               indiceCero = lista[i]
               if(indiceCero)
