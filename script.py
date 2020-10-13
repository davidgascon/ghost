import pyautogui
import time
import os
import math
import random


def building_check(building):
	'''
	Returns center cordinates of image found or False
	example - building_check("college")
	'''
	confidence = .7
	folder = os.path.join(os.getcwd(), "hunt", building)
	#print(folder)
	version = highest_dir(folder)
	checkingFolder = os.path.join(folder, version)
	#print(checkingFolder)
	pyautogui.screenshot(region=(566, 38, 545, 964))
	while True:
		for file in os.listdir(checkingFolder):
			#print(file)
			if pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964)):
				#print(f"{building} found with file {file}")
				#print(pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964)))
				try:
					x, y = pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964))
					return x, y
				except:
					return False
				
			else:
				pass
		return False

def highest_dir(folder):
	'''
	Returns the highest 'version' or folder number that we should be comparing to.
	'''
	versions = []
	for item in os.listdir(folder):
		if "." not in item:
			versions.append(item)

	versions.sort(reverse=True)
	print(f"Highest Folder is {versions[0]}")
	return versions[0]

def centerRadius(path, radius=10, confidence=.8):
	
	center = pyautogui.locateCenterOnScreen(path, confidence=confidence, grayscale=True)
	pyautogui.click(center[0], center[1])
	return center[0], center[1], radius

def button_back():
	if pyautogui.locateOnScreen('images/backbutton.jpg', confidence=.8, grayscale=True):
		print("Pressing Back Button.")
		boxpress(582, 49, 632, 88)
	else:
		print("Back button not found.")


def moveToCity(screen='city'):
	if pyautogui.locateOnScreen('images/map.jpg', confidence=.8, grayscale=True):
		print("Map found!")
		return True
	else:
		if pyautogui.locateOnScreen('images/city.jpg', confidence=.8, grayscale=True):
			centerRadius('images/city.JPG', 25)
			
			print("Pressed on the map.")
			time.sleep(3)
			moveToCity()
		elif pyautogui.locateOnScreen('images/backbutton.jpg', confidence=.8, grayscale=True):
			button_back()
		
		print("Not sure what was found. Retrying to find the city.")
		moveToCity()

def boxpress(left, top, right, bottom):
	randomX = random.randrange(left, right, 1)
	randomY = random.randrange(top, bottom, 1)
	pyautogui.click(randomX, randomY)


def circlepress(centerX, centerY, radius=10):
	print("Pressing the circle.")
	randomradius = random.randrange(0, radius)
	angledegrees = random.randrange(0, 360)
	angle = math.radians(angledegrees)

	randomX = round(centerX + (math.sin(math.radians(90-angledegrees))*randomradius)/(math.sin(math.radians(90))))
	randomY = round(centerY + (math.sin(math.radians(angledegrees))*randomradius)/(math.sin(math.radians(90))))
	pyautogui.moveTo(randomX, randomY)
	pyautogui.click(randomX, randomY)
	print(f"Randomly clicked at {randomX} {randomY}")
	time.sleep(.5)
	#circlepress(155, 300, 15)




def daily_harvest():
	print("Running Harvest Skills Check.")
	moveToCity()
	if pyautogui.locateCenterOnScreen('images/skills.jpg', grayscale=True, confidence=.8):
		center = pyautogui.locateCenterOnScreen('images/skills.jpg', grayscale=True, confidence=.8)
		circlepress(center[0], center[1]) #presses skills
		time.sleep(random.uniform(.75, 1.5))
		try:
			center = pyautogui.locateCenterOnScreen('images/harvest.jpg', grayscale=True, confidence=.8)
			circlepress(center[0], center[1]) #presses harvest
			if pyautogui.pixelMatchesColor(908, 962, (67, 67, 67), tolerance=10) == False: #if use button is green
				time.sleep(random.uniform(.5, 1))
				boxpress(756, 947, 924, 978) #presses use
				time.sleep(random.uniform(2,4))
				boxpress(618, 195, 1063, 949) #presses on screen to exit out
				time.sleep(random.uniform(2,2.25))
				boxpress(885, 751, 1085, 960) #randomly  in lower right corner to exit out
				time.sleep(random.uniform(.25,1))
			else:
				print("Skill colling down.")
				boxpress(700, 340, 987, 778)
				time.sleep(random.uniform(.5,1))
				boxpress(700, 340, 987, 778)
		except:
			print("Harvest skill not found.")
	else:
		print("Skills button not found.")

	moveToCity()


def daily_pinata():
	print("Running Pinata.")
	moveToCity()
	if building_check('pinata'):
		print("Pinata found!")
		try:
			center = building_check('pinata')
			circlepress(center[0], center[1])
		except:
			print("Pinata not found.")
			moveToCity()
			return
		
		listOfPinatas = pyautogui.locateAllOnScreen('images/pinata_center.jpg')
		listOfCenters = []
		
		for centerofpinata in listOfPinatas:
			print(pyautogui.center(centerofpinata))
			listOfCenters.append(pyautogui.center(centerofpinata))

		random.shuffle(listOfCenters)
		for pinata in listOfCenters:
			print(f"original point is {pinata}" )
			circlepress(pinata[0], pinata[1], radius=15)
			time.sleep(random.uniform(.2, .5))
			if pyautogui.pixelMatchesColor(866, 920, (116, 195, 41), tolerance=10): #if pixel at bottom is green, ie you've bust
				print("Bummer. You drew a bomb.")
				moveToCity()
				break
			if pyautogui.pixelMatchesColor(1083, 968, (2, 59, 66), tolerance=10):
				print("Fortune Teller Time!")
				time.sleep(random.uniform(4,6))
				boxpress(779, 851, 907, 876) #press try
				time.sleep(random.uniform(.5,1.5))
				boxpress(582, 816, 1088, 921) #randomly presses a card
				time.sleep(random.uniform(.5,1.5))
				boxpress(976, 954, 1091, 979) #presses fold
				time.sleep(random.uniform(.5,1.5))
				boxpress(776, 543, 904, 574) #presses confirm
				time.sleep(random.uniform(.5,1.5))


listOfTasks = ['pinata', 'harvest']
random.shuffle(listOfTasks)
print(f"List of things to do! {listOfTasks}")

for task in listOfTasks:
	if task == 'pinata':
		daily_pinata()
	if task == 'harvest':
		daily_harvest()


#building_check("castle")


