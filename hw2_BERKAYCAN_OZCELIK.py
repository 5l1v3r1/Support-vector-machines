#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Reading the test set
import pandas as pd
dtest = pd.read_csv(r"C:\Users\user\Desktop\EE-HW2\datatest.txt",delimiter = ',')
dtest.head()


# In[3]:


#Reading the train set
dtrain = pd.read_csv(r"C:\Users\user\Desktop\EE-HW2\datatraining.txt",delimiter = ',')
dtrain.head()


# In[4]:


#Spliting the train and test sets and Defining the labels
X_train = dtrain[['Temperature','Humidity','Light','CO2','HumidityRatio']]
X_test = dtest[['Temperature','Humidity','Light','CO2','HumidityRatio']]
y_train = dtrain[['Occupancy']]
y_test = dtest[['Occupancy']]


# In[6]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score


# In[7]:


#Creating arrays for each pair C and Y
ArrayC = [0.1,1,10]
ArrayY = [0.01,0.1,1]
#Creating empty arrays to hold each output for the given C and Y inputs
Accuracy = [0,0,0]
KfoldCrossVal = [0,0,0]

from sklearn import svm
from sklearn import metrics

#Main loop where we seperate the data into N (10) Folds and train the model with the training set
for x in range(3):
    svc = svm.SVC(kernel='linear', gamma = ArrayY[x], C=ArrayY[x]).fit(X_train,y_train)
    KFolds = KFold(n_splits=10,shuffle=False)
    KfoldCrossVal[x] = cross_val_score(svc,X_train,y_train,cv=10).mean()
    sm = svc.fit(X_train,y_train)
    y_pred = sm.predict(X_train)
    Accuracy[x] = metrics.accuracy_score(y_train,y_pred)


# In[8]:


#Getting the Max value in the Accuracy Array and finding the index of it so we can find the best values for C,Y
max_value = max(Accuracy)
max_index = Accuracy.index(max_value)
ArrayC[max_index],ArrayY[max_index]


# In[9]:


#Training the model with the best C,Y pair and calculating the final accuracy score
svc = svm.SVC(kernel='linear', gamma = ArrayY[max_index], C=ArrayY[max_index]).fit(X_test,y_test)
KFolds = KFold(n_splits=10,shuffle=False)
KfoldCrossVal_final = cross_val_score(svc,X_test,y_test,cv=10).mean()
sm = svc.fit(X_test,y_test)
y_pred = sm.predict(X_test)
Accuracy_final = metrics.accuracy_score(y_test,y_pred)


# In[18]:


#Asign the best C,Y pair to Best_CY
Best_CY = ArrayC[max_index],ArrayY[max_index]


# In[19]:


#Generate confusion matrix for test set predictions
from sklearn.metrics import confusion_matrix
Conf_matrix = confusion_matrix(y_test, y_pred)


# In[20]:


#Outputs of the homework - Confusion Matrix - Best pair values of C,Y - Accuracy on test set
Conf_matrix, Best_CY, Accuracy_final


# In[ ]:





# In[ ]:




