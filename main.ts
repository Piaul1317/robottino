function destra_avanti () {
    if (controllo != 25) {
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocita)
        controllo = 25
        basic.showLeds(`
            . . # # #
            . . . # #
            . . # . #
            . # . . .
            # . . . .
            `)
    }
}
function robot_Avanti () {
    if (controllo != 70) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        controllo = 70
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    }
}
function robot_destra () {
    if (controllo != 67) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocitaRotazione)
        controllo = 67
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    }
}
function derapata_sinistra () {
    if (controllo != 90) {
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        controllo = 90
        basic.showLeds(`
            # # # . #
            # . . # #
            # . # # #
            . . . . .
            . . . . .
            `)
    }
}
function decrementaVelocita () {
    if (controllo != 101) {
        velocita += -5
        controllo = 101
        if (velocita < 20) {
            velocita = 20
        }
        basic.showString("" + velocita)
    }
}
function robot_Ferma () {
    if (controllo != 0) {
        controllo = 0
        mecanumRobotV2.state()
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            `)
    }
}
function derapata_destra () {
    if (controllo != 8) {
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        controllo = 8
        basic.showLeds(`
            # . # # #
            # # . . #
            # # # . #
            . . . . .
            . . . . .
            `)
    }
}
function incrementaVelocita () {
    if (controllo != 100) {
        velocita += 5
        controllo = 100
        if (velocita > 100) {
            velocita = 100
        }
        basic.showString("" + velocita)
    }
}
function sinistra_indietro () {
    if (controllo != 94) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        controllo = 94
        basic.showLeds(`
            . . . . #
            . . . # .
            # . # . .
            # # . . .
            # # # . .
            `)
    }
}
function destra_indietro () {
    if (controllo != 28) {
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocita)
        controllo = 28
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            `)
    }
}
function sinistra_avanti () {
    if (controllo != 12) {
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        controllo = 12
        basic.showLeds(`
            # # # . .
            # # . . .
            # . # . .
            . . . # .
            . . . . #
            `)
    }
}
function robot_sinistra () {
    if (controllo != 68) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocitaRotazione)
        controllo = 68
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    }
}
function robot_ShiftSinistra () {
    if (controllo != 13) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        controllo = 13
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            `)
    }
}
function robot_ShiftDestra () {
    if (controllo != 22) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        controllo = 22
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            `)
    }
}
function robot_Indietro () {
    if (controllo != 21) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        controllo = 21
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    }
}
let valoreIr = 0
let controllo = 0
let velocitaRotazione = 0
let velocita = 0
velocita = 50
velocitaRotazione = 20
irRemote.connectInfrared(DigitalPin.P0)
serial.redirectToUSB()
basic.forever(function () {
    valoreIr = irRemote.returnIrButton()
    serial.writeValue("ir", valoreIr)
    if (valoreIr == irRemote.irButton(IrButton.Up)) {
        robot_Avanti()
    } else if (valoreIr == irRemote.irButton(IrButton.Down)) {
        robot_Indietro()
    } else if (valoreIr == 68) {
        robot_sinistra()
    } else if (valoreIr == 67) {
        robot_destra()
    } else if (valoreIr == 13) {
        robot_ShiftDestra()
    } else if (valoreIr == 22) {
        robot_ShiftSinistra()
    } else if (valoreIr == 90) {
        derapata_destra()
    } else if (valoreIr == 8) {
        derapata_sinistra()
    } else if (valoreIr == 25) {
        destra_avanti()
    } else if (valoreIr == 12) {
        sinistra_avanti()
    } else if (valoreIr == 94) {
        destra_indietro()
    } else if (valoreIr == 28) {
        sinistra_indietro()
    } else if (valoreIr == irRemote.irButton(IrButton.Hash)) {
        incrementaVelocita()
    } else if (valoreIr == irRemote.irButton(IrButton.Star)) {
        decrementaVelocita()
    } else {
        robot_Ferma()
    }
})
