def numerosNoValidosFila(posicion, sudoku, sublistaSudoku): #recorremos el eje x de la matriz, es decir, la fila del elemento
    numerosNoValidos = []
    indiceFila = posicion - 1
    while(indiceFila != -1):
        #print("Número no válido encontrado, fila: "+str(sublistaSudoku)+" columna: "+str(indiceFila))
        #print("Número: "+str(sudoku[sublistaSudoku][indiceFila]))
        if(sudoku[sublistaSudoku][indiceFila] != 0):
            numerosNoValidos.append(sudoku[sublistaSudoku][indiceFila])
        indiceFila -= 1
    indiceFila = posicion + 1
    while(indiceFila != len(sudoku[sublistaSudoku])):
        #print("Número no válido encontrado, fila: "+str(sublistaSudoku)+" columna: "+str(indiceFila))
        #print("Número: "+str(sudoku[sublistaSudoku][indiceFila]))
        if(sudoku[sublistaSudoku][indiceFila] != 0):
            numerosNoValidos.append(sudoku[sublistaSudoku][indiceFila])
        indiceFila += 1
    return numerosNoValidos

def numerosNoValidosColumna(posicion, sudoku, sublistaSudoku): #recorremos el eje y de la matriz, es decir, la columna del elemento
    numerosNoValidos = []
    indiceColumna = sublistaSudoku - 1
    while(indiceColumna != -1):
        #print("Número no válido encontrado, fila: "+str(indiceColumna)+" columna: "+str(posicion))
        #print("Número: "+str(sudoku[indiceColumna][posicion]))
        if(sudoku[indiceColumna][posicion] != 0):
            numerosNoValidos.append(sudoku[indiceColumna][posicion])
        indiceColumna -= 1
    indiceColumna = sublistaSudoku + 1
    while(indiceColumna != len(sudoku)):
        #print("Número no válido encontrado, fila: "+str(indiceColumna)+" columna: "+str(posicion))
        #print("Número: "+str(sudoku[indiceColumna][posicion]))
        if(sudoku[indiceColumna][posicion] != 0):
            numerosNoValidos.append(sudoku[indiceColumna][posicion])
        indiceColumna += 1
    return numerosNoValidos

def numerosNoValidosCuadrado(posicion, sudoku, sublistaSudoku): #recorremos el cuadrado 2x2 del elemento
   numerosNoValidos = []
   if((sublistaSudoku+1)%2==0): #Sabemos si esta en la posición superior de su 2x2 o inferior
    print("Es fila par, el número se encuentra en la parte inferior de su 2x2")
    if((posicion+1)%2==0): #Sabemos si esta en la posición izquierda o derecha de su 2x2
        print("Es columna par, el número se encuentra en la parte derecha de su 2x2")
        numerosNoValidos.append(sudoku[sublistaSudoku-1][posicion-1])  #Así sacamos el único número que no fue guardado al revisar fila y columna
    else:
        print("Es columna impar, el número se encuentra en la parte izquierda de su 2x2")
        numerosNoValidos.append(sudoku[sublistaSudoku-1][posicion+1]) #Fila superior, columna derecha
   else:
    print("Es fila impar, el número se encuentra en la parte superior de su 2x2")
    if((posicion+1)%2==0): #Sabemos si esta en la posición izquierda de su 2x2 o derecha
        print("Es columna par, el número se encuentra en la parte derecha de su 2x2")
        numerosNoValidos.append(sudoku[sublistaSudoku+1][posicion-1])  #Fila inferior, columna izquierda
    else:
        print("Es columna impar, el número se encuentra en la parte izquierda de su 2x2")
        numerosNoValidos.append(sudoku[sublistaSudoku+1][posicion+1]) #Fila inferior, columna derecha
    
   return numerosNoValidos

def obtenerCandidatos(numerosNoValidos):
    filaLimpia= []
    for subLista in numerosNoValidos:
        for elemento in subLista:
            if elemento !=0 and elemento not in filaLimpia:
                filaLimpia.append(elemento)

    print("Números no válidos limpios: "+str(filaLimpia))
    candidatos = []
    for num in [1,2,3,4]:
        if num not in filaLimpia:
            candidatos.append(num)
    print("Candidatos encontrados: "+str(candidatos))
    return candidatos

def escribirNumero(filaSudoku, i_elemento, candidatos):
    if len(candidatos) == 1:
        filaSudoku[i_elemento] = candidatos[0]
        print("Número resuelto: "+str(filaSudoku))
        return True
    return False

def resolverSudoku(sudoku):
   cambios = True #Si en la última iteración devuelve True, significa que hubo cambios y se debe revisar nuevamente el sudoku
   while cambios:
    cambios = False
    candidatosPorCasilla = {}
    for i_lista in range(len(sudoku)):
        print("--Revisando fila: "+str(i_lista))
        for i_elemento in range(len(sudoku[i_lista])):
            print("--Revisando elemento: "+str(i_elemento))
            if sudoku[i_lista][i_elemento] == 0:
                numerosNoValidos = []
                print("Cero encontrado posición "+str(i_elemento))

                #Escogemos los números de la fila y columna del elemento
                numerosNoValidos.append(numerosNoValidosFila(i_elemento, sudoku, i_lista))
                numerosNoValidos.append(numerosNoValidosColumna(i_elemento, sudoku, i_lista))
                
                numerosNoValidos.append(numerosNoValidosCuadrado(i_elemento, sudoku, i_lista))
                print("Números no válidos: "+str(numerosNoValidos))
                candidatosPorCasilla[(i_lista, i_elemento)] = set(obtenerCandidatos(numerosNoValidos))

    for i_lista in range(len(sudoku)):
        for i_elemento in range(len(sudoku[i_lista])):
            posicion = (i_lista, i_elemento)
            if posicion in candidatosPorCasilla:
                candidatos = list(candidatosPorCasilla[posicion])
                resuelto = escribirNumero(sudoku[i_lista], i_elemento, candidatos)
                if resuelto:
                    cambios = True
   print("Sudoku resuelto: "+str(sudoku))
   return sudoku
print("SUDOKU")
RUTA_ENTRADA = "Sudoku/sudoku_sin_resolver.txt"
RUTA_SALIDA = "Sudoku/sudoku_resuelto.txt"
with open(RUTA_ENTRADA, "r", encoding="utf-8") as sudoku_bruto:
    lineas_sudoku = sudoku_bruto.readlines()
    linea_limpia = []
    sudoku_limpio = []
    for lista in lineas_sudoku:
        linea_limpia = lista.strip().strip("|").split("|")
        sudoku_limpio.append([int(elemento) for elemento in linea_limpia])

for fila in sudoku_limpio:
    print(fila)

sudokuResuelto =resolverSudoku(sudoku_limpio)
with open(RUTA_SALIDA, "w", encoding="utf-8") as sudoku_resuelto:
    for fila in sudokuResuelto:
        for elemento in fila:
         sudoku_resuelto.write("|" + str(elemento))
        sudoku_resuelto.write("| \n")