
def countlength(inputarray):
	c = 0
	for i in inputarray:
		c += 1
	return c

def addElem(inputarray):
	position = int(input("Enter the index position for the element insertion: "))
	element = int(input("Now add the inserting element: "))
	length = countlength(inputarray)
	#Show error when entered index is out of range of input array
	if position > length:
		print("[INFO] Entered index out of range..")
	else:
		fhalf = inputarray[0: position]
		shalf = inputarray[position:]
		fhalf += [element]
		outputarray = fhalf+shalf
		print("The new array is: ", outputarray)

inputarray = [0,6,0,7,1,9,9,7]
addElem(inputarray)

