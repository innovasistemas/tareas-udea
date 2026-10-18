import unittest
import src.triqui as triqui

# Pruebas de caja blanca
class TestWhiteBox(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_board_full(self):
        '''
        Simular camino donde se cumple la condición: tablero lleno 
        9 posiciones ocupadas: se espera True
        '''
        board_full = [" X ", " O ", " X ", " X ", " O ", " X ", " O ", " X ", " O "]
        result = triqui.isBoardFull(board_full)
        self.assertTrue(result)

       
    def test_is_space_free(self):
        board_half_full = [" X ", "   ", " X ", " X ", "   ", " X ", " O ", " X ", " O "]
        result = triqui.isSpaceFree(board_half_full, 1)
        self.assertTrue(result)
        
        
    def test_is_not_space_free(self):
        board_half_full = [" X ", "   ", " X ", " X ", "   ", " X ", " O ", " X ", " O "]
        result = triqui.isSpaceFree(board_half_full, 0)
        self.assertFalse(result)

