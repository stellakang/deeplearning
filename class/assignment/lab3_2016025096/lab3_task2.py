import time 
import random
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def cross_entropy_cost(m, y_hat, y):
    return -(1.0/m) * (np.dot(np.log(y_hat), y.T) + np.dot(np.log(1-y_hat), (1-y).T))

def task2(m,n,num_of_iter,alpha2,x_train,y_train,x_test,y_test):
    print('========= task2 =========')
    #task2 variables
    w1=np.zeros((1,2))
    b1=np.zeros((1,1))
    w2=np.zeros((1,1))
    b2=np.zeros((1,1))

    start = time.time()
    for t in range(num_of_iter):
        #task2 train
        z1 = np.dot(w1,x_train)+b1
        a1 = sigmoid(z1)
        z2 = np.dot(w2,a1)+b2
        a2 = sigmoid(z2)

        dz2 = a2-y_train
        dw2 = np.dot(dz2,a1.T)/m
        db2 = np.sum(dz2, axis=1,keepdims=True)/m
        dz1 = np.multiply(np.dot(w2.T,dz2),np.multiply(a1,1-a1))
        dw1 = np.dot(dz1,x_train.T)/m
        db1 = np.sum(dz1,axis=1,keepdims=True)/m 

        #task2 update
        w2 -= alpha2*dw2
        b2 -= alpha2*db2
        w1 -= alpha2*dw1
        b1 -= alpha2*db1

    train_time = time.time()-start    
    cost_train=0.0
    cost_test=0.0
    train_accuracy = 0.0
    test_accuracy = 0.0
      
    #train set cost and accuracy
    z1 = np.dot(w1,x_train)+b1
    a1 = sigmoid(z1)
    z2 = np.dot(w2,a1)+b2
    a2 = sigmoid(z2)
    cost_train = cross_entropy_cost(m, a2, y_train)
    y_hat = a2.round()
    train_accuracy = np.sum(y_hat==y_train)/m*100
    print('train cost : %f'% cost_train)
    print('train accuracy : %f'%train_accuracy)
    
    #calculate cost and accuracy with n test samples
    start1 = time.time()
    z1 = np.dot(w1,x_test)+b1
    a1 = sigmoid(z1)
    z2 = np.dot(w2,a1)+b2
    a2 = sigmoid(z2)
    test_time = time.time()-start1
    cost_test = cross_entropy_cost(n, a2, y_test)
    y_hat = a2.round()
    test_accuracy = np.sum(y_hat==y_test)/n*100
    print('test cost : %f'% cost_test)
    print('test accuracy : %f'%test_accuracy)

    print('train time : ',train_time)
    print('test time : ',test_time)

