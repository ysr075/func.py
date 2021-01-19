import time

LED_on = "\nLED on"
LED_off = "\nLED off"

while True:
	choise = int(input("\n1.and / 2.or / 3.not: "))
	if choise == 1:
		IF1 = float(input("\nIF1: "))
		IF2 = float(input("IF2: "))
		if IF1 == 1 and IF2 == 1:
			print(LED_on)
		else:
			print(LED_off)
	elif choise == 2:
		IF1 = float(input("\nIF1: "))
		IF2 = float(input("IF2: "))
		if IF1 == 1 or IF2 == 1:
			print(LED_on)
		elif IF1 == 0 and IF2 == 0:
			print(LED_off) 
		else:
			print(LED_off)
	elif choise == 3:
		IF1 = float(input("\nIF1: "))
		if IF1 == 1:
			print(LED_off)
		elif IF1 == 0:
			print(LED_on)
	else:
		time.sleep(1)
		exit()
