function destra_avanti () {
    if (controllo != 1) {
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocita)
        controllo = 1
        basic.showLeds(`
            . . # # #
            . . . # #
            . . # . #
            . # . . .
            # . . . .
            `)
    }
}
function derapata_sinistra () {
    if (controllo != 4) {
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        controllo = 4
        basic.showLeds(`
            # # # . #
            # . . # #
            # . # # #
            . . . . .
            . . . . .
            `)
    }
}
function sinistra () {
    if (controllo != 11) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocitaRotazione)
        controllo = 11
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    }
}
function fermo () {
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
function decrementaVelocita () {
    if (controllo != 5) {
        velocita += 0 - 5
        controllo = 5
        if (velocita < 20) {
            velocita = 20
        }
        basic.showString("" + velocita)
    }
}
function accendiSpegniLed () {
    if (controllo != 15) {
        controllo = 15
        if (luceOn == 0) {
            mecanumRobotV2.setLed(LedCount.Left, LedState.ON)
            mecanumRobotV2.setLed(LedCount.Right, LedState.ON)
            luceOn = 1
            basic.showString("LED ON")
        } else {
            mecanumRobotV2.setLed(LedCount.Left, LedState.OFF)
            mecanumRobotV2.setLed(LedCount.Right, LedState.OFF)
            luceOn = 0
            basic.showString("LED OFF")
        }
    }
}
function derapata_destra () {
    if (controllo != 6) {
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        controllo = 6
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
    if (controllo != 7) {
        velocita += 5
        controllo = 7
        if (velocita > 100) {
            velocita = 100
        }
        basic.showString("" + velocita)
    }
}
function shift_destra () {
    if (controllo != 13) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        controllo = 13
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            `)
    }
}
function sinistra_indietro () {
    if (controllo != 8) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        controllo = 8
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
    if (controllo != 9) {
        controllo = 9
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocita)
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            `)
    }
}
function avanti () {
    if (controllo != 2) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
        controllo = 2
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    }
}
function sinistra_avanti () {
    if (controllo != 10) {
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        controllo = 10
        basic.showLeds(`
            # # # . .
            # # . . .
            # . # . .
            . . . # .
            . . . . #
            `)
    }
}
function shift_sinistra () {
    if (controllo != 12) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        controllo = 12
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            `)
    }
}
function destra () {
    if (controllo != 3) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocitaRotazione)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocitaRotazione)
        controllo = 3
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    }
}
function robot_Indietro () {
    if (controllo != 14) {
        controllo = 14
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    }
}
let valoreIr2 = 0
let controllo = 0
let velocitaRotazione = 0
let velocita = 0
let luceOn = 0
let ledDaVisualizzare = 0
luceOn = 0
velocita = 50
velocitaRotazione = 40
irRemote.connectInfrared(DigitalPin.P0)
serial.redirectToUSB()
basic.forever(function () {
    valoreIr2 = irRemote.returnIrButton()
    serial.writeValue("ir", valoreIr2)
    if (valoreIr2 == irRemote.irButton(IrButton.Up)) {
        avanti()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Down)) {
        robot_Indietro()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Left)) {
        sinistra()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Right)) {
        destra()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_3)) {
        shift_destra()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_1)) {
        shift_sinistra()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_9)) {
        derapata_destra()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_7)) {
        derapata_sinistra()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_2)) {
        destra_avanti()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_4)) {
        sinistra_avanti()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_6)) {
        destra_indietro()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Number_8)) {
        sinistra_indietro()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Hash)) {
        incrementaVelocita()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Star)) {
        decrementaVelocita()
    } else if (valoreIr2 == irRemote.irButton(IrButton.Ok)) {
        accendiSpegniLed()
    } else {
        fermo()
    }
})
