# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

data = pd.read_csv('AmazonEmployeeAccess.csv')
print("Amazon Employee Access")

X = data.iloc[:,:-1]
Y = data.iloc[:,-1:]


from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X,Y)

user_data = [[]]

r_n = int(input("Enter Resource Number : "))
user_data[0].append(r_n)
m_i = int(input("Enter your MGR ID : "))
user_data[0].append(m_i)
RR_1 =  int(input("Enter Role Role Up 1: "))
user_data[0].append(RR_1)
RR_2 =  int(input("Enter Role Role Up 2: "))
user_data[0].append(RR_2)
RR_D =  int(input("Enter Role Department: "))
user_data[0].append(RR_D)
R_T =  int(input("Enter Role Title Number: "))
user_data[0].append(R_T)
RF_D =  int(input("Enter Role Family Desc Number: "))
user_data[0].append(RF_D)
RF_N =  int(input("Enter Role Family Number: "))
user_data[0].append(RF_N)


result = model.predict(user_data)