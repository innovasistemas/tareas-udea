import unittest
import src.triqui as triqui

# Pruebas de caja negra (robustez)
class TestTriquiBlackBox(unittest.TestCase):
    def setUp(self):
        pass


    def test_param_not_list(self):
        with self.assertRaises(TypeError):
            triqui.isBoardFull(9)

        with self.assertRaises(TypeError):
            triqui.isBoardFull("Texto para el tablero")


    def test_empty_board(self):
       """
       Prueba de caja negra (valores límites): lista vacía no cumple
       y debe retornar False
       """
       board_empty = []
       result = triqui.isBoardFull(board_empty) 
       self.assertFalse(result)

    
    def test_out_of_range_movement(self):
        board_empty = ["   "] * 9
        with self.assertRaises(ValueError):
            triqui.isSpaceFree(board_empty, 9)
    
    
    def test_movement_is_not_int(self):
        board_empty = ["   "] * 9
        with self.assertRaises(TypeError):
            triqui.isSpaceFree(board_empty, "centro")

        
if __name__ == "__main__":
    unittest.main()
