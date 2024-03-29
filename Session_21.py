# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:24:20 2019

@author: CNsasi
"""
#importing libraries
import numpy as np
import statsmodels.api as sm
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
dta = sm.datasets.fair.load_pandas().data

# add "affair" column: 1 represents having affairs, 0 represents not
dta['affair'] = (dta.affairs > 0).astype(int)
y, X = dmatrices('affair ~ rate_marriage + age + yrs_married + children + \
religious + educ + C(occupation) + C(occupation_husb)',
dta, return_type="dataframe")
X = X.rename(columns = {'C(occupation)[T.2.0]':'occ_2',
'C(occupation)[T.3.0]':'occ_3','C(occupation)[T.4.0]':'occ_4',
'C(occupation)[T.5.0]':'occ_5',
'C(occupation)[T.6.0]':'occ_6',
'C(occupation_husb)[T.2.0]':'occ_husb_2',
'C(occupation_husb)[T.3.0]':'occ_husb_3',
'C(occupation_husb)[T.4.0]':'occ_husb_4',
'C(occupation_husb)[T.5.0]':'occ_husb_5',
'C(occupation_husb)[T.6.0]':'occ_husb_6'})
y = np.ravel(y)

#splitting data into training and test set
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size=0.30, random_state=101)

#Fitting Random Forest Regressor to the Training Test
logmodel=LogisticRegression()
logmodel.fit(X_train,y_train)

#Predicting the test set results
predictions=logmodel.predict(X_test)

#measure accuracy
from sklearn.metrics import confusion_matrix
accuracy=confusion_matrix(y_test,predictions)

#accuracy score
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,predictions)



