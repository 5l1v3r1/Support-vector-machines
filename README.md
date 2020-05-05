# Support-vector-machines

The aim of this project is to
  i. Understand concept of cross-validation
  ii. Apply cross-validation with Support Vector Machines on a sample dataset
  
Steps to do in the projects
  1. Read the data from the .txt files. Store the training and test data in two different
  variables.
  2. Define search space for SVM parameters. The values you need to use are
    i. 􀜥 = [0.1,1,10]
    ii. 􀟛 = [0.01,0.1,1]
  3. Write a function that separates the data into k folds and performs cross validation. The
  name of the function should be “k_fold_cv”. This function is expected to work with k=5
  and k=10. When calculating the performance of a model, you need to use classification
  accuracy. Since k-fold cross validation should be repeated for every possible pair of 􁈺􀜥,􀟛􁈻, these values should be introduced to the function as well.
    i. Input of the function: k (integer), training set, possible values for 􀜥, possible
    values for 􀟛
    ii. Output of the function: best 􁈺􀜥,􀟛􁈻 pair giving the highest CV accuracy
  4. Train a model on the entire training set using the best parameters found at step 3.
  5. Test the model on step 4 on the test set
    i. Generate confusion matrix for test set predictions
    ii. print the classification accuracy on test set
    iii. print the best 􁈺􀜥,􀟛􁈻 pair found at step 3
    
    
The overall structure of the program should be something like this:
  i. Specify an integer value for k (either 5 or 10 is ok)
  ii. Separate the training data into k-folds
  iii. Calculate k-fold cross validation accuracy on SVM models for all possible 􁈺􀜥,􀟛􁈻
  pairs
  iv. Store the 􁈺􀜥,􀟛􁈻 pair that gives the highest cross validation accuracy as 􁈺􀜥􀯕􀯘􀯦􀯧,􀟛􀯕􀯘􀯦􀯧􁈻
  v. Train an SVM model using 􁈺􀜥􀯕􀯘􀯦􀯧,􀟛􀯕􀯘􀯦􀯧􁈻 on the entire training set
  vi. Test your model in the previous step on the test set
