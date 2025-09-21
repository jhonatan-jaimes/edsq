from src.utilidades import BibliotecasEncode
from src.models import Message

biblioteca = BibliotecasEncode()

def caracter_to_code(array_caracter: list[str]):
    array_code: list[str] = []
    for i in array_caracter:
        if i in biblioteca.caracter_to_code:
            array_code.append(biblioteca.caracter_to_code[i])
        else:
            raise RuntimeError(f"Caracter no encontrado: {i}")
    return array_code

class Service:
    def encode_text(self, text_to_encode: Message):
        array_caracter = list(text_to_encode.text)
        array_code = caracter_to_code(array_caracter)
        return array_code