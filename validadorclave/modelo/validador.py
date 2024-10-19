from validadorclave.modelo.errores import ValidadorError, NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError
from abc import  ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool :
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

    def __init__(self):
        super().__init__(8)

    def es_valida(self, clave: str) -> bool:

        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError
        else:
            return True


    def contiene_caracter_especial(self, clave: str) -> bool:

        caracteres_especiales: list[str] = ["@", "_", "#", "$", "%"]

        for caracter in clave:
            if caracter in caracteres_especiales:
                return True
        return False

class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(6)

    def es_valida(self, clave: str) -> bool:

        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError
        return True

    def contiene_calisto(self, clave: str) -> bool:

        cantidad_mayusculas: int = 0

        for caracter in clave:
            if caracter.isupper():
                cantidad_mayusculas += 1
        if  2 <= cantidad_mayusculas < len(clave) and clave.lower() == "calisto":
            return True
        return False