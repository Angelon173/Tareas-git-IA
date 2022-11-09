###Problema 1 EL CUBO DE UN NUMERO 
def cubo(num1):
    c = num1 * num1 * num1
    return print("El cubo de", num1, "es", c)

cubo(9)


###Problema 2
def factorial(num2):
    if num2 == 1:
        return 1
    else:
        return(num2 * factorial(num2 - 1))

print(factorial(9))



###Problema 3
def repeticion(patron, cadena):
    r = cadena.count(patron)
    return print("se repite", r, "veces")

cadena = 'a v l o p q s a v l s a v l o'
patron = 'a v l'
repeticion(patron, cadena)






###Problema 5
from sympy import expand


def expresion(num3):
    return expand(num3)

print (expresion("(2*(x+1)*(y+3))"))