import pyautogui
import time
import os


def building_check(building):
	'''
	Returns center cordinates of image found or False
	example - building_check("college")
	'''
	confidence = .7
	folder = os.path.join(os.getcwd(), "hunt", building)
	print(folder)
	version = highest_dir(folder)
	checkingFolder = os.path.join(folder, version)
	print(checkingFolder)
	pyautogui.screenshot(region=(566, 38, 545, 964))
	while True:
		for file in os.listdir(checkingFolder):
			#print(file)
			if pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964)):
				#print(f"{building} found with file {file}")
				print(pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964)))
				try:
					x, y = pyautogui.locateCenterOnScreen(os.path.join(checkingFolder, file), confidence=confidence, grayscale=True, region=(566, 38, 545, 964))
				except:
					pass
				#return x, y
			else:
				print("")
		#return False
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

building_check("castle")


