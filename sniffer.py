try:
	import pyautogui
except:
	print("You have to install pyautogui")
	print("command is 'pip install pyautogui'")
	exit()
try:
	import time
except:
	print("You have to install time")
	print("command is 'pip install time'")
	exit()

try:
	import random
except:
	print("You have to install random")
	print("command is 'pip install random'")
	exit()

try:
	import math
except:
	print("You have to install math")
	print("command is 'pip install math'")
	exit()


#functions
def notfound(text):
	print(f"{text}")

def clicked(text):
	print(f"{text}")

def found(text):
	print(f"{text}")

def circlepress(centerX, centerY, radius):
	randomradius = random.randrange(0, radius)
	angledegrees = random.randrange(0, 360)
	angle = math.radians(angledegrees)

	randomX = round(centerX + (math.sin(math.radians(90-angledegrees))*randomradius)/(math.sin(math.radians(90))))
	randomY = round(centerY + (math.sin(math.radians(angledegrees))*randomradius)/(math.sin(math.radians(90))))

	return randomX, randomY
	#circlepress(155, 300, 15)

print("Welcome to the OG Ghost!")
print("Using this is quite simple. You're going to press enter, and the screen is going to start searching for a bunch of images. When it finds an image, it's going to press the image, then continue until you quit.")
print("To quit, you need to continue to press 'control c' until the script exits. It's not pretty, but it works.\n")
input("When you're ready, press the enter key and lets get to farming!")

buttons_pressed = 0
quitcommand = 0

while quitcommand != 1:

	#wait button 

	if pyautogui.locateOnScreen('images/wait.png', confidence=.9) == None:
		notfound("Wait")
	elif pyautogui.locateOnScreen('images/wait.png', confidence=.9) != None:
		wait_button = pyautogui.locateOnScreen('images/wait.png', confidence=.9)
		wait_center = pyautogui.center(wait_button)
		waitx, waity = wait_center
		found("Wait")
		pyautogui.click(1100,580)
		time.sleep(random.randrange(1,2))
		clicked("Wait")
		buttons_pressed += 1


	#reload game data yes button
	if pyautogui.locateOnScreen('images/reload_data_yes.png', confidence=.9) == None:
		notfound("Reload game data")
	elif pyautogui.locateOnScreen('images/reload_data_yes.png', confidence=.9) != None:
		reload_button = pyautogui.locateOnScreen('images/reload_data_yes.png', confidence=.9)
		reload_center = pyautogui.center(reload_button)
		reloadcenterx, reloadcentery = reload_center
		found("Reload game data")
		pyautogui.click(reloadcenterx, reloadcentery)
		time.sleep(random.randrange(1,2))
		clicked("Reload game data")
		buttons_pressed += 1


	# Daily Rewards
	if pyautogui.locateOnScreen('images/daily_reward.png', confidence=.9) == None:
		notfound("Daily reward")
	elif pyautogui.locateOnScreen('images/daily_reward.png', confidence=.9) != None:
		reward_button = pyautogui.locateOnScreen('images/daily_reward.png', confidence=.9)
		reward_center = pyautogui.center(reward_button)
		found("Daily reward")
		rewardcenterx, rewardcentery = reward_center
		pyautogui.click(circlepress(rewardcenterx, rewardcentery, 4))
		time.sleep(random.randrange(1,2))
		clicked("Daily reward")
		buttons_pressed += 1

	#daily reward reward screen
	if pyautogui.locateOnScreen('images/you_have_reward.png', confidence=.9) != None:
		pyautogui.click(circlepress(1095,389,4)) #exits out of "congras you have reward screen"
		time.sleep(random.randrange(1,2))
		clicked("Collect daily reward screen")
		buttons_pressed += 1


	#random offer
	if pyautogui.locateOnScreen('images/x_button_random_offer.png', confidence=.9) == None:
		notfound("Random offer")
	elif pyautogui.locateOnScreen('images/x_button_random_offer.png', confidence=.9) != None:
		random_offer_button = pyautogui.locateOnScreen('images/x_button_random_offer.png', confidence=.9)
		random_offer_center = pyautogui.center(random_offer_button)
		found("Random offer")
		random_offer_x, random_offer_y = random_offer_center
		pyautogui.click(circlepress(random_offer_x, random_offer_y, 5))
		time.sleep(random.randrange(1,2))
		clicked("Random offer")
		buttons_pressed += 1


	#android ad
	if pyautogui.locateOnScreen('images/memu_ad_popup.png', confidence=.9) == None:
		notfound("Android ad")
	elif pyautogui.locateOnScreen('images/memu_ad_popup.png', confidence=.9) != None:
		button = pyautogui.locateOnScreen('images/memu_ad_popup.png', confidence=.9)
		button_center = pyautogui.center(button)
		found("Android ad")
		button_x, button_y = button_center
		pyautogui.click(circlepress(button_x, button_y,4))
		time.sleep(random.randrange(1,2))
		clicked("Android ad")
		buttons_pressed += 1

	#monthly pack offer
	if pyautogui.locateOnScreen('images/monthly_offer.png', confidence=.9) == None:
		notfound("Montly card offer")
	elif pyautogui.locateOnScreen('images/monthly_offer.png', confidence=.9) != None:
		button = pyautogui.locateOnScreen('images/monthly_offer.png', confidence=.9)
		found("Monthly card offer")
		pyautogui.click(circlepress(735,97,4))
		time.sleep(random.randrange(1,2))
		clicked("Monthly card offer")
		buttons_pressed += 1	

	#android kffer for app store
	if pyautogui.locateOnScreen("images/no_thanks.png", confidence=.7):
		notfound("Play store offer")
	elif pyautogui.locateOnScreen("images/no_thanks.png", confidence=.7):
		button = pyautogui.locateOnScreen("images/no_thanks.png", confidence=.7)
		found("Play store offer")
		buttoncenter = pyautogui.center(button)
		centerx, centery = buttoncenter
		pyautogui.click(centerx, centery)
		time.sleep(random.randrange(1,2))
		clicked("Play store offer")
		buttons_pressed += 1


		

	print(f"{buttons_pressed} events clicked\n")
	time.sleep(2)