from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SequentialFeatureSelector
import pandas as pd

df = pd.read_csv('StudentPerformanceFactors.csv')

X = df[['Hours_Studied', 'Attendance', 'Parental_Involvement',
        'Access_to_Resources', 'Previous_Scores', 'Motivation_Level', 'Tutoring_Sessions']]
y = df['Exam_Score']

model = RandomForestRegressor(random_state=42)
selector = SequentialFeatureSelector(model, n_features_to_select=3, direction='forward')
selector.fit(X, y)

print("Selected features:", X.columns[selector.support_])
