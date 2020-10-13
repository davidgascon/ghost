## screenshotter
# Used to take screen shots of a region and save to a folder

try:
	from tkinter import *
except:
	print("tkinter not installed.")
	exit()

try:
	import tkfilebrowser
except:
	print("tkfilebrowser not installed.")
	exit()

try:
	import keyboard
except:
	print("keyboard not installed.")
	exit()

try:
	import pyautogui
except:
	print("pyautogui not installed.")
	exit()

try:
	import time
except:
	print("time not installed.")
	exit()

try:
	import os
except:
	print("os not installed.")
	exit()

def save_location():
	path = tkfilebrowser.askopendirname(title='Select the file', filetypes=[('*', '*'), ('PNG', '*.png'), ('JPG', '*.jpg')])
	print(f"Path is {path}")
	return path

def save_screenshot(path):
	mousePositionX, mousePositionY = pyautogui.position()
	pixelDimensions = 15
	path = os.path.join(path, (str(time.time()) + ".jpg"))
	print(path)
	pyautogui.screenshot(path, region=(mousePositionX-pixelDimensions, mousePositionY-pixelDimensions, pixelDimensions*2, pixelDimensions*2))


print("Selecting folder to save screenshots to.")
path = save_location()

print("Press the letter b to take a screenshot of where the mouse is, or press q to quit.")
print("Running.")

try:
	while True:
		# Check if b was pressed
		if keyboard.is_pressed('b'):
			print('b Key was pressed')
			time.sleep(.1)
			
			save_screenshot(path)
			continue
		if keyboard.is_pressed('q'):

			exit()
except:
	exit()





