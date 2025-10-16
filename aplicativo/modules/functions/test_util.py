import unittest as uni
from util import validarEntradas

class TestArea(uni.TestCase):
    def test_validarNomeSobrenome(self):
        print('Teste de nome')
        
        self.assertAlmostEqual(validarEntradas('Lucas02', 'Melo', 'Email@123'), False)
        
        print('teste de sobrenome')
        self.assertAlmostEqual(validarEntradas('Lucas', 'Mel0', 'Email@123'), False)
        
    def test_validarEmail(self):
        print('Teste Email')
        self.assertAlmostEqual(validarEntradas('Lucas', 'Melo', 'Email123'), False)
        
        