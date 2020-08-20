# Logistic classification(Regression). 

classification 알고리즘 중에서 정확도가 높은 중요한 알고리즘.  

## 기존 Regression  
- H(X) = WX  
- Cost: cost(W) = avg(sum((WX-y)^2))  
- Gradient descent: update w  
- 임의의 점에서 기울기를 이용하여 최소의 cost를 갖는 지점으로 이동한다.  

## Binary Classification  
- 0, 1 encoding : 두가지로 분류  
- linear regression을 이용하여 분류를 하게 되면  
  - 데이터를 따라 기울기가 기울어지므로 제대로 된 분류가 이루어지지 않는다.  
  - hypothesis의 결과값이 0, 1이 아닌 훨씬 벗어난 수가 나타난다.  
- 위와 같은 이유로 linear regression에서의 hypothesis를 바꿔야할 필요성!  
  - H(X) = g(z)  
  - g(z) = 1/(1+e^(-z))   
  - z = WtX  
  
- cost function  
  linear regression의 cost를 활용하면 local minimum이 많이 존재하게 된다.  
  바꿔야할 필요성!  
  
  
  **cost(H(x), b)**  
  y=1일때: -log(H(x))   
  y=0일때: -log(1-H(x))    
  
  그래프를 그려보면 y=1일 때에는 가설이 0에 가까울수록 cost가 커지고  
  y=0일 때에는 가설이 1에 가까울수록 cost가 커지도록 한다.  

  하나로 나타내면!  
  Cost(W) = avg(sum(c(H(x),y)))  
  c(H(x), y) = -ylog(H(x))-(1-y)log(1-H(x))  
  
- 과정  
  - hypothesis 구하기  
  - cost function 계산  
  - gradient descent algorithm을 이용하여 update  
