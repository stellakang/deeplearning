# Softmax Regression  

softmax Regression이란 기존에 배웠던 logistic classification에서 더 나아가서  
`Multinomial classification` 을 하기위한 학습 방법이다!   

logistic regression과 동일하게  
1) 가설 설정  
2) cost function 계산  
3) gradient descent로 weight 업데이트  

예를 들어, A,B,C로 분류하는 경우 logistic regression을 사용하면   
A or not A/ B or not B/ C or not C 로 나누어서 계산할 수 있다.   
이는 아래와 같이 행렬 곱셈으로 간단하게 나타낼 수 있다.     

|Wa1 Wa2 Wa3||x1|   |yA|  
|Wb1 Wb2 Wb3||x2| = |yB|  
|Wc1 Wc2 Wc3||x3|   |yC|  

그렇다면 sigmoid는 어디에 위치해야할까?  
기존에는 Wx를 구한 후에 sigmoid 함수를 거쳐서 확률값을 구했는데  
여기서는 sigmoid 대신 `softmax`를 사용하여 확률값으로 나타내어준다.  

## Softmax  
- S(yi) = e^yi/sum(e^yi)  
- 0과 1사이의 값  
- 전체의 합 = 1  

## One-Hot Encoding  
- 가장 큰 값을 1로 두고, 나머지는 0으로 변환  
- argmax 사용  

## Cost function : Cross-entropy    
- D(S, L) = -sum(Li log(Si))  
- Li는 클래스 i에 대한 실제 값(클래스 i에 속하면 1, 아니면 0)  
  Si는 클래스 i에 대한 예측값을 one hot encoding으로 나타낸 것(y hat)  
- Logistic regression의 cost function은 binary에 관여하는 것일뿐 서로 차이가 없다.  

## Gradient descent  
이후에 Gradient descent로 cost function을 minimize하는 weight 값을 구한다.  
