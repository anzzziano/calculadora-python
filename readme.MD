# Calculadora Básica en Python
Este script proporciona una función de calculadora básica que permite realizar operaciones aritméticas simples: suma, resta, multiplicación y división.

## Descripción de la Función
La función calcular recibe tres parámetros:

num_a: Primer número (puede ser un número entero o decimal).
num_b: Segundo número (puede ser un número entero o decimal).
operacion: Una cadena de texto que especifica la operación que se desea realizar. Las operaciones válidas son:

"suma"

"resta"

"multiplicacion"

"division"

La función verifica que num_a y num_b sean números (entero o decimal) y que operacion sea una cadena de texto válida.
En caso de que el tipo de dato no sea correcto o que no se indique una operación válida, se mostrará un mensaje de error.

# Realiza una suma de 1 y 2
calcular(1, 2, "suma")
 Resultado esperado: el resultado de la suma es :  3

# Realiza una resta de 5 menos 3
calcular(5, 3, "resta")
 Resultado esperado: el resultado de la resta es : 2

# Realiza una multiplicación de 4 por 0
calcular(4, 0, "multiplicacion")
 Resultado esperado: el resultado de la multiplicacion es :  0

# Realiza una división de 8 entre 2
calcular(8, 2, "division")
 Resultado esperado: el resultado de la multiplicacion es :  4