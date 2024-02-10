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
function robot_sinistra () {
    if (controllo != 68) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, velocita)
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
function robot_destra () {
    if (controllo != 67) {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, velocita)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, velocita)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, velocita)
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
let controllo = 0
let velocita = 0
velocita = 50
controllo = 0
serial.redirectToUSB()
irRemote.connectInfrared(DigitalPin.P0)
basic.forever(function () {
    serial.writeValue("tasto", irRemote.returnIrButton())
    if (irRemote.returnIrButton() == 70) {
        robot_Avanti()
    } else if (irRemote.returnIrButton() == 21) {
        robot_Indietro()
    } else if (irRemote.returnIrButton() == 68) {
        robot_sinistra()
    } else if (irRemote.returnIrButton() == 67) {
        robot_destra()
    } else if (irRemote.returnIrButton() == 13) {
        robot_ShiftDestra()
    } else if (irRemote.returnIrButton() == 22) {
        robot_ShiftSinistra()
    } else {
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
})
