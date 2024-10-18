# Arithmetic Operators

## Variables are declared
number1 = 10
number2 = 5
number3 = 10

# # Addition(suma +)
result_addition = number1 + number2  # 10 + 5 = 15
#print(f"El resultado de number1 + number2 ({number1} + {number2}) es {result_addition}")


## subtraction (resta -)
result_subtraction = number2 - number1  # 5 - 10 = -5
#print(f"El resultado de number2 - number1 ({number2} - {number1}) es {result_subtraction}")


## Multiply (multiplicación *)
result_multiply = number1 * number2  # 10 * 5 = 50
#print(f"El resultado de number1 * number2 ({number1} * {number2}) es {result_multiply}")


## split (división /)
result_split = number1 / number2  # 10 / 5 = 2.0
#print(f"El resultado de number1 / number2 ({number1} / {number2}) es {result_split}")


## Integer division (división entera) //
result_integer_division = number1 // 3  # 10 / 3 = 3.3333, but the result es 3, only take integer part (3)
#print(f"El resultado de number1 // 3 ({number1} // 3) es {result_integer_division}")



# <------------------------------- // ------------------------------->
# Comparison Operators

## Equal to == (igual a)
result_operation_equal = number1 == number2  # 10 == 5, False
result_operation_equal2 = number1 == number3  # 10 == 10, True
# print(f"Resultado de la operacion {number1} == {number2} es: ({result_operation_equal})")
# print(f"Resultado de la operacion {number1} == {number3} es: ({result_operation_equal2})")

## Different != (diferente de)
result_operation_different = number1 != number2  # 10 != 5, True
result_operation_different2 = number1 != number3  # 10 != 10, False
# print(f"Resultado de la operacion {number1} != {number2} es: ({result_operation_different})")
# print(f"Resultado de la operacion {number1} != {number3} es: ({result_operation_different2})")

## Greater than > (mayor que)
result_operation_more_than = number1 > number2  # 10 > 5, True
result_operation_more_than2 = number1 > number3  # 10 > 10, False
# print(f"Resultado de la operacion {number1} > {number2} es: ({result_operation_more_than})")
# print(f"Resultado de la operacion {number1} > {number3} es: ({result_operation_more_than2})")

## Less than < (menor que)
result_operation_less_than = number1 < number2  # 10 < 5, False
result_operation_less_than2 = number1 < number3  # 10 < 10, False
# print(f"Resultado de la operacion {number1} < {number2} es: ({result_operation_less_than})")
# print(f"Resultado de la operacion {number1} < {number3} es: ({result_operation_less_than2})")

## Greater than or equal to >= (mayor o igual que)
result_operation_greater_or_equal = number1 >= number2  # 10 >= 5, True
result_operation_greater_or_equal2 = number1 >= number3  # 10 >= 10, True
# print(f"Resultado de la operacion {number1} >= {number2} es: ({result_operation_greater_or_equal})")
# print(f"Resultado de la operacion {number1} >= {number3} es: ({result_operation_greater_or_equal2})")

## Less than or equal to <= (menor o igual que)
result_operation_less_or_equal = number1 <= number2  # 10 <= 5, False
result_operation_less_or_equal2 = number1 <= number3  # 10 <= 10, True
# print(f"Resultado de la operacion {number1} <= {number2} es: ({result_operation_less_or_equal})")
# print(f"Resultado de la operacion {number1} <= {number3} es: ({result_operation_less_or_equal2})")



# <------------------------------- // ------------------------------->
# Logical Operators

# variables are declared
verdadero = True
falso = False


## And 'and' (Y)
result_operation_and = verdadero and verdadero  # True and True = True
result_operation_and2 = verdadero and falso  # True and falso = Falso
# print(f"Resultado de la operacion {verdadero} and {verdadero} es: ({result_operation_and})")
# print(f"Resultado de la operacion {verdadero} and {falso} es: ({result_operation_and2})")


## Or 'or' (O)
result_operation_or = verdadero or verdadero  # True and True = True
result_operation_or2 = verdadero or falso  # True and falso = True
# print(f"Resultado de la operacion {verdadero} or {verdadero} es: ({result_operation_or})")
# print(f"Resultado de la operacion {verdadero} or {falso} es: ({result_operation_or2})")


## Not 'not' (no)
result_operation_not = not verdadero  # True --> False
result_operation_not2 = not falso # False --> True
# print(f"Resultado de la operacion not {verdadero} es: ({result_operation_not})")
# print(f"Resultado de la operacion not {falso} es: ({result_operation_not2})")


