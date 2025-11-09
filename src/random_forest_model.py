from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

df = pd.read_csv('StudentPerformanceFactors.csv')

X = df[['Sleep_Hours', 'Physical_Activity']]
y = df['Exam_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 기본 모델
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
print("Base R²:", r2_score(y_test, rf.predict(X_test)))

# Grid Search
params = {'n_estimators':[100,200, 300], 'max_depth':[None,10,20, 30], 'min_samples_split':[2,5, 10]}
grid = GridSearchCV(rf, params, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)

best = grid.best_estimator_
print("Best Params:", grid.best_params_)
print("Optimized R²:", r2_score(y_test, best.predict(X_test)))
