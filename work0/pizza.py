from time import time
from datetime import datetime
from glob import glob

def take(name , price):
	"""
	adds the given Person with the given prices to the current order
	"""
	print("Taking order from " + name + " " + price)
	if(name in orders):
		orders[name] += price
	else:
		orders[name] = price

def list_of_orders():
	"""
	Returns the a list of the current orders (helping function)
	"""
	result = ""
	print(list(orders.keys()))
	list_of_people = list(orders.keys())
	for person in list_of_people:
		result += person + "-" + str(orders[person]) + "\n"
	return result

def status():
	"""
	Prints the status
	"""
	print(list_of_orders())

def save():
	"""
	Saves the orders in a file
	"""

	#sets the currents time to a variable
	ts = time()
	stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
	#creates a new file for the orders
	file_order = open("orders/oreders" + stamp ,"w")
	print("Saved the current order to orders_"+ stamp)
	file_order.write(list_of_orders())
	file_order.close()
	orders.clear()

def list_func():
	counter = 0
	for file in glob("orders/*"):
		files_with_orders[str(counter)] = file
		print("[" + str(counter) + "]" + " - " + file)
		counter += 1

def load(number):
	if(list(list_of_orders.keys()) == []):
		print("Use list command before loading\n")
	elif([] != list(list_of_orders.keys())):
		print("You have not saved the current order.\nif you wish to discard it, type load <number> again.")

### Setting global variables ###
orders = {}	#Keeps the orders
commands = {"status": status, "save": save, "list": list_func } #keeps the commands
list_of_orders = {}

### Main Menu ###
while(True):
	command = input("Enter command>")
	splited_command = command.split()

	if(command == "finish"):
		break

	#The commans are separated by the count of arguments
	#If more areguments are given than the wanted ->
	#prints error messege and continues

	elif(splited_command[0] == 'take'):
		if( len(splited_command)>3 ):
			print("Too many arguments\n")
		else:
			take(splited_command[1] ,splited_command[2])
	elif( splited_command[0] == 'load' ):
		if( len(splited_command)>2 ):
			print("Too many arguments")
		else:
			load(splited_command[1])
	else:
		if( len(splited_command)>1 ):
			print("Too many arguments")
		else:
			commands[command]()
