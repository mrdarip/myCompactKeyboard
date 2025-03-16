from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()
keyboard.col_pins = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 26, 27)
keyboard.row_pins = (2, 3, 4, 5, 6, 7, 8, 9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

keyboard.keymap = [
    # Layer 0
    [
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.QUES, KC.EXLM,
        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC,
        KC.NUBS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.SCLN, KC.COLN, KC.MINS, KC.ME,
        KC.GRAVE, KC.SPACE, KC.GRAVE, KC.MENU, KC.LCTL, KC.HOME, KC.END, KC.ESC, KC.ROT, KC.ROT, KC.X, KC.N1,
        KC.TAB, KC.SPACE, KC.FN, KC.LALT, KC.TA, KC.UP, KC.META, KC.LEFT, KC.PSCR, KC.PGUP, KC.Y, KC.N2,
        KC.CAPS, KC.LSFT, KC.LCTL, KC.LGUI, KC.LEFT, KC.DOWN, KC.RIGHT, KC.ENT, KC.DEL, KC.PGDN, KC.Z, KC.N3,
    ],
    # Layer 1
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11,
        KC.F12, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS,
        KC.EQL, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLS,
        KC.DEL, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPACE, KC.RALT, KC.RGUI, KC.APP, KC.RCTL, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT,
    ],
]

if __name__ == '__main__':
    keyboard.go()