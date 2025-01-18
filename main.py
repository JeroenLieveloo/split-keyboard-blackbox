print("Starting")

import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.modules.layers import Layers;
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.split import Split, SplitSide
from kmk.modules.holdtap import HoldTap
from kmk.modules.tapdance import TapDance
from storage import getmount
from kmk.extensions.lock_status import LockStatus

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())


keyboard.modules.append(HoldTap())

tapdance = TapDance()
keyboard.modules.append(tapdance)

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
split = Split(
    # data_pin=keyboard.data_pin,  # The primary data pin to talk to the secondary device with
    #uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

if side == SplitSide.LEFT:
    keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP11, board.GP12, board.GP10,)
    flipDisplay = True
else:
    keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10,)
    flipDisplay = False

keyboard.row_pins = (board.GP21, board.GP20, board.GP19, board.GP18,)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.modules.append(split)


# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# Layer toggles
RAISE = KC.MO(1)
NAV = KC.MO(2)

# Homerow mods
HR_A = KC.HT(KC.A, KC.LGUI)
HR_S = KC.HT(KC.S, KC.LALT)
HR_D = KC.HT(KC.D, KC.LCTL)
HR_F = KC.HT(KC.F, KC.LSFT)

HR_SCLN = KC.HT(KC.SCLN, KC.RGUI)
HR_L = KC.HT(KC.L, KC.LALT)
HR_K = KC.HT(KC.K, KC.RCTL)
HR_J = KC.HT(KC.J, KC.RSFT)

HR_LGUI = KC.LGUI
HR_LBRC = KC.HT(KC.LBRC, KC.LALT)
HR_RBRC = KC.HT(KC.RBRC, KC.LCTL)
HR_BSLS = KC.HT(KC.BLSL, KC.LSFT)

HT_TAB = KC.HT(KC.TAB, KC.LALT)
HT_ENT = KC.HT(KC.ENT, KC.LCTL)
HT_SPC = KC.HT(KC.SPACE, KC.LSFT)


# keyboard.keymap = [
#     [   #QWERTY
#         KC.GRV,     KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.MINS,
#         KC.ESC,	    HR_A,		HR_S,		HR_D,		HR_F,		KC.G,           KC.H,       HR_J,       HR_K,       HR_L,       HR_SCLN,    KC.QUOT,
#         KC.CAPS,    KC.Z,       KC.X,		KC.C,		KC.V,		KC.B,           KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.EQL,
#                                             KC.ENT,	    KC.SPACE,	KC.TAB,         KC.BSPC,    RAISE,      KC.DEL,
#     ],
#     [  #RAISE
#         _______,    KC.N1,      KC.N2,		KC.N3,		KC.N4,		KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.PSCR,
#         _______,    HR_LGUI,    HR_LBRC,    HR_RBRC,    HR_BSLS,    _______,        XXXXXXX,    KC.LEFT,    KC.UP,      KC.RIGHT,   XXXXXXX,    KC.INS,
#         _______,    _______,    _______,    _______,    _______,    _______,        KC.MPLY,    XXXXXXX,    KC.DOWN,    XXXXXXX,    XXXXXXX,    XXXXXXX,
#                                             _______,	NAV,	    _______,        _______,    _______,    _______,
#     ],
#     [  #NAV
#         KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6,          KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12, 
#         _______,    _______,    _______,    _______,    _______,    _______,        _______,    KC.HOME,    KC.PGUP,    KC.END,     _______,    _______,
#         _______,    _______,	_______,	_______,	_______,	_______,        _______,    _______,    KC.PGDN,    _______,    _______,    _______,
#                                             _______,	_______,	_______,        _______,    _______,    _______,
#     ],
# ]

keyboard.keymap = [
    [   #QWERTY
        KC.GRV,     KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.MINS,
        KC.ESC,	    KC.A,		KC.S,		KC.D,		KC.F,		KC.G,           KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.CAPS,    KC.Z,       KC.X,		KC.C,		KC.V,		KC.B,           KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.EQL,
                                            HT_ENT,	    HT_SPC,	    HT_TAB,         KC.BSPC,    RAISE,      KC.DEL,
    ],
    [  #RAISE
        _______,   	KC.N1,      KC.N2,		KC.N3,		KC.N4,		KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.PSCR,
        _______,    _______,    KC.LBRC,    KC.RBRC,    KC.BSLS,    _______,        KC.LGUI,    KC.LEFT,    KC.UP,      KC.RIGHT,   NAV,        KC.INS,
        _______,    _______,    _______,    _______,    _______,    _______,        KC.MPLY,    XXXXXXX,    KC.DOWN,    XXXXXXX,    XXXXXXX,    XXXXXXX,
                                            _______,	_______,	_______,        _______,    _______,    _______,
    ],
    [  #NAV
        _______,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,          KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,      
        _______,    _______,    _______,    _______,    _______,    _______,        _______,    KC.HOME,    KC.PGUP,    KC.END,     _______,    KC.F12,
        _______,    _______,	_______,	_______,	_______,	_______,        _______,    _______,    KC.PGDN,    _______,    _______,    _______,
                                            _______,	_______,	_______,        _______,    _______,    _______,
    ],
]

lockStatus = LockStatus().get_caps_lock == True
keyboard.extensions.append(lockStatus)

class DisplayLockStatus(LockStatus):
    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            oled_ext = get_display(self.get_caps_lock())

def get_display(isCapsOn):

    oledData = OledData(
        corner_one = {0:OledReactionType.STATIC, 1:["   LAYER"]},
        corner_two = {0:OledReactionType.LAYER, 1:["BASE", "RAISE", "NAV"]},
        corner_three = {0:OledReactionType.STATIC, 1:["   CAPS"]},
        corner_four = {0:OledReactionType.STATIC, 1:["ON" if isCapsOn else "OFF"]},
        )

    return Oled(
        oledData,
        toDisplay = OledDisplayMode.TXT,
        oWidth=128,
        oHeight=32,
        flip = flipDisplay,
        )
    

oled_ext = get_display(False)


# KC.CAPS.after_press_handler(set_CAPS_display)

keyboard.extensions.append(oled_ext)
# keyboard.extensions.append(DisplayLockStatus())
if __name__ == '__main__':
    keyboard.go()

 # type: ignore