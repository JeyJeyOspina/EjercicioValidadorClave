from validadorclave.modelo.errores import ValidadorError
from abc import  ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    @abstractmethod
    def es_valida(self):
        pass




