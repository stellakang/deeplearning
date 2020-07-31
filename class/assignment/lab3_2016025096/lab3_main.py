import sys
import time 
import random
import numpy as np
from lab3_task1 import task1
from lab3_task2 import task2
from lab3_task3 import task3

m=1000 #the number of training samples
n=100 #the number of test samples
num_of_iter=1000 #the number of iteration
alpha1 = 3.2 #task1 learning rate
alpha2 = 3.5 #task2 learning rate
alpha3 = 3.5 #task3 learning rate

x_train=np.zeros((2,m)) #x_train : 2 x m
y_train=np.zeros(m) #y_train : m x 1
x_test=np.zeros((2,n)) #x_test : 2 x n matrix
y_test=np.zeros(n) #y_test : n x 1 matrix

def initialization():
    #generate m training samples
    for i in range(m):
        x_train[0][i] = random.uniform(-2,2)
        x_train[1][i] = random.uniform(-2,2)
        if x_train[0][i] * x_train[0][i] > x_train[1][i]:
            y_train[i] = 1
        else:
            y_train[i] = 0
    #generate n test samples
    for j in range(n):    
        x_test[0][j] = random.uniform(-2,2)
        x_test[1][j] = random.uniform(-2,2)
        if x_test[0][j] * x_test[0][j] > x_test[1][j]:
            y_test[j] = 1
        else:
            y_test[j] = 0

if __name__ == "__main__":
    
    if len(sys.argv)!=4:
        print("Insufficient arguments")
        sys.exit()
    
    play1 = sys.argv[1]
    play2 = sys.argv[2]
    play3 = sys.argv[3]
    
    initialization()
    
    if play1:
        task1(m,n,num_of_iter,alpha1,x_train,y_train,x_test,y_test)
    if play2:
        task2(m,n,num_of_iter,alpha2,x_train,y_train,x_test,y_test)
    if play3:
        task3(m,n,num_of_iter,alpha3,x_train,y_train,x_test,y_test)
    

