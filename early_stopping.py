import math
class node : 
	def __init__(self,output = None):
		self.feature = None
		self.left = None
		self.right = None
		self.output = None
		
		
def entropy(plus,minus):
	x=0.0
	y=0.0
	plus = float(plus)
	minus = float(minus)
	pluss = 0.0
	if plus!=0:
		pluss = plus/(plus+minus)
		x = math.log(pluss,2)
	if minus!=0:
		minus = minus/(plus+minus)
		y = math.log(minus,2)
	return -(pluss*x) -(minus*y)
	
def information_gain(entropyPrev,numPosless,numNegless,numPosmore,numNegmore):
	numPosless=float(numPosless)
	numNegless=float(numNegless)
	numPosmore=float(numPosmore)
	numNegmore=float(numNegmore)
	total = numPosless+numNegless+numPosmore+numNegmore
	return ((numPosless+numNegless)*entropy(numPosless,numNegless))/(total) + ((numPosmore+numNegmore)*entropy(numPosmore,numNegmore))/(total)
	
class tree_construct:
	def __init__(self):
		self.tree = None
	def createNode(self):
		newNode = node()
		return newNode
		
	def maxIG(self,mat,features, prev, prev_feature):
		prevOutput = 1
		output_feature = 0
		xx = 0
		yy = 0
		for feature in range(len(features)):
			numPosless= 0
			numNegless=0
			numPosmore=0
			numNegmore=0
			if feature in prev_feature:
				continue
				
			for j in prev:
					if j<500:
						if mat[j][feature]==0:
							numPosless = numPosless+1
						else:
							numPosmore = numPosmore + 1
					if j>=500:
						 if mat[j][feature]==0:
							numNegless = numNegless+1
						 else:
							numNegmore = numNegmore + 1
		
			output = information_gain(0,numPosless,numNegless,numPosmore,numNegmore)
			if output < prevOutput:
				xx = numPosless+numNegless
				yy = numPosmore+numNegmore
				output_feature = feature
				prevOutput = output
		if xx==0 or yy==0:
			return -1
		if xx+yy < 12:
			return -1
			
		return output_feature
				
	def create_tree(self,mat,features,prev=[],tree=None,prev_feature=[]):
		if tree == None:
			tree = self.createNode()
		next_feature = self.maxIG(mat,features,prev,prev_feature)
		if next_feature == -1:
			count = 0
			count1 = 0
			for element in prev:
				if element<500:
					count = count + 1
				else:
					count1 = count1 + 1
			if count >= count1:
				tree.output = 1
			else:
				tree.output = -1
			return tree
		list1 = []
		list2 = []
		for i in prev:
			if mat[i][next_feature]==0:
				list1.append(i)
			else :
				list2.append(i)
		
		tree.feature = next_feature
		prev_feature.append(next_feature)
		tree.left = self.create_tree(mat,features,list1,tree.left,prev_feature)
		tree.right = self.create_tree(mat,features,list2,tree.right,prev_feature)
		return tree
		
def outputResult(tree,list1):
	if tree.output!=None:
		return tree.output
	if list1[tree.feature] == 0:
		return outputResult(tree.left,list1)
	else:
		return outputResult(tree.right,list1)
		
def accuracy(list1,list2):
	count = 0
	for i in range(len(list1)):
		if(list1[i]==list2[i]):
			count = count + 1
	return (count*100)/len(list1)
	

def testFile(tree,testPath="Test.txt",featurePath = "selected-features-indices.txt"):
	features = open(featurePath,"r")
	value = []
	for line in features:
		value.append(int(line))
	test = open(testPath,"r")
	list3 = []
	matrix = []
	for line in test:
		i = 0;
		list11 = []
		list100 = []
		for tuples in line.split(" "):
			if i==0:
				i = i+1	
				continue
			else :
				attribute = tuples.partition(':')[0]
				list100.append(int(attribute))
				
		for k in value:
			if k in list100:
				list11.append(1)
			else:
				list11.append(0)
		matrix.append(list11)
		
	for list10 in matrix:
		x = outputResult(tree,list10)
		list3.append(x)
	outVec = []
	for i in range(1000):
		if i<500:
			outVec.append(1)
		else:
			outVec.append(-1)

	print "Accuracy is : "
	print accuracy(outVec,list3)
	return list3
	
def trainFile(trainPath="Train.txt",featurePath="selected-features-indices.txt"):
	train = open(trainPath,"r")
	features = open(featurePath,"r")
	value = []
	for line in features:
		value.append(int(line))
	
	mat = []
	for line in train:
		i = 0;
		listp = []
		list2 = []
		for tuples in line.split(" "):
			if i==0:
				i = i+1
				
				continue
			else :
				#print tuples
				attribute = tuples.partition(':')[0]
				list2.append(int(attribute))
				
		for ii in value:
			if ii in list2:
				listp.append(1)
			else:
				listp.append(0)
		mat.append(listp)

	decision_tree = tree_construct()
	feature_no = []
	prev = []
	for i in range(5000):
		feature_no.append(i)
	for i in range(1000):
		prev.append(i)
	
	tree = decision_tree.create_tree(mat,feature_no,prev)
	return tree


trainPath = "Train.txt"
testPath = "Test.txt"
featurePath = "selected-features-indices.txt"
tree = trainFile(trainPath,featurePath)
x = testFile(tree)
