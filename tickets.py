# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:29:39 2016

@author: charles
"""

import csv as csv
import numpy as np
import matplotlib.pyplot as plt

#Read the file and data
csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next() 						
data=[] 

#Put the data in an array
for row in csv_file_object: 							
    data.append(row[0:]) 								
data = np.array(data) 									

#Separate the 1st class, 2nd class and 3rd class passengers
c1_stats = data[0::,2] == "1" 	
c2_stats = data[0::,2] == "2" 	
c3_stats = data[0::,2] == "3"

#Find male and female passengers in each class
c1f_stats = data[c1_stats,4] == "female"
c2f_stats = data[c2_stats,4] == "female"
c3f_stats = data[c3_stats,4] == "female"
c1m_stats = data[c1_stats,4] == "male"
c2m_stats = data[c2_stats,4] == "male"
c3m_stats = data[c3_stats,4] == "male"

#Survival data of all passengers from each class
c1_onboard = data[c1_stats,1].astype(np.float)
c2_onboard = data[c2_stats,1].astype(np.float)
c3_onboard = data[c3_stats,1].astype(np.float)

#Proportion of all passengers who survived from each class
prop_c1_survived = np.sum(c1_onboard) / np.size(c1_onboard)
prop_c2_survived = np.sum(c2_onboard) / np.size(c2_onboard)
prop_c3_survived = np.sum(c3_onboard) / np.size(c3_onboard)

#Survival data of male and female passengers from each class
c1f_onboard = data[c1f_stats,1].astype(np.float)
c2f_onboard = data[c2f_stats,1].astype(np.float)
c3f_onboard = data[c3f_stats,1].astype(np.float)
c1m_onboard = data[c1m_stats,1].astype(np.float)
c2m_onboard = data[c2m_stats,1].astype(np.float)
c3m_onboard = data[c3m_stats,1].astype(np.float)

#Proportion of male and female passengers who survived from each class
prop_c1f_survived = np.sum(c1f_onboard) / np.size(c1f_onboard)
prop_c2f_survived = np.sum(c2f_onboard) / np.size(c2f_onboard)
prop_c3f_survived = np.sum(c3f_onboard) / np.size(c3f_onboard)
prop_c1m_survived = np.sum(c1m_onboard) / np.size(c1m_onboard)
prop_c2m_survived = np.sum(c2m_onboard) / np.size(c2m_onboard)
prop_c3m_survived = np.sum(c3m_onboard) / np.size(c3m_onboard)

#Print all results
print 'Proportion of people in class1 who survived is %s' % prop_c1_survived
print 'Proportion of people in class2 who survived is %s' % prop_c2_survived
print 'Proportion of people in class3 who survived is %s' % prop_c3_survived

print 'Proportion of female in class1 who survived is %s' % prop_c1f_survived
print 'Proportion of female in class2 who survived is %s' % prop_c2f_survived
print 'Proportion of female in class3 who survived is %s' % prop_c3f_survived
print 'Proportion of male in class1 who survived is %s' % prop_c1m_survived
print 'Proportion of male in class2 who survived is %s' % prop_c2m_survived
print 'Proportion of male in class3 who survived is %s' % prop_c3m_survived

#Bar plots of the proportion of survivors 
N = 3
t_prop = (prop_c1_survived, prop_c2_survived, prop_c3_survived)
f_prop = (prop_c1f_survived, prop_c2f_survived, prop_c3f_survived)
m_prop = (prop_c1m_survived, prop_c2m_survived, prop_c3m_survived)
index = np.arange(N)
width = 0.25

p1 = plt.bar(index, t_prop, width, color='r')
p2 = plt.bar(index+width, f_prop, width, color='y')
p3 = plt.bar(index+(2*width), m_prop, width, color='b')
             
plt.xlabel('Class')
plt.ylabel('Proportion of the survivors')
plt.title('Proportion of the Titanic survivors based on class and gender')
plt.xticks(index + (3*width/2), ('1st class', '2nd class', '3rd class'))
plt.yticks(np.arange(0, 0.71, 0.1))
plt.legend((p1, p2, p3), ('Total','Female', 'Male'))

plt.tight_layout()
plt.show()

