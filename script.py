import pyautogui
import time
import os
import math
import random

#constants
directory = os.getcwd()
gameRegion = (566, 38, 545, 964)
testing = False
farmsRan = 0
totalFarms = 0

def testing(message='No Message Entered'):
	'''If testing is marked as true, it will print the message'''
	global testing
	if testing:
		print(f"{message}")
	else:
		pass


def building_check(building):
	'''
	Returns center cordinates of image found or False
	example - building_check("college")
	'''
	testing("Running Building Check.")
	confidence = .7
	folder = os.path.join(os.getcwd(), "hunt", building)
	#print(folder)
	version = highest_dir(folder)
	checkingFolder = os.path.join(folder, version)
	#print(checkingFolder)
	pyautogui.screenshot(region=(566, 38, 545, 964))
	testing(f"Checking for image in {checkingFolder}")
	while True:
		for file in os.listdir(checkingFolder):

			#print(file)
			if pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964)):
				#print(f"{building} found with file {file}")
				#print(pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964)))
				testing("Found an image in this folder.")
				try:
					x, y = pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964))
					testing(f"Found the image at {x} {y}")
					return x, y
				except:
					testing("Could not find the image to click on it.")
					return False
				
			else:
				pass
		return False

def highest_dir(folder):
	'''
	Returns the highest 'version' or folder number that we should be comparing to.
	'''
	versions = []
	testing("Checking the higest directory")
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
	testing("Checking for the back button")
	if pyautogui.locateOnScreen('images/backbutton.jpg', confidence=.8, grayscale=True):
		testing("Clicking the back button.")
		boxpress(582, 49, 632, 88)
	else:
		testing("Back button not found.")


def moveToCity(screen='city', count=0):
	sniffer()
	counter = count + 1
	print(f"Looking for city. Cycle # {counter}")
	if counter % 5 == 0:
		print("It's been ran 5 times")
		sniffer()



	if pyautogui.locateOnScreen('images/map.jpg', confidence=.8, grayscale=True):
		print("Map found!")
		time.sleep(random.uniform(1,3))
		return True
	else:
		if pyautogui.locateOnScreen('images/city.jpg', confidence=.8, grayscale=True):
			centerRadius('images/city.JPG', 25)
			
			print("Pressed on the map.")
			time.sleep(3)
			
		elif pyautogui.locateOnScreen('images/backbutton.jpg', confidence=.8, grayscale=True):
			button_back()
		elif building_check('app'):
			try:
				print("Clicking on the map in 5.")
				time.sleep(5)
				center = building_check('app')
				circlepress(center[0], center[1])
				time.sleep(20)
			except:
				print("App not found")
		time.sleep(1)
		moveToCity(count=counter)

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

def clickImage(image):
	global gameRegion
	try:
		cords = pyautogui.locateOnScreen(image, confidence=.85, grayscale=True, region=gameRegion)
		pyautogui.moveTo(cords[0], cords[1])
		boxpress(cords[0], cords[1], cords[0] + cords[2], cords[1] + cords[3])
		return True
	except:
		print(f"{image} not found.")
		return False

def daily_harvest():
	print("Running Harvest Skills Check.")
	moveToCity()
	if pyautogui.locateCenterOnScreen('images/skills.jpg', grayscale=True, confidence=.8):
		center = pyautogui.locateCenterOnScreen('images/skills.jpg', grayscale=True, confidence=.8)
		circlepress(center[0], center[1]) #presses skills
		time.sleep(random.uniform(2, 4))
		try:
			center = pyautogui.locateCenterOnScreen('images/harvest.jpg', grayscale=True, confidence=.8)
			circlepress(center[0], center[1]) #presses harvest
			time.sleep(random.uniform(1, 2))
			if pyautogui.pixelMatchesColor(908, 962, (67, 67, 67), tolerance=10) == False: #if use button is green
				time.sleep(random.uniform(1, 2))
				boxpress(756, 947, 924, 978) #presses use
				time.sleep(random.uniform(2,3))
				boxpress(618, 195, 1063, 949) #presses on screen to exit out
				time.sleep(random.uniform(2,2.5))
				boxpress(885, 751, 1085, 960) #randomly  in lower right corner to exit out
				time.sleep(random.uniform(.75,1.5))
			else:
				time.sleep(1)
				print("Skill colling down.")
				boxpress(720, 340, 987, 778)
				time.sleep(random.uniform(1,2))
				boxpress(720, 340, 987, 778)
				time.sleep(2)
		except:
			print("Harvest skill not found.")
	else:
		print("Skills button not found.")
	print("Done running harvest skill.")
	time.sleep(.5)
	moveToCity()


def daily_pinata():
	print("Running Pinata.")
	moveToCity()
	if building_check('pinata'):
		print("Pinata found!")
		try:
			center = building_check('pinata')
			circlepress(center[0], center[1])
			time.sleep(2)
		except:
			print("Pinata not found.")
			time.sleep(2)
			moveToCity()
			return
		
		listOfPinatas = pyautogui.locateAllOnScreen('images/pinata_center.jpg')
		listOfCenters = []
		
		for centerofpinata in listOfPinatas:
			listOfCenters.append(pyautogui.center(centerofpinata))

		random.shuffle(listOfCenters)
		for pinata in listOfCenters:
			print(f"original point is {pinata}" )
			circlepress(pinata[0], pinata[1], radius=15)
			time.sleep(random.uniform(.5, 1.2))
			if pyautogui.pixelMatchesColor(866, 920, (116, 195, 41), tolerance=10): #if pixel at bottom is green, ie you've bust
				print("Bummer. You drew a bomb.")
				time.sleep(.25)
				moveToCity()
				break
			if pyautogui.pixelMatchesColor(1083, 968, (2, 59, 66), tolerance=10):
				print("Fortune Teller Time!")
				time.sleep(random.uniform(5,7))
				boxpress(779, 851, 907, 876) #press try
				time.sleep(random.uniform(4,6))
				boxpress(582, 816, 1088, 921) #randomly presses a card
				time.sleep(random.uniform(2,4))
				boxpress(976, 954, 1091, 979) #presses fold
				time.sleep(random.uniform(2,4))
				boxpress(776, 543, 904, 574) #presses confirm
				time.sleep(random.uniform(3,5))

def listOfFarms(directory=os.getcwd()):
	'''Returns a list of farms in the farms folder'''
	totalFarms = 0
	farmsDirectory = os.path.join(directory, "farms")
	#print(farmsDirectory)
	listOfFarms = []
	for farm in os.listdir(farmsDirectory):
		listOfFarms.append(farm)
		totalFarms += 1
	#print(listOfFarms)
	return listOfFarms,totalFarms

def sniffer(count=0):
	global gameRegion
	#upgrade button for game version
	if pyautogui.locateOnScreen('images/sniffer/upgrade.jpg', confidence=.85, grayscale=True, region=gameRegion):
		print("Upgrade game version button found.")
		boxpress(671, 519, 806, 553) #presses upgrade
		time.sleep(5)
		pyautogui.click(633, 846) #presses play store
		time.sleep(15)
		if pyautogui.pixelMatchesColor(1024, 963, (11, 154, 141), tolerance=10):
			print("Pressing always.")
			pyautogui.click(1024, 963)
			time.sleep(12)
		pyautogui.click(1021, 262) #presses upgrade
		while pyautogui.pixelMatchesColor(1027, 259, (241, 243, 244), tolerance=10):
			print("Still downloading..")
			time.sleep(6)
		pyautogui.click(1021,262) #presses open
		time.sleep(10)

	#get reward
	if pyautogui.locateOnScreen('images/sniffer/dailyReward.jpg', region=gameRegion, grayscale=True, confidence=.8):
		print("Found daily reward")
		clickImage('images/sniffer/dailyReward.jpg')
		time.sleep(random.uniform(1,2))
	if pyautogui.locateOnScreen('images/sniffer/reward.jpg', region=gameRegion, grayscale=True, confidence=.8):
		boxpress(600, 60, 1050, 860)

	if pyautogui.locateOnScreen('images/sniffer/wasted_skill.jpg', region=gameRegion, grayscale=True, confidence=.8):
		testing("Found the wasted skill image. Going to try to exit.")
		if random.choice(['true', 'false']) == 'true':
			boxpress(714, 258, 983, 896) #randomly presses in middle of skills page
		else:
			boxpress(586, 756, 1062, 890) #randomly presses in bottom half of skills page
	if pyautogui.locateOnScreen('images/sniffer/playstore_open_grey.jpg', region=gameRegion, grayscale=True, confidence=.8):
		testing("Downing update still.")
		time.sleep(15)
	if pyautogui.locateOnScreen('images/go_button.jpg', region=gameRegion, grayscale=True, confidence=.8):
		print("Found the go button.")
		boxpress(558, 203, 1091, 756)
		time.sleep(random.uniform(1,3))		

	#These will click the image if it's found
	clickImage('images/sniffer/playstore_open.jpg')
	clickImage('images/sniffer/little_x.jpg')
	clickImage('images/sniffer/playstore_open.jpg')
	for imgLink in os.listdir(os.path.join(os.getcwd(), 'images', 'automatic')):
		clickImage(os.path.join(os.getcwd(), 'images', imgLink))
	time.sleep(3)
		
def moveCity():
	print("moving city")
	pyautogui.moveTo(704, 717)
	time.sleep(1)
	pyautogui.dragRel(350, -236, duration=random.uniform(1,1.2))
	time.sleep(3)
def moveToMap(cycle=0):
	global gameRegion
	counter = 0
	testing("Moving to Map")
	if pyautogui.locateOnScreen('images/city_button.jpg', confidence=.8, grayscale=True, region=gameRegion) == None:
		circlepress(628, 957, 32) #presses map
		time.sleep(random.uniform(.8, 1.5))
		while pyautogui.locateOnScreen('images/city_button.jpg', confidence=.8, grayscale=True, region=gameRegion) == None:
			print("City button not found. Not on map yet.")
			time.sleep(random.uniform(.5,1.5))
			counter += 1
			if counter > 5:
				sniffer()
				print("Adding one to cycle")
				moveToMap(cycle+1)
				if cycle > 4:
					print("Problem locating the map..")
					exit()

	return True


def sendGathers(resource='wood', marches=1):
	def press_searchButton(cycle=0):
		counter = 0
		circlepress(1069, 798, 20) #presses search button
		while pyautogui.locateOnScreen('images/go_button.jpg', confidence=.8, grayscale=True, region=gameRegion) == None:
			testing("Still searching for the game button")
			time.sleep(random.uniform(.25, .75))
			counter += 1
			if counter > 10:
				if cycle > 5:
					print("Fatal error finding go button. Exiting.")
					exit()

				press_searchButton(cycle+1)
		else:
			testing("Found the go button. Returning True.")
			return True
	def press_goButton(cycle=0):
		global gameRegion
		counter = 0
		while pyautogui.locateOnScreen('images/go_button.jpg', confidence=.8, grayscale=True, region=gameRegion) == None:
			print("Waiting for go button.")
			time.sleep(random.uniform(.5,1))
			counter += 1
			if counter > 5:
				press_searchButton()
		clickImage('images/go_button.jpg') #presses the go button
		time.sleep(random.uniform(.25,.5))

	def press_gather(cycle=0):
		global gameRegion
		counter = 0
		time.sleep(random.uniform(.75,1.5))
		while pyautogui.locateOnScreen('images/gather_button.jpg', confidence=.8, grayscale=True, region=gameRegion):
			clickImage('images/gather_button.jpg')
			time.sleep(random.uniform(.2,.6))
			if cycle < 10:
				press_gather(cycle+1)
			else:
				print("Error finding cycle button.")
				exit()
	def change_resource(resource='wood', firstRun=True):
		global gameRegion
		if firstRun == True:
			testing("First run")
			time.sleep(random.uniform(.1,.6))
		else:
			testing("not first run")

			time.sleep(random.uniform(.1,.2))

		if pyautogui.locateOnScreen(f'images/resource/found_{resource}.jpg', grayscale=True, confidence=.8, region=gameRegion) == None:
			print(f"{resource.upper()} not found. Attempting to select.")
			if clickImage(f'images/resource/{resource}.jpg'):
				print("Clicked on the resource.")
				time.sleep(random.uniform(1,2))
				change_resource(resource, firstRun=False )

		else:
			testing("Found the resource tile. Returning True")
			return True
	def tile_size(size=4):
		if pyautogui.locateOnScreen('images/resource/4outof6.jpg') == None:
			circlepress(798, 959, 4) #pressing 4
			time.sleep(.2)
			#tile_size(size)
		else:
			testing("Found 4/6. Returning True")
			return True
	#try:
	print(f"Sending {marches} gathers for {resource}")
	moveToMap()
	press_searchButton()
	change_resource('food')
	tile_size()
	press_goButton()
	time.sleep(1)
	press_gather()
	time.sleep(2)
	clickImage('images/set_out.jpg')
	print("Sent gather out.")
	time.sleep(random.uniform(1,3))
	#except:
	#	print("Error somewhere where we tried to send gather out.")
	#	moveToCity()

def redeemTroops():
	list_of_troops = []
	counter = 0
	counter1 = 0
	for troop in os.listdir(os.path.join(os.getcwd(), 'hunt', 'redeemTroops')):
		print("Checking next image")
		#try:
		for spot in pyautogui.locateAllOnScreen(os.path.join(os.getcwd(), 'hunt', 'redeemTroops', troop), confidence=.8, grayscale=True):
			
			#print(spot)
			print(f"Found one at {spot[0]} {spot[1]} {spot[2]} {spot[3]}")
			counter += 1
			
			if [spot[0], spot[1]] in list_of_troops:
				pass
			else:
				list_of_troops.append([spot[0], spot[1]])
				counter1 += 1
					
		

		#except:
		#	print("Found nothing")
		print("NEW LIST ------------------------------------------------------")
		for spot in list_of_troops:
			print(spot)
		print(counter)
		print(counter1)




#listOfFarms(directory)
listOfFarms, totalFarms = listOfFarms()
while listOfFarms != []:
	currentFarm = random.choice(listOfFarms)
	listOfFarms.remove(currentFarm)
	listOfTasks = ['pinata', 'harvest', 'gathers']
	#tasks to add - check quests, oen mail, donate to tech, lord skills, level up, growth map, daily reward
	#random tasks to do -check lord skill, view golden hammer, check VIP, check packs, view rankings, check emblem, check merit, 
	random.shuffle(listOfTasks)
	print(f"----------------------------Running farm {farmsRan}/{totalFarms}------------------------")
	print(f"List of things to do! {listOfTasks}")




	farmpath = os.path.join('farms', currentFarm)
	os.startfile(farmpath)
	print("Sleeping for 30")
	time.sleep(30)
	moveToCity()
	moveCity()
	for task in listOfTasks:
		print(f"Tasks were doing now {task.upper()}")
		if task == 'pinata':
			daily_pinata()
		if task == 'harvest':
			daily_harvest()
		if task == 'gathers':
			sendGathers()
		listOfTasks.remove(task)
	print("Exiting")
	farmsRan += 1
	time.sleep(1)

	os.system(f"TASKKILL /F /IM Nox.exe")


#building_check("castle")
#NoxVMHandle.exe


