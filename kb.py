import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=DiodeOrientation.ROW2COL,
                interval=0.02,
                max_events=64,
            ),
        ]
    row_pins = (board.GP21, board.GP20, board.GP19, board.GP18,)
    col_pins = (board.GP15, board.GP14, board.GP13, board.GP11, board.GP12, board.GP10,)
    
    SCL = board.GP9
    SDA = board.GP8
    data_pin = board.GP0
    
    coord_mapping = [
        0,  1,  2,  3,  4,  5,      29, 28, 27, 26, 25, 24,
        6,  7,  8,  9,  10, 11,     35, 34, 33, 32, 31, 30,
        12, 13, 14, 15, 16, 17,     41, 40, 39, 38, 37, 36,
                    21, 22, 23,     47, 46, 45,]
