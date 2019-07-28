import Rpi.GPIO as GPIO
import sys
import os
import time #example time.sleep(1)
import maestro

from subprocess import Popen

'''	Setup Servo connection to Maestro '''
servo = maestro.Controller("/dev/ttyACM0")

'''	Setup GPIO pins on the Raspberry Pi '''
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

'''	Set up movie locations and names '''	
movie1 = ("/home/pi/Videos/movie1.mp4")
movie2 = ("/home/pi/Videos/movie2.mp4")
movie3 = ("/home/pi/Videos/movie3.mp4")
movie4 = ("/home/pi/Videos/movie4.mp4")

'''	Set up state variables for the videos and GPIO pins '''
last_state1 = True
last_state2 = True
last_state3 = True
last_state4 = True

input_state1 = True
input_state2 = True
input_state3 = True
input_state4 = True

quit_video = True

rotation = [2000,4667,7333,10000]

''' Main loop '''
while True:
	'''Read states of inputs'''
	input_state1 = GPIO.input(14)
	input_state2 = GPIO.input(15)
	input_state3 = GPIO.input(18)
	input_state4 = GPIO.input(23)
	quit_video = GPIO.input(24)

	'''If input 1 detects movement'''
	if input_state1 != last_state1:
		if (player and not input_state1):
                        servo.setTarget(0,rotation[0])
			os.system('killall omxplayer.bin')
			omxc = Popen(['omxplayer', '-b', movie1])
			player = True
		elif not input_state1:
                        servo.setTarget(0,rotation[0])			
                        omxc = Popen(['omxplayer', '-b', movie1])
			player = True
	
	'''If input 2 detects movement'''
	elif input_state2 != last_state2:
		if (player and not input_state2):
                        servo.setTarget(0,4667)
			os.system('killall omxplayer.bin')
			omxc = Popen(['omxplayer', '-b', movie2])
			player = True
		elif not input_state2:
                        servo.setTarget(0,4667)
			omxc = Popen(['omxplayer', '-b', movie2])
			player = True
	'''If input 3 detects movement'''	
	elif input_state3 != last_state3:
		if (player and not input_state2):
                        servo.setTarget(0,7333)
			os.system('killall omxplayer.bin')
			omxc = Popen(['omxplayer', '-b', movie3])
			player = True
		elif not input_state3:
                        servo.setTarget(0,7333)
			omxc = Popen(['omxplayer', '-b', movie3])
			player = True
	'''If input 4 detects movement'''
	elif input_state4 != last_state4:
		if (player and not input_state4):
                        servo.setTarget(0,10000)
			os.system('killall omxplayer.bin')
			omxc = Popen(['omxplayer', '-b', movie4])
			player = True
		elif not input_state4:
                        servo.setTarget(0,10000)
			omxc = Popen(['omxplayer', '-b', movie4])
			player = True
	
	'''If omxplayer is running and GPIO pins are NOT shorted to ground'''
	elif (player and input_state1 and input_state2 and input_state3 and input_state4):
		os.system('killall omxplayer.bin')
		player = False

	'''GPIO(24) to close omxplayer manually - used during debug'''
	if quit_video == False:
		os.system('killall omxplayer.bin')
		player = False

	'''Set last_input states'''
	last_state1 = input_state1
	last_state2 = input_state2 
	last_state3 = input_state3
	last_state4 = input_state4
	'''' unnecessa
	
