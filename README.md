# 교육 요인 기반 학업 성취도 예측 모델링
**작성자:** 김종민

**과목:** 머신러닝

---

## 프로젝트 개요
- 이 프로젝트는 **학생의 성적에 영향을 미치는 요인을 데이터 기반으로 분석**하기 위해 수행되었습니다.  
- 학생의 학업 성취는 다양한 요인에 의해 결정되며, 이를 머신러닝 기법을 활용하여 탐구하고자 했습니다.  
- 이를 통해 개인의 학습 전략 개선뿐만 아니라, 교육정책 수립에도 도움을 줄 수 있는 인사이트를 도출하는 것이 목표입니다.

---

## 연구 목표 및 가설
**연구 목표:**  
학생의 시험 성적(Exam_Score)에 유의미한 영향을 주는 요인을 찾는다.

**가설**
1. 수면 시간(Sleep_Hours)은 성적에 긍정적인 영향을 미칠 것이다.  
2. 체육 활동 시간(Physical_Activity)은 성적에 긍정적인 영향을 미칠 것이다.

---

## 데이터 개요
- **출처:** Kaggle - *Student Performance Factors*  
- **데이터 크기:** 6,607개 레코드 × 20개 피처  
- **형식:** CSV 파일  

| Feature | 설명 |
|:--|:--|
| Hours_Studied | 주당 학습 시간 |
| Attendance | 수업 출석률 |
| Parental_Involvement | 학생 교육에 대한 부모의 참여 수준 |
| Access_to_Resources | 교육 자원의 가용성 |
| Extracurricular_Activities | 교외 활동 참여 |
| Sleep_Hours | 밤 평균 수면 시간 |
| Previous_Scores | 이전 시험 점수 |
| Motivation_Level | 동기 수준 (낮음/중간/높음) |
| Internet_Access | 인터넷의 접근 가능성 |
| Tutoring_Sessions | 한 달동안 참석한 과외 세션 수 |
| Family_Income | 가정의 소득 수준 |
| Teacher_Quality | 교사의 질 |
| School_Type | 다니는 학교 유형 |
| Peer_Influence | 또래의 학업 성과에 대한 영향 |
| Physical_Activity | 주당 체육 활동 평균 시간 |
| Learning_Disabilities | 학습 장애의 존재 |
| Parental_Education_Level | 부모의 최고 교육 수준 |
| Distance_from_Home | 집에서 학교까지의 거리 |
| Gender | 학생의 성별 |
| Exam_Score | 최종 시험 점수 (타깃 변수) |

---

## 데이터 전처리 과정
1. **결측치 처리:**  
   - 범주형 변수의 결측치는 **최빈값(mode)** 으로 대체  
2. **범주형 인코딩:**  
   - `LabelEncoder` 대신 `map()`을 사용해 수동 인코딩 (예: Low=0, Medium=1, High=2)  
   - 순위가 존재하는 변수의 의미를 유지  
3. **이상치(outlier) 확인:**  
   - 특별한 이상치는 별견되지 않음  
---

### Linear Regrssion 적용


### Random Forest 적용 및 튜닝
- 기본 모델과 Grid Search로 하이퍼파라미터 최적화 시도  
- R² 변화: -0.017 → -0.015  
  비선형 모델에서도 유의미한 개선은 확인되지 않음

---

### Feature Selection (Sequential Feature Selector)
- 상관계수 0.1 이상인 피처 7개 중 3개 자동 선택  
- 선택된 3개 피처로 모델 학습 시 성능 약간 하락  
  선형모델에서는 더 많은 변수를 사용하는 것이 설명력 향상에 기여

---

## 주요 결과 요약

| 분석 항목 | MSE | R² | 설명 |
|:--|--:|--:|:--|
| Sleep Hours | 14.2 | -0.001 | 영향 없음 |
| Physical Activity | 14.2 | -0.002 | 영향 없음 |
| Attendance | 9.22 | 0.35 | 중간 정도의 양의 상관관계 |
| Hours Studied | 10.46 | 0.23 | 약한 양의 상관관계 |
| Attendance + Hours Studied | 5.81 | 0.59 | 강한 관계 |
| Random Forest (최적화 후) | 14.3 | -0.015 | 비선형에서도 영향 미미 |

---

## 결론 및 배운 점
- 초기 가설(수면·체육)은 **기각**됨  
- 학생 성적에는 **공부시간과 출석률**이 가장 큰 영향을 미침  
- 분석 과정에서 다음과 같은 점을 배우게 됨:
  1. **전처리와 결측치 처리의 중요성**  
  2. **시각화의 효과적 활용** — 단순 수치보다 이해도가 향상  
  3. **모델 선택의 중요성** — 데이터 특성과 모델 특성의 일치 필요  
