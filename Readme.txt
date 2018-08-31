				SENTIMENT CLASSIFICATION OF MOVIE REVIEWS USING DECISION TREE AND FOREST
			
The package contains the solution for the assignment 1 of CSL 603(Machine Learning). The package contains the python implementation of the movie review classification problem. The input is given in the form of the text file which contains the bag of words representation of the review given by the user. The package contains the decision tree ID3 algorithm implementation in python language.

This program can be run in two ways : 
A. USING "master.py" FILE : 
	The code can be run using the "master.py" file via following command :
	"python master.py ExperimentNo"
	
	Here ExperimentNo refers to the following command line options : 
	2 -> To build the decision tree
	3 -> To see the results of the noise addition
	4 -> To get the output of the pruned tree.
	5 -> To learn a decision forest that uses feature bagging
	
B. Running each file idividually. 
The following package contains the following file :
1. create_dataset.py - It contains the code for creating the Train and the Test data.
	Execution command - python create_dataset.py
	output - Randomly selected 500 positive and 500 Negative reviews for the test as well as train data written in the files.
	
2. create_feature.py - It contains the code for the feature selection.
	Execution command - python create_feature.py
	output - selected-feature-indices.txt file wich contains 2500 words with high +ve average polarity and 2500 words with high -ve average polarity.
	
3. create_decision_tree.py - It prints the accuracy for the given dataset.
	Execution command - python create_decision_tree.py
	output - Accuracy of the data present in Test.txt file when the decision tree is trained on the data inside Train.txt file.
	
4. random_forest.py - It prints the accuracy of the model when trained on the 10 different decision tree.
	Execution command - python random_forest.py
	output - It prints the random forest accuracy for the 10 trees individually and then overall accuracy of the random forest.
	
5. noise_addition.py - Adding noise to the data
	Execution command - python noise_addition.py 
	output - It prints the accuracy on the test data for the 0.1, 0.5, 5, 10 percent of noise addition.
	
6. pruning.py - output of the decision tree when pruning is done to the decision tree.
	Execution command - python pruning.py
	output - It prints the accuracy of the pruned tree.
	
7. early_stopping.py - code for early stopping implementation
	Executiion command - "python early_stopping.py"
	output - It construct the tree using early stopping as a termination condition.
	
8. data files : There are also some data files such as "Train.txt", "Test.txt", "selected-feature-indices.txt".

NOTE - 1. Please do run the "create_feature.py" file after running the "random_forest.py" file. The "random_forest.py" file changes the dimensionality of the selected features.
       2. All the accuracies are for the test data.

==============================================================================================================
Prinshu Kumar
2016csb1051
IIT Ropar
