def missing_number (n,lista):
    for i in range(1,n+1):
        if i not in lista:
            return i 
        
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
assert missing_number(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10, "Error en el caso de prueba"
assert missing_number(3, [1, 3]) == 2, "Error en el caso de prueba"