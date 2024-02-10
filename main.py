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
controllo = 0
velocita = 0
velocita = 50
velocitaRotazione = 20
irRemote.connect_infrared(DigitalPin.P0)

def on_forever():
    if irRemote.return_ir_button() == 70:
        robot_Avanti()
    elif irRemote.return_ir_button() == 21:
        robot_Indietro()
    elif irRemote.return_ir_button() == 68:
        robot_sinistra()
    elif irRemote.return_ir_button() == 67:
        robot_destra()
    elif irRemote.return_ir_button() == 13:
        robot_ShiftDestra()
    elif irRemote.return_ir_button() == 22:
        robot_ShiftSinistra()
    else:
        robot_Ferma()
basic.forever(on_forever)
