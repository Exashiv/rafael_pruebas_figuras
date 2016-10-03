import math


class Figuras:

    def cuadrado(self, lado):
        if(lado < 0):
            return 'no hay distancias negativas'
        try:
            lado = float(lado)
            return lado * lado
        except Exception:
            return 'dato incorrecto'

    def rectangulo(self, base, altura):
        if(base < 0 or altura < 0):
            return 'no hay distancias negativas'
        try:
            altura = float(altura)
            base = float(base)
            return altura * base
        except Exception:
            return 'dato incorrecto'

    def triangulo(self, base, altura):
        if(base < 0 or altura < 0):
            return 'no hay distancias negativas'
        try:
            altura = float(altura)
            base = float(base)
            return (altura * base) / 2
        except Exception:
            return 'dato incorrecto'

    def circulo(self, radio):
        if(radio < 0):
            return 'no hay distancias negativas'
        try:
            radio = float(radio)
            return (math.pi * (radio * radio))
        except Exception:
            return 'dato incorrecto'
