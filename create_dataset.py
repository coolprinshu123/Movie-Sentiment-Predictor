import random
import sys
fileName = "Train/labeledBow.feat"
posIndexArr = []
negIndexArr = []
for j in range(500):
	index = random.randint(0,12499)
	while(index in posIndexArr):
		index = random.randint(0,12499)
	posIndexArr.append(index)
for j in range(500):
	index = random.randint(12500,24999)
	while(index in negIndexArr):
		index = random.randint(12500,24999)
	negIndexArr.append(index)

CompleteList = posIndexArr + negIndexArr
#print(len(negIndexArr))

CompleteList.sort()
#print(CompleteList)

file = open(fileName,"r")
train = open("Train.txt","w+")
k = 0;
count = 0;
for line in file:
	if count != 1000:
	  if CompleteList[count] == k:
		train.write(line)
		#print count
		count = count + 1
	  k = k+1
	#print j
#print CompleteList[count - 1]
file.close()
train.close()
		
fileName = "Test/labeledBow.feat"
file = open(fileName,"r")
posIndexArr = []
negIndexArr = []
for j in range(500):
	index = random.randint(0,12499)
	while(index in posIndexArr):
		index = random.randint(0,12499)
	posIndexArr.append(index)
for j in range(500):
	index = random.randint(12500,24999)
	while(index in negIndexArr):
		index = random.randint(12500,24999)
	negIndexArr.append(index)

CompleteList = posIndexArr + negIndexArr
CompleteList. sort()

file = open(fileName,"r")
train = open("Test.txt","w")
k = 0;
count = 0;
for line in file:
	if count != 1000:
	  if CompleteList[count] == k:
		train.write(line)
		#print count
		count = count + 1
	  k = k+1
	#print j
#print CompleteList[count - 1]
file.close()
train.close()


	
