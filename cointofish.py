import pyautogui
import time

def in_fishes_screen():
	if pyautogui.locateOnScreen('myfishes.jpg', confidence = 0.80) is None:
		return False
	else:
		return True

def go_to_fishes_screen():
	print('-- Go to fishes sreen')
	invent = pyautogui.locateCenterOnScreen('inventory.jpg', confidence = 0.90)
	pyautogui.moveTo(invent, duration=0.3, tween=pyautogui.easeInOutQuad)
	pyautogui.click()
	time.sleep(2)	

def get_fishes():
	return list(pyautogui.locateAllOnScreen('gear.jpg', confidence = 0.95))

def fish_close():
	close = pyautogui.locateCenterOnScreen('close.jpg', confidence = 0.80)
	pyautogui.moveTo(close, duration=0.3, tween=pyautogui.easeInOutQuad)
	pyautogui.click()
	time.sleep(2)	

def fish_open(fish):
	print('-- Open Fish')
	l,t,w,h = fish
	x,y=int(l+(w/2)),int(t+(h/2))
	pyautogui.moveTo((x,y), duration=0.3, tween=pyautogui.easeInOutQuad)
	pyautogui.click()
	time.sleep(2)

	if pyautogui.locateCenterOnScreen('nothungry.jpg', confidence = 0.90): 
		print('-- The fish is not hungry')
		fish_close()
	else:
		fish_feed()

def fish_feed():
	print('-- Feed Fish')
	available_food = pyautogui.locateCenterOnScreen('availablefood.jpg', confidence = 0.90)
	pyautogui.moveTo(available_food, duration=0.2, tween=pyautogui.easeInOutQuad)
	if available_food:
		pyautogui.click()
		pyautogui.press('down')
		time.sleep(1)
		pyautogui.press('enter')
		feed = pyautogui.locateOnScreen('feed.jpg', confidence = 0.90)
		pyautogui.moveTo(feed, duration=0.2, tween=pyautogui.easeInOutQuad)
		pyautogui.click()
		print('-- Fed Fish')
		time.sleep(3)
	else:
		fish_close()

if __name__ == "__main__":
	while True:
		if not in_fishes_screen(): 
			go_to_fishes_screen()

		fish_close()
		
		fishes = get_fishes()
		for fish in fishes:
			fish_open(fish)
	
		print("-- Ended all fishes")
		print("-- Waiting for 20s.....")
		time.sleep(20)