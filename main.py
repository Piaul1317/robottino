def destra_avanti():
    global controllo
    if controllo != 1:
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocita)
        controllo = 1
        basic.show_leds("""
            . . # # #
            . . . # #
            . . # . #
            . # . . .
            # . . . .
            """)
def derapata_sinistra():
    global controllo
    if controllo != 4:
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        controllo = 4
        basic.show_leds("""
            # # # . #
            # . . # #
            # . # # #
            . . . . .
            . . . . .
            """)
def sinistra():
    global controllo
    if controllo != 11:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocita - 10)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocita - 10)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita - 10)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita - 10)
        controllo = 11
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
def fermo():
    global controllo
    if controllo != 0:
        controllo = 0
        mecanumRobotV2.state()
        basic.show_leds("""
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            """)
def decrementaVelocita():
    global velocita, controllo, stringaDaVisualizzare
    if controllo != 5:
        velocita += 0 - 5
        controllo = 5
        if velocita < 20:
            velocita = 20
        stringaDaVisualizzare = "" + str(velocita)
def accendiSpegniLed():
    global controllo, luceOn
    if controllo != 15:
        controllo = 15
        if luceOn == 0:
            mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
            mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
            luceOn = 1
        else:
            mecanumRobotV2.set_led(LedCount.LEFT, LedState.OFF)
            mecanumRobotV2.set_led(LedCount.RIGHT, LedState.OFF)
            luceOn = 0
def derapata_destra():
    global controllo
    if controllo != 6:
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        controllo = 6
        basic.show_leds("""
            # . # # #
            # # . . #
            # # # . #
            . . . . .
            . . . . .
            """)
def incrementaVelocita():
    global velocita, controllo, stringaDaVisualizzare
    if controllo != 7:
        velocita += 5
        controllo = 7
        if velocita > 100:
            velocita = 100
        stringaDaVisualizzare = "" + str(velocita)
def shift_destra():
    global controllo
    if controllo != 13:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        controllo = 13
        basic.show_leds("""
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            """)
def sinistra_indietro():
    global controllo
    if controllo != 8:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        controllo = 8
        basic.show_leds("""
            . . . . #
            . . . # .
            # . # . .
            # # . . .
            # # # . .
            """)
def destra_indietro():
    global controllo
    if controllo != 9:
        controllo = 9
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocita)
        basic.show_leds("""
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            """)
def avanti():
    global controllo
    if controllo != 2:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        controllo = 2
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
def sinistra_avanti():
    global controllo
    if controllo != 10:
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        controllo = 10
        basic.show_leds("""
            # # # . .
            # # . . .
            # . # . .
            . . . # .
            . . . . #
            """)
def shift_sinistra():
    global controllo
    if controllo != 12:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        controllo = 12
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            """)
def destra():
    global controllo
    if controllo != 3:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocita - 10)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocita - 10)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita - 10)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita - 10)
        controllo = 3
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
def robot_Indietro():
    global controllo
    if controllo != 14:
        controllo = 14
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
stringaAppoggio = ""
valoreIr2 = 0
controllo = 0
velocita = 0
luceOn = 0
stringaDaVisualizzare = ""
ledDaVisualizzare = 0
luceOn = 0
velocita = 50
irRemote.connect_infrared(DigitalPin.P0)
serial.redirect_to_usb()

def on_forever():
    global valoreIr2
    valoreIr2 = irRemote.return_ir_button()
    serial.write_value("ir", valoreIr2)
    if valoreIr2 == irRemote.ir_button(IrButton.UP):
        avanti()
    elif valoreIr2 == irRemote.ir_button(IrButton.DOWN):
        robot_Indietro()
    elif valoreIr2 == irRemote.ir_button(IrButton.LEFT):
        sinistra()
    elif valoreIr2 == irRemote.ir_button(IrButton.RIGHT):
        destra()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_3):
        shift_destra()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_1):
        shift_sinistra()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_9):
        derapata_destra()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_7):
        derapata_sinistra()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_2):
        destra_avanti()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_4):
        sinistra_avanti()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_6):
        destra_indietro()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_8):
        sinistra_indietro()
    elif valoreIr2 == irRemote.ir_button(IrButton.HASH):
        incrementaVelocita()
    elif valoreIr2 == irRemote.ir_button(IrButton.STAR):
        decrementaVelocita()
    elif valoreIr2 == irRemote.ir_button(IrButton.OK):
        accendiSpegniLed()
    else:
        fermo()
basic.forever(on_forever)

def on_in_background():
    global stringaAppoggio, stringaDaVisualizzare
    if stringaDaVisualizzare != "":
        stringaAppoggio = stringaDaVisualizzare
        stringaDaVisualizzare = ""
        basic.show_string(stringaAppoggio)
control.in_background(on_in_background)
