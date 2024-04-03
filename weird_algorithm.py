   
def weird_algorithm(n):
    if n<0: return False
    x=int(n)
    result =[x]
    while (x!=1):
        if x%2 == 0:
            x=x//2
        else:
            x=(x*3+1)
        result.append(x)
    return result

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
assert weird_algorithm(1) == [1], "Error en el caso de prueba"
assert weird_algorithm(10) == [10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"