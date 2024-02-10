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
def robot_Avanti():
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
def robot_destra():
    global controllo
    if controllo != 3:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocitaRotazione)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocitaRotazione)
        controllo = 3
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
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
def decrementaVelocita():
    global velocita, controllo
    if controllo != 5:
        velocita += 0 - 5
        controllo = 5
        if velocita < 20:
            velocita = 20
        basic.show_string("" + str(velocita))
def robot_Ferma():
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
    global velocita, controllo
    if controllo != 7:
        velocita += 5
        controllo = 7
        if velocita > 100:
            velocita = 100
        basic.show_string("" + str(velocita))
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
def robot_sinistra():
    global controllo
    if controllo != 11:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocitaRotazione)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocitaRotazione)
        controllo = 11
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
def robot_ShiftSinistra():
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
def robot_ShiftDestra():
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
def accendiSpegni():
    global controllo, luceOn
    if controllo != 15:
        controllo = 15
        if luceOn == 0:
            mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
            mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
            luceOn = 1
            basic.show_string("LED ON")
        else:
            mecanumRobotV2.set_led(LedCount.LEFT, LedState.OFF)
            mecanumRobotV2.set_led(LedCount.RIGHT, LedState.OFF)
            luceOn = 0
            basic.show_string("LED OFF")
valoreIr2 = 0
controllo = 0
velocitaRotazione = 0
velocita = 0
luceOn = 0
luceOn = 0
velocita = 50
velocitaRotazione = 40
ledDaVisualizzare = 0
irRemote.connect_infrared(DigitalPin.P0)
serial.redirect_to_usb()

def on_forever():
    global valoreIr2
    valoreIr2 = irRemote.return_ir_button()
    serial.write_value("ir", valoreIr2)
    if valoreIr2 == irRemote.ir_button(IrButton.UP):
        robot_Avanti()
    elif valoreIr2 == irRemote.ir_button(IrButton.DOWN):
        robot_Indietro()
    elif valoreIr2 == irRemote.ir_button(IrButton.LEFT):
        robot_sinistra()
    elif valoreIr2 == irRemote.ir_button(IrButton.RIGHT):
        robot_destra()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_3):
        robot_ShiftDestra()
    elif valoreIr2 == irRemote.ir_button(IrButton.NUMBER_1):
        robot_ShiftSinistra()
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
        accendiSpegni()
    else:
        robot_Ferma()
basic.forever(on_forever)
