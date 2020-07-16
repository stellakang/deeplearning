import time 
import random
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def cross_entropy_cost(m, y_hat, y):
    return -(1.0/m) * (np.dot(np.log(y_hat), y.T) + np.dot(np.log(1-y_hat), (1-y).T))

def task1(m,n,num_of_iter,alpha1,x_train,y_train,x_test,y_test):  
    print('========= task1 =========')
    #task1 variables
    w=np.zeros((2,1))
    b=0.0
    start = time.time()
    for t in range(num_of_iter):
        #task1 train
        z = np.dot(w.T,x_train)+b
        a = sigmoid(z)
        
        dz = a - y_train
        dw = np.dot(x_train,dz.T)/m
        db = np.sum(dz)/m

        #task1 update
        w -= alpha1*dw
        b -= alpha1*db

    train_time = time.time()-start
    
    cost_train=0.0
    cost_test=0.0
    train_accuracy = 0.0
    test_accuracy = 0.0
    
    #train set accuracy
    z = np.dot(w.T,x_train)+b
    a = sigmoid(z)
    y_hat = a.round()
    train_accuracy = np.sum(y_hat==y_train)/m*100
    cost_train = cross_entropy_cost(m, a, y_train)
    print('train cost : %f'% cost_train)
    print('train accuracy : %f'%train_accuracy)
    
    #calculate cost with n test samples
    start1 = time.time()
    z = np.dot(w.T,x_test)+b
    a = sigmoid(z)
    test_time = time.time()-start1
    cost_test = cross_entropy_cost(n, a, y_test)
    y_hat = a.round()
    test_accuracy = np.sum(y_hat==y_test)/n*100
    
    print('test cost : %f'% cost_test)
    print('test accuracy : %f'%test_accuracy)

    print('train time : ',train_time)
    print('test time : ',test_time)

