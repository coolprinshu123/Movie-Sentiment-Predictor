
list = []

fileName = "imdbEr.txt"
file = open(fileName,"r")
i = 0
for line in file:
	#print line
	list.append((float(line),i))
	i = i+1
	#print list[i-1]	

list.sort()
#print list
res = [i[1] for i in list]

with open('selected-features-indices.txt', 'w') as fp:
	for j in range(2500):
		fp.write(str(res[j]) + "\n")
	for j in range(2500):
		fp.write(str(res[-j-1]) + "\n")
    
