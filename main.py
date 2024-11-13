import os

os.system("cls")

#  que reciba dos parámetros: num_a y num_b. La función debe 
# realizar una de las siguientes operaciones:
#  suma, resta, multiplicación o división, según un tercer parámetro 
# llamado operacion
#  El tercer parámetro debe ser una cadena
#  que puede contener uno de los siguientes valores: "suma", "resta", 
# "multiplicacion" o "division"
#  La función debe realizar la operación correspondiente
#  y retornar el resultado
#  Ten en cuenta que, los números ingresados como
#  parámetros, pueden no ser válidos para ciertas operaciones. Por 
# ejemplo, la división por cero no está permitida.
#  Debes utilizar un bloque try...except para manejar los posibles 
# errores y retornar un mensaje de error si ocurre algún problema.

def calcular(num_a,num_b,operacion):
    try:
       if type(num_a) == int or type(num_a) == float or type(num_b) == int or type(num_b) == float and type(operacion) == str:
        if operacion.strip().lower() == "suma":
            resultado = num_a + num_b
            return print("el resultado de la suma es : ", resultado)
        elif operacion.strip().lower() == "resta":
            resultado = num_a - num_b
            return print("el resultado de la resta es:", resultado)
        elif operacion.strip().lower() == "multiplicacion":
            if num_a == 0 or num_b == 0:
                resultado = 0
                return print("el resultado de la multiplicacion es " , resultado)
            else:
                resultado = num_a * num_b
                return print("el resultado de la multiplicacion es : ", resultado)
        elif operacion.strip().lower() == "division":
            if num_a == 0 or num_b == 0:
                resultado = 0
                return print("el resultado de la division es " , resultado)
            else:
                resultado = num_a / num_b
                return print("el resultado de la multiplicacion es ", resultado)
        else:
            return print("elige una operacion valida")                       
    except:
        return print("operacion numerica invalida")


calcular(1,2,"suma") # elegir operacion desde el llamado a la funcion


