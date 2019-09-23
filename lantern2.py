import sys
import os
import maestro
import time

from subprocess import Popen

movie1 = ("/home/pi/Videos/T2GS.h264")

servo = maestro.Controller("/dev/ttyACM0")
n = 0
FNULL = open(os.devnull,'w')

servo.setTarget(0,2000)
cmd = "omxplayer --orientation 0 --layer %d %s "%(n,movie1)
Popen(cmd, shell=True, stdout=FNULL,stderr=FNULL)
time.sleep(8)
servo.setTarget(0,4667)
time.sleep(.5)
cmd = "omxplayer --orientation 270 --layer %d %s "%(n,movie1)
Popen(cmd, shell=True, stdout=FNULL,stderr=FNULL)
time.sleep(8)
servo.setTarget(0,7333)
time.sleep(.5)
cmd = "omxplayer --orientation 180 --layer %d %s "%(n,movie1)
Popen(cmd, shell=True, stdout=FNULL,stderr=FNULL)
time.sleep(8)
servo.setTarget(0,10000)
time.sleep(.5)
cmd = "omxplayer --orientation 90 --layer %d %s "%(n,movie1)
Popen(cmd, shell=True, stdout=FNULL,stderr=FNULL)
time.sleep(8)
servo.setTarget(0,7333)
time.sleep(.5)
cmd = "omxplayer --orientation 180 --layer %d %s "%(n,movie1)
Popen(cmd, shell=True, stdout=FNULL,stderr=FNULL)
time.sleep(8)
servo.setTarget(0,4667)
time.sleep(.5)
cmd = "omxplayer --orientation 270 --layer %d %s "%(n,movie1)
Popen(cmd, shell=True, stdout=FNULL,stderr=FNULL)
time.sleep(8)
servo.setTarget(0,2000)
cmd = "omxplayer --orientation 0 --layer %d %s "%(n,movie1)
Popen(cmd, shell=True, stdout=FNULL,stderr=FNULL)
time.sleep(8)


