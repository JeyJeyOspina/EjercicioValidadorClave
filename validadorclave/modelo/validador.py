from validadorclave.modelo.errores import ValidadorError
from abc import  ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    @abstractmethod
    def es_valida(self):
        pass

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

class ReglaValidacionGanimedes(ReglaValidacion):

    def es_valida(self):
        pass

    def contiene_caracter_especial(self, clave: str):

        caracteres_especiales: list[str] = ["@", "_", "#", "$", "%"]

        for caracter in clave:
            if caracter in caracteres_especiales:
                return True
        return False

    def contiene_calisto(self, clave):

        cantidad_mayusculas: int = 0

        for caracter in clave:
            if caracter.isupper():
                cantidad_mayusculas += 1
        if  2 <= cantidad_mayusculas < len(clave):
            return True

