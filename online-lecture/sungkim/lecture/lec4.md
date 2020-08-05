# Multi-variable linear regression.  

## Multi-variable  
- 원래는 input 값이 한 개였는데 여기서는 여러 개의 input으로 regression을 해야 한다.  
- 3개인 경우: H(x1, x2, x3) = w1x1 + w2x2 + w3x3 + b   
- n개인 경우: H(x1, x2, ... xn) = w1x1 + w2x2 + ... + wnxn + b  
- cost function 계산하는 식 동일  

## Matrix  
- 여러 개의 인풋에 대해서 계산을 할 때에는 matrix multiplication을 사용한다.  
- Hypothesis  
  **H(X) = XW**   
  w1x1 + w2x2 + w3x3 + ... + wnxn   
- 한 pair의 인풋이 아니라 여러 개의 인풋에 대해서도 행렬로 나타낼 수 있다.  
  - 각 행을 한 pair로 나타낸다.  
    the number of instances = 행의 수   
    

## Summarize  
- Lecture(theory)  
  H(x) = Wx + b  
- Implementation(Tensorflow)  
  H(X) = XW  
  
