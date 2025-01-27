# -*- coding: utf-8 -*-
"""Multivariate_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E09VoHH689bRHKwNWVRmuwZmPQY_D39v
"""

#Import all dependencies
from google.colab import files
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stat
import numpy as np
from google.colab import drive

#Upload data
uploaded_train = files.upload()
uploaded_test=files.upload()

train_df = pd.read_csv(io.BytesIO(uploaded_train['train_data.csv']))
test_df=pd.read_csv(io.BytesIO(uploaded_test['test_data.csv']))

#Data size understanding
print(train_df.head)
print(train_df.columns)

#Assigning X_train,Y_train
X_train=train_df[train_df.columns[0:4]]
print(X_train.head)
Y_train=train_df[train_df.columns[4]]
Y_train.head

#Calculate m and n
m=len(X_train.index)
n=len(X_train.columns)

#Understanding the data values and distribution
#Individual histograms
X_train.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,
           xlabelsize=8, ylabelsize=8, grid=False)    
plt.tight_layout(rect=(0, 0, 1.2, 1.2))

#Pair wise scatter plots
# Pair-wise Scatter Plots
cols = ['T', 'V', 'P', 'RH','E']
pp = sns.pairplot(train_df[cols], size=1.8, aspect=1.8,
                  plot_kws=dict(edgecolor="k", linewidth=0.5),
                  diag_kind="kde", diag_kws=dict(shade=True))

fig = pp.fig 
fig.subplots_adjust(top=0.93, wspace=0.3)
t = fig.suptitle('Ambient variables and Net daily generated Electricity', fontsize=14)

#Feature normalization
X_train_normal=X_train
for i in range(n):
  column=X_train_normal[X_train_normal.columns[i]]
  X_train_normal[X_train_normal.columns[i]]=(column-stat.mean(column))/(max(column)-min(column))

#Data analysis after normalization
X_train_normal.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,
           xlabelsize=8, ylabelsize=8, grid=False)    
plt.tight_layout(rect=(0, 0, 1.2, 1.2))

cols = ['T', 'V', 'P', 'RH','E']
pp = sns.pairplot(train_df[cols], size=1.8, aspect=1.8,
                  plot_kws=dict(edgecolor="k", linewidth=0.5),
                  diag_kind="kde", diag_kws=dict(shade=True))

fig = pp.fig 
fig.subplots_adjust(top=0.93, wspace=0.3)
t = fig.suptitle('Ambient variables and Net daily generated Electricity', fontsize=14)

"""# New Section"""

#Parameter vector
theta=[1 *1]*(n+1)
theta=np.array(theta)
np.shape(theta)
theta=theta.reshape((n+1),1)
np.shape(theta)

#Adding another column of ones in X_train
ones=[1 for i in range(m)]
#learning rate
step=0.01

#Threshold can be used for convergence detection while Gradient descent
threshold=[pow(10,-4)*1]*(n+1)
threshold=np.array(threshold)
threshold=threshold.reshape((n+1),1)

X_train.insert(0,'Ones',ones)

#Gradient descent


for i in range(1000):
  theta=theta-((step*(1/m))*(np.dot(np.dot(theta.T,X_train.T),X_train))).T

  

theta

test_df.head
ones=[1*1]*len(test_df.index)
test_df.insert(0,'One',ones)
test_df

#Prediction
y_pre=np.dot(test_df,theta)

y_pre
np.shape(y_pre)

#Saving predicted output in a csv file
import csv

file_name_csv= y_pre

f=open("file_name_csv.csv", "w")

writer = csv.writer(f)

writer.writerows(file_name_csv)

