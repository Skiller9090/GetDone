string = "i am an animal"
splitString = string.split()
print(splitString)
stringList = []
stringLength = len(splitString)
print(stringLength)
if splitString[0] == "i":
	for i in splitString[abs(1-stringLength)]:
		stringList.append(i)
		print(stringList)