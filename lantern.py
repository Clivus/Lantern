import maestro
servo = maestro.Controller(ttyStr='/dev/ttySO')
servo.setTarget(0,2500)
