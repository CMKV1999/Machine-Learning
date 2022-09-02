#Question 1
import statistics

# Statistics module provides functions for calculating mathematical statistics of numeric (Real-valued) data.
# These functions support int, float, decimal and fraction
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Sorted Ages: ", ages) # sort usually sorts in ascending order
print("\nMinimum value of Ages: ", min(ages))
print("\nMaximum value of Ages: ", max(ages))

ages.insert(0,min(ages))
# Insert() method inserts given element at given index list 

ages.append(max(ages))
#The append() method appends an element to the end of the list.

print("\nNew List of ages: ", ages) # Updatesd list of the ages

print("\nMedian of ages: ", statistics.median(ages))
print("\nAverage of ages: ", statistics.mean(ages))
print("\nRange of ages: ", max(ages)-min(ages))

#Question 2

dog = dict()
#Creating a new dictionary named dog
dog.update({"name":"Jack", "color":"Bi-color", "breed":"German Shepherd or Alsatian", "legs":4, "age":6})
# Adding keys and values pairs to the dictionary using update
print("German Breed :",dog)
stud_dict = dict()
stud_dict.update({"first_name":"C M Krishna Vamsi", "last_name":"Mendru", "gender":"Male","age":"23",
                 "marital status":"Single", "skills":["Python","Html"],
                 "country":"India", "city":"Vijayawada", "address":" 64-1-13" })

print("\nStudent Dictionary: ",stud_dict)
print("\nLength of Student Dictionary: ", len(stud_dict))
# len() function gives the length of the values in student dictionary
print("\nSkills Key Value in Student Dictionary: ",stud_dict["skills"])
print("\nData Type of Skills in Student Dictionary: ", type(stud_dict["skills"]))
# type() gives the data type of the skills key in dictionary

stud_dict["skills"].extend(["C Programming", "Java"])
print("Skills after adding new values: ", stud_dict["skills"])
# extend() adds all new values to skills

print("\n",stud_dict.keys())
print(stud_dict.values())  


#Question 3

devils = ("Pujitha","Padmini","Anjum","Pramithi")
# tuples in Python,are immutable, you cannot update it, i.e., you cannot add, change, or remove items (elements) in tuple.
print("Sisters: ", devils)
evils = ("Tarun","Vamsi","Kashyap","Manoj","Aditya")
print("\nBrothers: ", evils)
siblings = devils + evils
print("\nMy siblings: ",siblings)
print("\nNumber of Siblings:", len(siblings))
fam_members = siblings+("Sambsiava Rao","Hemalatha")
print("\nFamily Members: ", fam_members)

#Question 4

IT_companies = {'Apple', 'Oracle','Google','Amazon','Facebook', 'Microsoft', 'IBM'}
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24] 

# First part of the question

print("Length of Set  IT Companies: ",len(IT_companies))
IT_companies.add('Twitter')
#Adding new companies to set using add()
print("\nIT companies: ", IT_companies)
IT_companies.update(['DBS','SAP','Meta','TCS'])
#update() allows to add multiple companies
print("\nIT companies after adding new elements: ",IT_companies)
IT_companies.remove('TCS')
print(IT_companies)

#Second Part of the question

print("\n Difference between Remove() and Discard():")
print("\n The built-in method, discard() in Python, removes the element from the set only if the element is present in the set. If the element is not present in the set, then no error or exception is raised and the original set is printed.")
print("\n The built-in method, remove() in Python, removes the element from the set only if the element is present in the set, just as the discard() method does but If the element is not present in the set, then an error or exception is raised.")
#all set operation can be performed in set: union(), intersection()
#Sets are used to store multiple items in a single variable.
print("\nUnion of A and B sets: ",A.union(B))
#update() will exclude any duplicate items
print("\nIntersection of A and B sets: ",A.intersection(B))
#intersection() method returns a set that contains the similarity between two or more sets

print("\nIs A Subset of B? ",A.issubset(B))
#issubset() method returns True if a set A is a subset of set B.
print("\nAre A and B disjoint sets? ",A.isdisjoint(B))
#isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
print("\nJoin A with B and B with A: ",(A.union(B)).intersection(B.union(A)))
print("\nSymmetric Difference of A with B: ",A.symmetric_difference(B))
#symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
#clear() clears all elements from set
A.clear()
B.clear()
print("\nSet A after the operations: " , A)
print("\nSet B after the operations: " , B)

print("\n Age list: ",age)
age1 = set(age)
print("\nAges(after changing the data_type): ", age1)
print("\nLength of age (data_type is list): ", len(age))
print("\nLength of age (data_type is set): ",len(age1))

#Question 5

from cmath import pi
import math


radius = 30
_area_of_circle_ = pi*pow(radius,2)
_circum_of_circle_ = 2*pi*radius
print("Area of a circle : ", _area_of_circle_,' sq mts')
print("Circumference of a circle : ", _circum_of_circle_, ' mts')

radius = float(input("Enter radius of circle: "))
_area_of_circle_ = pi * pow(radius,2)
print("Area of a circle = ",_area_of_circle_,' sq mts')

#Question 6

txt = "I am a teacher and I love to inspire and teach people"
print(txt)
words = set(txt.split(" "))
print("\nNumber of Unique words: ",len(words), words)

#Question 7
#text = "Name \t Age \tCountry City\nAsabench 250 \tFinland Helsinki"
#print(text)

line1 = "Name \t Age \tCountry City"
#\t gives a tab space while \n takes us to a new line

line2 = "\nAsabench 250 \tFinland Helsinki"
print(line1)
print(line2)

#Question 8
radius = 10 
area = 3.14 * radius ** 2 
print("The area of a circle with radius",radius,"is %.0f" %area, "sq mts.")


#Question 9
no_of_students = int(input("Enter number of students: "))
weight_lbs = list() 
weight_kgs = list() 

for each in range(no_of_students):
    weight_lb = int(input("Enter weight of {} student in lbs: ".format(each+1)))
    weight_lbs.insert(each, weight_lb)
   
    weight_kg = float("%.2f" %(weight_lb*0.453592)) # lb = 0.453592 kg
    weight_kgs.insert(each, weight_kg)
    
print("weight of students in lbs: ",weight_lbs)
print("weight of students in kgs: ",weight_kgs)

#Question 10
import numpy as num    
import pandas as pan  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import confusion_matrix 

M = num.array([[1,0],[2,0],[3,0],[6,0],[6,0],[7,0],[10,0],[11,0]])
print("Dataset with total 8 points: \n",M,"\n Size: ",len(M))
P = num.array([0,0,1,1,1,0,0,0])
print("\nClass label for the datasetM  P:",P)
M_train, M_test, P_train, P_test= train_test_split(M, P, test_size= 0.50, random_state=0,shuffle=False ) 
print("\nTraining Data M: \n", M_train)
print("\nTraining Data label P:", P_train)

stand_scalar= StandardScaler()    
M_train= stand_scalar.fit_transform(M_train)    
M_test= stand_scalar.transform(M_test) 

classifier= KNeighborsClassifier(n_neighbors=3)  
#Fitting the data to classifier
classifier.fit(M_train, P_train)
#Predict Labels for M-test data
P_pred= classifier.predict(M_test) 
print('\nPredicted Classs labels for testing data P:',P_pred)
     

confusion_matrix_result = confusion_matrix(P_test, P_pred)
print("\nConfusion Matrix\n",confusion_matrix_result)


total_value = sum(sum(confusion_matrix_result))
#Accuracy TN+TP / P+N
accuracy=(confusion_matrix_result[0,0]+confusion_matrix_result[1,1])/total_value
print ('\nAccuracy : ', accuracy)

sensitivity = confusion_matrix_result[1,1]/(confusion_matrix_result[1,0]+confusion_matrix_result[1,1])
print('Sensitivity : ', sensitivity )

specificity = confusion_matrix_result[0,0]/(confusion_matrix_result[0,0]+confusion_matrix_result[0,1])
print('Specificity : ', specificity)









