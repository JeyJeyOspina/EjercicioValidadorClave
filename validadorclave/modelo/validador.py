from validadorclave.modelo.errores import ValidadorError
from abc import  ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    @abstractmethod
    def es_valida(self):
        pass

    def _validar_longitud(self, clave: str) -> bool:
        ...

    def _contiene_mayuscula(self, clave: str) -> bool:
        ...

    def _contiene_minuscula(self, clave: str) -> bool:
        ...

    def _contiene_numero(self, clave: str) -> bool:
        ...




