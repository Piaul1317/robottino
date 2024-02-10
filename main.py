def destra_avanti():
    global controllo
    if controllo != 25:
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocita)
        controllo = 25
        basic.show_leds("""
            . . # # #
            . . . # #
            . . # . #
            . # . . .
            # . . . .
            """)
def robot_Avanti():
    global controllo
    if controllo != 70:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        controllo = 70
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
def robot_destra():
    global controllo
    if controllo != 67:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocitaRotazione)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocitaRotazione)
        controllo = 67
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
def derapata_sinistra():
    global controllo
    if controllo != 90:
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        controllo = 90
        basic.show_leds("""
            # # # . #
            # . . # #
            # . # # #
            . . . . .
            . . . . .
            """)
def decrementaVelocita():
    global velocita, controllo
    if controllo != 101:
        velocita += -5
        controllo = 101
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
    if controllo != 8:
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        controllo = 8
        basic.show_leds("""
            # . # # #
            # # . . #
            # # # . #
            . . . . .
            . . . . .
            """)
def incrementaVelocita():
    global velocita, controllo
    if controllo != 100:
        velocita += 5
        controllo = 100
        if velocita > 100:
            velocita = 100
        basic.show_string("" + str(velocita))
def sinistra_indietro():
    global controllo
    if controllo != 94:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        controllo = 94
        basic.show_leds("""
            . . . . #
            . . . # .
            # . # . .
            # # . . .
            # # # . .
            """)
def destra_indietro():
    global controllo
    if controllo != 28:
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocita)
        controllo = 28
        basic.show_leds("""
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            """)
def sinistra_avanti():
    global controllo
    if controllo != 12:
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        controllo = 12
        basic.show_leds("""
            # # # . .
            # # . . .
            # . # . .
            . . . # .
            . . . . #
            """)
def robot_sinistra():
    global controllo
    if controllo != 68:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocitaRotazione)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocitaRotazione)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocitaRotazione)
        controllo = 68
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
def robot_ShiftSinistra():
    global controllo
    if controllo != 13:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        controllo = 13
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            """)
def robot_ShiftDestra():
    global controllo
    if controllo != 22:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, velocita)
        controllo = 22
        basic.show_leds("""
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            """)
def robot_Indietro():
    global controllo
    if controllo != 21:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, velocita)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, velocita)
        controllo = 21
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
valoreIr = 0
controllo = 0
velocitaRotazione = 0
velocita = 0
velocita = 50
velocitaRotazione = 20
irRemote.connect_infrared(DigitalPin.P0)
serial.redirect_to_usb()

def on_forever():
    global valoreIr
    valoreIr = irRemote.return_ir_button()
    serial.write_value("ir", valoreIr)
    if valoreIr == irRemote.ir_button(IrButton.UP):
        robot_Avanti()
    elif valoreIr == irRemote.ir_button(IrButton.DOWN):
        robot_Indietro()
    elif valoreIr == 68:
        robot_sinistra()
    elif valoreIr == 67:
        robot_destra()
    elif valoreIr == 13:
        robot_ShiftDestra()
    elif valoreIr == 22:
        robot_ShiftSinistra()
    elif valoreIr == 90:
        derapata_destra()
    elif valoreIr == 8:
        derapata_sinistra()
    elif valoreIr == 25:
        destra_avanti()
    elif valoreIr == 12:
        sinistra_avanti()
    elif valoreIr == 94:
        destra_indietro()
    elif valoreIr == 28:
        sinistra_indietro()
    elif valoreIr == irRemote.ir_button(IrButton.HASH):
        incrementaVelocita()
    elif valoreIr == irRemote.ir_button(IrButton.STAR):
        decrementaVelocita()
    else:
        robot_Ferma()
basic.forever(on_forever)


