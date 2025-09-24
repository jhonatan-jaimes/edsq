import random

from src.utilidades import BibliotecasEncode
from src.models import Message

biblioteca = BibliotecasEncode()


def code_random():
    num_random = random.randint(1, 166)
    return num_random + 110


def caracter_to_code(array_caracter: list[str]):
    array_code: list[str] = []
    for i in array_caracter:
        if i in biblioteca.caracter_to_code:
            array_code.append(biblioteca.caracter_to_code[i])
        else:
            raise RuntimeError(f"Caracter no encontrado: {i}")
    return array_code


def code_to_number(array_code: list[str]):
    array_numb: list[str] = []
    for i in array_code:
        lista = list(i)
        for j in lista:
            num = biblioteca.code_to_number[j]
            array_numb.append(num)
    return array_numb


def number_to_caracter(array_numb: list[str]):
    codigo = code_random()
    array_char: list[str] = []
    for n in array_numb:
        numero = int(n) * codigo
        str_nu = str(numero)
        pri_par = str_nu[0:2]
        seg_par = str_nu[2:4]
        array_char.append(biblioteca.number_to_caracter.get(pri_par, pri_par))
        array_char.append(biblioteca.number_to_caracter.get(seg_par, seg_par))
    return array_char


def encode_clean(array_char: list[str]):
    encode = ""
    for i in array_char:
        encode += i
    return encode


class Service:
    def encode_text(self, text_to_encode: Message):
        array_caracter = list(text_to_encode.text)
        array_code = caracter_to_code(array_caracter)
        array_numb = code_to_number(array_code)
        array_char = number_to_caracter(array_numb)
        encode = encode_clean(array_char)
        return encode
