import unittest
from figuras import Figuras


class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.figuras = Figuras()

    def test_area_cuadrado_lado_5(self):
        resultado = self.figuras.cuadrado(5)
        self.assertEqual(25, resultado)

    def test_area_cuadrado_lado_6(self):
        resultado = self.figuras.cuadrado(6)
        self.assertEqual(36, resultado)

    def test_area_cuadrado_lado_g(self):
        resultado = self.figuras.cuadrado('g')
        self.assertEqual('dato incorrecto', resultado)

    def test_area_cuadrado_lado_4punto5(self):
        resultado = self.figuras.cuadrado(4.5)
        self.assertEqual(20.25, resultado)

    def test_area_cuadrado_lado_0(self):
        resultado = self.figuras.cuadrado(0)
        self.assertEqual(0, resultado)

    def test_area_cuadrado_lado_12(self):
        resultado = self.figuras.cuadrado(12)
        self.assertEqual(144, resultado)

    def test_area_cuadrado_lado_neg1(self):
        resultado = self.figuras.cuadrado(-1)
        self.assertEqual('no hay distancias negativas', resultado)

    def test_area_rectangulo_base_5_altura_7(self):
        resultado = self.figuras.rectangulo(5, 7)
        self.assertEqual(35, resultado)

    def test_area_rectangulo_base_6_altura_12(self):
        resultado = self.figuras.rectangulo(6, 12)
        self.assertEqual(72, resultado)

    def test_area_rectangulo_base_a_altura_80(self):
        resultado = self.figuras.rectangulo('a', 80)
        self.assertEqual('dato incorrecto', resultado)

    def test_area_rectangulo_base_5punto1_altura_7punto9(self):
        resultado = self.figuras.rectangulo(5.1, 7.9)
        self.assertEqual(40.29, resultado)

    def test_area_rectangulo_base_neg1_altura_7(self):
        resultado = self.figuras.rectangulo(-1, 7)
        self.assertEqual('no hay distancias negativas', resultado)

    def test_area_triangulo_base_5_altura_7(self):
        resultado = self.figuras.triangulo(5, 7)
        self.assertEqual(17.5, resultado)

    def test_area_triangulo_base_neg5_altura_neg7(self):
        resultado = self.figuras.triangulo(-5, -7)
        self.assertEqual('no hay distancias negativas', resultado)

    def test_area_triangulo_base_6_altura_12(self):
        resultado = self.figuras.triangulo(6, 12)
        self.assertEqual(36, resultado)

    def test_area_triangulo_base_a_altura_80(self):
        resultado = self.figuras.triangulo('a', 80)
        self.assertEqual('dato incorrecto', resultado)

    def test_area_triangulo_base_5punto1_altura_7punto9(self):
        resultado = self.figuras.triangulo(5.1, 7.9)
        self.assertEqual(20.145, resultado)

    def test_area_triangulo_base_neg9_altura_neg7(self):
        resultado = self.figuras.triangulo(-9, -7)
        self.assertEqual('no hay distancias negativas', resultado)

    def test_area_circulo_radio_5(self):
        resultado = self.figuras.circulo(5)
        self.assertEqual(78.53981633974483, resultado)

    def test_area_circulo_radio_2(self):
        resultado = self.figuras.circulo(2)
        self.assertEqual(12.566370614359172, resultado)

    def test_area_circulo_radio_g(self):
        resultado = self.figuras.circulo('g')
        self.assertEqual('dato incorrecto', resultado)

    def test_area_circulo_radio_5punto1(self):
        resultado = self.figuras.circulo(5.1)
        self.assertEqual(81.71282491987051, resultado)

    def test_area_circulo_radio_neg3(self):
        resultado = self.figuras.circulo(-3)
        self.assertEqual('no hay distancias negativas', resultado)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
