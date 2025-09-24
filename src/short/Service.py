from src.models import LinkShort
from src.utilidades import BibliotecaLink
from random import Random

link_biblioteca = BibliotecaLink()
random = Random()


def number_random():
    return random.randint(1, 54) + 9


def code_link(number_code: int):
    code = ""
    for i in range(0, number_code):
        key = number_random()
        code += link_biblioteca.biblioteca_link.get(str(key), str(key))
    return code


def create_link(link_cli: str, number_code: int):
    return link_cli + code_link(number_code)


class Service:
    def __init__(self):
        self.number_code = 8

    def create_save_link(self, links: LinkShort):
        return create_link(links.cli, self.number_code)
