import re     #para trabajar con subcadenas 
from typing import Dict

def do_math(numbers_string: str) -> int:
    numbers = numbers_string.split()    #Utilizamos el metodo split para separar la cadena de entrada en una lista de números utilizando el espacio como separador.     
    letters_dict = {}
    for number in numbers:
        letter = re.search("[a-zA-Z]", number).group()#Utilizamos el metodo search para buscar la primera ocurrencia de una letra en el número.
        int_number = int(''.join(filter(str.isdigit, number))) 
        if letter in letters_dict:
            letters_dict[letter].append(int_number)
        else:
            letters_dict[letter] = [int_number]

    sorted_numbers = [number for letter in sorted(letters_dict) for number in letters_dict[letter]]

    result = sorted_numbers[0]
    for i in range(1, len(sorted_numbers)):
        result = result + sorted_numbers[i]
        result = result - sorted_numbers[i]
        result = result * sorted_numbers[i]
        result = result / sorted_numbers[i]

    return round(result)
do_math("24z6 1x23 y369 89a 900b")







