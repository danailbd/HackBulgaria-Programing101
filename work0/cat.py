import sys
from random import randint
from functools import reduce

def cat():
	file = open(sys.argv[1], "w")
	file.write("\n".join(["Az","sam","gotin"]))
	file.close()

	file = open(sys.argv[1], "r")
	print(file.read())

def main():
	filelist = sys.argv[1:]
	for filename in filelist:
		file = open(filename, "r")
		print(file.read() + "\n\n")

def generate_numbers():
	file = open(sys.argv[1], "w")
	for i in range(0, int(sys.argv[2])):
		file.write(str(randint(1,1000)) + " ")
	
def sum_numbers():
	file = open(sys.argv[1], 'r')
	numbers = file.read().split()
	print(reduce(lambda x, y: int(x) + int(y) ,numbers))

def concat_files():
	newFile = open("Megatron", "w")
	for file in sys.argv[1:]:
		tempFile = open(file, 'r')
		newFile.write(tempFile.read())

def wc():
	file = open(sys.argv[2], 'r')
	if(sys.argv[1] == 'chars'):
		print(len(file.read()))
	elif(sys.argv[1] == 'words'):
		print(len(file.read().split()))
	else:
		print(len(file.read().split("\n")))


if __name__ == "__main__":
	wc()