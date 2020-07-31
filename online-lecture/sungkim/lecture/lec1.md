# Machine Learning.   

## Concept  
### 1. Limitations of explicit programming.  
- spam filter: many rules.  
- automatic driving: too many rules.  
- 이렇게 하나씩 모두 프로그래밍하지 말고 데이터를 보고 학습  

## 2. Machine learning  
*" Field of study that gives computers  
the ability to learn without being explicitly programmed"    
Arthur Samuel(1959)*  

## 3. Supervised/Unsupervised learning  

### Supervised learning  
- learning with labeled examples - training set  
- Examples  
  - Image labeling: learning from tagged images  
  - Email spam filter: learning from labeled(spam or ham) email  
  - Predicting exam score: learning from previous exam score and time spent  

- Types  
  - Regression  
    예) 시험 점수를 공부하는 시간에 따라 어떻게 되는지 예측할 때  
  - (binary) classification  
    예) 공부하는 시간에 따라서 시험을 통과하는지, 통과하지 못하는지 예측할 때
  - (multi-label) classification  
    예) 공부하는 시간에 따라 시험 점수(A, B, C, D, E, F)를 예측할 때  
  
### Unsupervised learning  
- un-labeled data: 라벨없이 비슷한 것끼리 그룹화한다.    
- Google news grouping  
- Word clustering  
